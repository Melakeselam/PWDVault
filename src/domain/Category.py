import os
import sys
from src.utils.DomainUtils import DomainUtils
from multipledispatch import dispatch

HOURS_IN_A_DAY = 24
HOURS_IN_A_MONTH = 720
HOURS_IN_A_YEAR = 8640
DAYS_IN_A_MONTH = 30
DAYS_IN_A_YEAR = 365
MONTHS_IN_A_YEAR = 12


class PasswordRetentionPeriod:

    def __init__(self, years=0, months=0, days=0, hours=0):
        self._years = years
        self._months = months
        self._days = days
        self._hours = hours

    def __str__(self) -> str:
        to_string = f'[years:{self._years},months:{self._months},days:{self._days},hours:{self._hours}]'
        return DomainUtils.correct_obj_str_format(to_string)

    def in_hours(self) -> int:
        hours = self._hours + (self._days * HOURS_IN_A_DAY) + \
            (self._months * HOURS_IN_A_MONTH) + \
            (self._years * HOURS_IN_A_YEAR)
        return int(hours)

    def in_days(self) -> int:
        days = (self._hours / HOURS_IN_A_DAY) + self._days + \
            (self._months * DAYS_IN_A_MONTH) + \
            (self._years * DAYS_IN_A_YEAR)
        return int(days)

    def values(self):
        return [self._years,self._months,self._days,self._hours]


class Category:

    def __init__(self, platform_id, name, description=None,  password_retention_period=PasswordRetentionPeriod(months=3)):
        self._platform_id = platform_id
        self._name = name
        self._description = description
        self._password_retention_period = self.correct_time_distribution(
            password_retention_period)

    def __str__(self) -> str:
        to_string = f'Category[platform_id:{self._platform_id},name:\'{self._name}\',descritpion:\'{self._description}\',password_retention_period:{self._password_retention_period}]'
        return DomainUtils.correct_obj_str_format(to_string)

    def platform_id(self):
        return self._platform_id

    @dispatch()
    def name(self):
        return self._name

    @dispatch()
    def description(self):
        return self._description

    @dispatch()
    def password_retention_period(self):
        return self._password_retention_period

    @dispatch(str)
    def name(self, name):
        self._name = name

    @dispatch(str)
    def description(self, description):
        self._description = description

    @dispatch(PasswordRetentionPeriod)
    def password_retention_period(self, password_retention_period):
        self._password_retention_period = self.correct_time_distribution(
            password_retention_period)

    def correct_time_distribution(self, period=PasswordRetentionPeriod()):
        hours = period._hours
        days = (hours // HOURS_IN_A_DAY) + period._days
        hours = hours % HOURS_IN_A_DAY
        months = days // DAYS_IN_A_MONTH + period._months
        days = int(days % DAYS_IN_A_MONTH)
        years = int(months // MONTHS_IN_A_YEAR) + period._years
        months = int(months % MONTHS_IN_A_YEAR)
        return PasswordRetentionPeriod(years, months, days, hours)

    def values(self):
        return [self._platform_id,self._name,self._description,self._password_retention_period]