from re import I
from unicodedata import name
from xmlrpc.client import DateTime
from datetime import datetime, timedelta

from domain.Credentials import Credentials
from domain.Platform import Platform
from domain.Category import Category, PasswordRetentionPeriod
from service.dtos.PlatformDto import PlatformDto
from service.adaptors.PlatformDtoAdaptor import PlatformDtoAdaptor as adaptor

# onlinePlatform = Platform(1, "online", "this is an online platform")
# financeCategory = Category(
#     1, "finance", "financial websites", 1, CredentialsRetentionPeriod(hours=180))
# print(onlinePlatform)
# print(financeCategory)
# print(financeCategory.pwd_retention_in_months(), "months")

# mycredentials = Credentials('01',Domain('Gmail','www.gmail.com', 1), 'melak', 'melak123')
# print(mycredentials)

today = datetime.today()
tomorrow = today + timedelta(days=1)
print(tomorrow)
# print(today)
# print(datetime.timetz(today))
# print(DateTime(datetime.today()))

# test = dict(ContactName = 'Alfred Schmidt', City = 'Frankfurt')

# for field in test.keys():
#     print(field,f': \'{test[field]}\'')
# print(str(test).replace('{','').replace('}','').replace(':',' ='))

# test = {"one":1, "two":2, "three":3}
# for num in test.values():
#     print(num)

# obj = PlatformDto(1,'online','online')
# print(obj)
# obj = PlatformDto(None,'online','online')
# print(obj)
# obj = PlatformDto(1,)
# print(obj)
# obj = PlatformDto(None)
# print(obj)

# obj = PlatformDto(None,'online',None)
# print(adaptor.dto_to_model(obj))
# obj = Platform(None,'melak',None)
# print(obj.name())
# obj.name('martha')
# print(obj)

# row = ("melak",18,"austin")
# mymap = dict(name='Peter',age=15)
# mymap['name']

# def print_person(name,age,city):
#     print(f'name = {name}, age = {age}, city = {city}')

# print_person(*row)

# nums = dict(one=1,two=2)
# num_values = [*nums.values()]
# x = [1,3]
# print(nums.fromkeys)
