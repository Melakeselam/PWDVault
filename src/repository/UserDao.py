from src.app.AppContext import AppContext
from src.domain.User import User

class UserDao:
    
    def __init__(self,app:AppContext) -> None:
        self.persist = app.persistence()

    def add_user(self,user:User):
        user_map = dict(
            first_name=user.first_name(),
            last_name=user.last_name(),
            username=user.username(),
            password=user.password(),
            security_question_1=user.sq_1(),
            sq_answer_1=user.sq_ans_1(),
            security_question_2=user.sq_2(),
            sq_answer_2=user.sq_ans_2(),
            security_question_3=user.sq_3(),
            sq_answer_3=user.sq_ans_3()
        )

        id = self.persist.insert_into_table('User',user_map)
        return id

    def get_by_username(self, username):
        return self.persist.find_by_field_in_table('User','username',username)

    