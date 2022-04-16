import os
import sys
from datetime import datetime, timedelta
from utils.DomainUtils import DomainUtils
import enum
from multipledispatch import dispatch
from service.PwdGenerator import PwdGenerator as Generator

class Status(enum.Enum):
    CREATED = 0
    ACTIVE = 1
    SUSPENDED = 2
    EXPIRED = 3
    ABOUT_TO_EXPIRE = 4

class PasswordPattern:
    def __init__(self,pwd_size=16,pwd_min_num_req=1,pwd_min_upper_req=1,pwd_min_special_req=1,pwd_special_req=1) -> None:
        self._pwd_size=pwd_size
        self._pwd_min_num_req=pwd_min_num_req
        self._pwd_min_upper_req=pwd_min_upper_req
        self._pwd_min_special_req=pwd_min_special_req
        self._pwd_special_req=pwd_special_req
    
    def __str__(self) -> str:
        to_string = f'PasswordPattern[pwd_size:{self.pwd_size},pwd_min_num_req:\'{self.pwd_min_num_req}\',pwd_min_upper_req=pwd_min_upper_req:\'{self.pwd_min_upper_req}\',pwd_min_special_req:{self.pwd_min_special_req},pwd_special_req:{self.pwd_special_req}]'
        return DomainUtils.correct_obj_str_format(to_string)

    def pwd_size(self):
        return self._pwd_size
    
    def pwd_min_num_req(self):
        return self._pwd_min_num_req

    def pwd_min_upper_req(self):
        return self._pwd_min_upper_req

    def pwd_min_special_req(self):
        return self._pwd_min_special_req

    def pwd_special_req(self):
        return self._pwd_special_req


class Credentials:
    
    @dispatch(int,str,str,datetime,datetime,datetime,PasswordPattern,Status)
    def __init__(self, host_id, username, password, date_created, date_pwd_updated, date_pwd_expires, pwd_pattern, status = Status.CREATED) -> None:
        self._host_id = host_id
        self._username = username
        self._password = password
        self._date_created = date_created
        self._pwd_updated_date = date_pwd_updated
        self._pwd_expiration_date = date_pwd_expires
        self._pwd_pattern = pwd_pattern
        self._status = status

    @dispatch(int,str,datetime,datetime,datetime,PasswordPattern,Status)
    def __init__(self, host_id, username, date_created, date_pwd_updated, date_pwd_expires, pwd_pattern, status = Status.CREATED) -> None:
        self._host_id = host_id
        self._username = username
        self._password = self.generate_and_update_pwd(pwd_pattern)
        self._date_created = date_created
        self._pwd_updated_date = date_pwd_updated
        self._pwd_expiration_date = date_pwd_expires
        self._pwd_pattern = pwd_pattern
        self._status = status

    def __str__(self) -> str:
        to_string = f'Credentials[host_id:{self._host_id},user_name:\'{self._user_name}\',password:\'{self._password}\',date_created:{self._date_created},date_pwd_expires:{self._date_pwd_expires},status:{self._status}]'
        return DomainUtils.correct_obj_str_format(to_string)

    def host_id(self):
        return self._host_id

    def username(self):
        return self._username


    def password(self):
        return self._password

    def date_created(self):
        return self._date_created

    def pwd_updated_date(self):
        return self._pwd_updated_date

    def pwd_expiration_date(self):
        return self._pwd_expiration_date

    def pwd_pattern(self):
        return self._pwd_pattern

    def status(self):
        return self._status

    def generate_and_update_pwd(self, pwd_pattern, pwd_retention_in_hours):
        self._password = Generator.generatePassword(pwd_pattern)
        self._date_pwd_updated = datetime.today()
        self._date_pwd_expires = self.calc_exp_date(self._date_pwd_updated,pwd_retention_in_hours)

    def calc_exp_date(date, retention_in_hours):
        return date + timedelta(hours=retention_in_hours)

    def validate_pwd_pattern(pwd_pattern):
        if type(pwd_pattern) is not dict or\
            'length' not in pwd_pattern.keys() or\
                type(pwd_pattern['length']) is not int or\
                    'upper' not in pwd_pattern.keys() or\
                        type(pwd_pattern['upper']) is not int or\
                            'num' not in pwd_pattern.keys() or\
                                type(pwd_pattern['num']) is not int or\
                                    'special' not in pwd_pattern.keys() or\
                                        type(pwd_pattern['special']) is not int:
                                        return False
        return True

    def update_validity(self, pwd_retention_in_hours):
        expiration_date_delta = self._pwd_expiration_date - datetime.today().date()
        if expiration_date_delta.days <= 0:
            self.status = Status.EXPIRED.name
        elif expiration_date_delta.days <= 5:
            self.status = Status.ABOUT_TO_EXPIRE.name

    def activate(self):
        if self.status == 'CREATED' or self.status == 'SUSPENDED':
            self.status = Status.ACTIVE.name
            return True
        else:
            print(f'Unable to activate... current Status is {self.status}')
            return False

    def suspend(self):
        if self.status == 'CREATED' or self.status == 'ACTIVE':
            self.status = Status.SUSPENDED.name
            return True
        else:
            print(f'Unable to suspend... current Status is {self.status}')
            return False



