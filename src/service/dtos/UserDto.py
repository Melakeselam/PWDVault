from multipledispatch import dispatch
from utils.DomainUtils import DomainUtils


class UserDto:
    @dispatch(str, str)
    def __init__(self, username, password) -> None:
        self._id = -1,
        self._first_name = None,
        self._last_name = None,
        self._username = username,
        self._password = password,
        self._sq_1 = None,
        self._sq_ans_1 = None,
        self._sq_2 = None,
        self._sq_ans_2 = None,
        self._sq_3 = None,
        self._sq_ans_3 = None
    
    @dispatch(int, str, str, str)
    def __init__(self, id, first_name, last_name, username) -> None:
        self._id = id,
        self._first_name = first_name,
        self._last_name = last_name,
        self._username = username,
        self._password = None,
        self._sq_1 = None,
        self._sq_ans_1 = None,
        self._sq_2 = None,
        self._sq_ans_2 = None,
        self._sq_3 = None,
        self._sq_ans_3 = None

    @dispatch(int, str, str, str, str, str, str, str, str)
    def __init__(self, user_id,
                 username,
                 password,
                 # sq: security questions
                 sq_1,
                 sq_ans_1,
                 sq_2,
                 sq_ans_2,
                 sq_3,
                 sq_ans_3
                 ) -> None:
        self._id = user_id
        self._first_name = None
        self._last_name = None
        self._username = username
        self._password = password
        self._sq_1 = sq_1
        self._sq_ans_1 = sq_ans_1
        self._sq_2 = sq_2
        self._sq_ans_2 = sq_ans_2
        self._sq_3 = sq_3
        self._sq_ans_3 = sq_ans_3
    
    @dispatch(int, str, str, str, str, str, str, str, str, str, str)
    def __init__(self, user_id,
                 first_name,
                 last_name,
                 username,
                 password,
                 # sq: security questions
                 sq_1,
                 sq_ans_1,
                 sq_2,
                 sq_ans_2,
                 sq_3,
                 sq_ans_3
                 ) -> None:
        self._id = user_id
        self._first_name = first_name
        self._last_name = last_name
        self._username = username
        self._password = password
        self._sq_1 = sq_1
        self._sq_ans_1 = sq_ans_1
        self._sq_2 = sq_2
        self._sq_ans_2 = sq_ans_2
        self._sq_3 = sq_3
        self._sq_ans_3 = sq_ans_3

    @dispatch(int, str, str, str, str, str, str, str, str)
    def __init__(self, user_id,
                 username,
                 password,
                 # sq: security questions
                 sq_1,
                 sq_ans_1,
                 sq_2,
                 sq_ans_2,
                 sq_3,
                 sq_ans_3
                 ) -> None:
        self._id = user_id
        self._first_name = None
        self._last_name = None
        self._username = username
        self._password = password
        self._sq_1 = sq_1
        self._sq_ans_1 = sq_ans_1
        self._sq_2 = sq_2
        self._sq_ans_2 = sq_ans_2
        self._sq_3 = sq_3
        self._sq_ans_3 = sq_ans_3

    def __str__(self) -> str:
        to_string = f"UserDto[id:{self._id},first_name:\'{self._first_name}\',last_name:\'{self._last_name}\',username:\'{self._username}\',password:\'{self._password}\',sq_1:\'{self._sq_1}\',sq_ans_1:\'{self._sq_ans_1}\',sq_2:\'{self._sq_2}\',sq_ans_2:\'{self._sq_ans_2}\',sq_3:\'{self._sq_3}\',sq_ans_3:\'{self._sq_ans_3}\']"
        return DomainUtils.correct_obj_str_format(to_string)

    def id(self):
        return self._id

    def first_name(self):
        return self._first_name

    def last_name(self):
        return self._last_name

    def username(self):
        return self._username

    def password(self):
        return self._password

    def sq_1(self):
        return self._sq_1

    def sq_ans_1(self):
        return self._sq_ans_1
    
    def sq_2(self):
        return self._sq_2

    def sq_ans_2(self):
        return self._sq_ans_2
    
    def sq_3(self):
        return self._sq_3

    def sq_ans_3(self):
        return self._sq_ans_3

    def get_security_questions(self):
        return [self._sq_1, self._sq_2, self._sq_3]

    def authenticate(self, password):
        return self._password == password