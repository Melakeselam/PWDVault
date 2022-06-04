from src.utils.DomainUtils import DomainUtils

class User:
    def __init__(self,user_id, 
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


    def __str__(self) -> str:
        to_string = f"User[id:{self._id},first_name:\'{self._first_name}\',last_name:\'{self._last_name}\',username:\'{self._username}\',password:\'{self._password}\',sq_1:\'{self._sq_1}\',sq_ans_1:\'{self._sq_ans_1}\',sq_2:\'{self._sq_2}\',sq_ans_2:\'{self._sq_ans_2}\',sq_3:\'{self._sq_3}\',sq_ans_3:\'{self._sq_ans_3}\']"
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
        return [self._sq_1,self._sq_2,self._sq_3]

    def validate_sequrity_questions(self, answers):
        return answers[self._sq_1] == self._sq_ans_1\
        and answers[self._sq_2] == self._sq_ans_2\
        and answers[self._sq_3] == self._sq_ans_3

    def authenticate(self, password):
        return self._password == password

    