from domain.Credentials import Credentials
from utils.DomainUtils import DomainUtils
from multipledispatch import dispatch


class HostDto:
    _user_id = -1
    _id = -1
    _name = None
    _address = None
    _platform_id = -1
    _category_name = None
    _credentials = None
    _custom_pwd_retention_period_in_hours = 0
    @dispatch(int, int, str, int, str, Credentials, str, int)
    def __init__(self, user_id: int, host_id: int, host_name: str, platform_id: int, category_name: str, credentials: Credentials, host_address: str, custom_pwd_retention_period_in_hours: int = 0):
        self._user_id = user_id
        self._id = host_id
        self._name = host_name
        self._address = host_address
        self._platform_id = platform_id
        self._category_name = category_name
        self._credentials = credentials
        self._custom_pwd_retention_period_in_hours = custom_pwd_retention_period_in_hours

    @dispatch(int, str, int, str, Credentials, str)
    def __init__(self, host_id: int, host_name: str, platform_id: int, category_name: str, credentials: Credentials, host_address: str):
        self._id = host_id
        self._name = host_name
        self._address = host_address
        self._platform_id = platform_id
        self._category_name = category_name
        self._credentials = credentials

    @dispatch(int, str, int, str, str, int)
    def __init__(self, host_name: str, platform_id: int, category_name: str, host_address: str, custom_pwd_retention_period_in_hours: int):

        self._name = host_name
        self._address = host_address
        self._platform_id = platform_id
        self._category_name = category_name
        self._custom_pwd_retention_period_in_hours = custom_pwd_retention_period_in_hours

    def __str__(self) -> str:
        to_string = f'[user_id:\'{self._user_id}\',host_id:\'{self._id}\',host_name:\'{self._name}\',platform_id:\'{self._platform_id}\',category_name\'{self._category_name}\',address:\'{self._address}\',custom_pwd_retention_period_in_hours:\'{self._custom_pwd_retention_period_in_hours}\']'
        return DomainUtils.correct_obj_str_format(to_string)

    def user_id(self):
        return self._user_id

    def id(self):
        return self._id

    def name(self):
        return self._name

    @dispatch()
    def address(self):
        return self._address

    def platform_id(self):
        return self._platform_id

    def category_name(self):
        return self._category_name

    def credentials(self) -> Credentials:
        return self._credentials

    @dispatch()
    def custom_pwd_retention_period_in_hours(self):
        return self._custom_pwd_retention_period_in_hours

    @dispatch(str)
    def address(self, address):
        self._address = address

    @dispatch(int)
    def custom_pwd_retention_period_in_hours(self, hours):
        self._custom_pwd_retention_period_in_hours = hours
