class DomainUtils:

    def __init__(self) -> None:
        pass

    def correct_obj_str_format(objectString) -> str:
        objectString = str(objectString)
        return objectString.replace('[', '{').replace(']', '}').replace(':', ': ').replace(',', ', ')
