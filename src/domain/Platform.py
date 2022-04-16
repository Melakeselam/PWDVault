from utils.DomainUtils import DomainUtils
from multipledispatch import dispatch 

class Platform:
    def __init__(self, id, name, description=None):
        if name is None:
            raise Exception("The 'name' must have value.")
        self._id = id
        self._name = name
        self._description = description

    def __str__(self) -> str:
        to_string = f"Platform[id:{self._id},name:\'{self._name}\',description:\'{self._description}\']"
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

    
