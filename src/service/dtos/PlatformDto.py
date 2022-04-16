from utils.DomainUtils import DomainUtils
from multipledispatch import dispatch


class PlatformDto:
    def __init__(self, id, name=None, description=None) -> None:
        self._id = id
        self._name = name
        self._description = description
    
    # def __init__(self, name, description) -> None:
    #     self._id = None
    #     self._name = name
    #     self._description = description

    # def __init__(self) -> None:
    #     pass

    def __str__(self) -> str:
        to_string = f"PlatformDto[id:{self._id},name:\'{self._name}\',description:\'{self._description}\']"
        return DomainUtils.correct_obj_str_format(to_string)

    def id(self):
        return self._id

    @dispatch()
    def name(self):
        return self._name

    @dispatch()
    def description(self):
        return self._description

    @dispatch(str)
    def name(self, name):
        self._name = name

    @dispatch(str)
    def description(self, description):
        self._description = description

    def values(self):
        return [self._id,self._name,self._description]
