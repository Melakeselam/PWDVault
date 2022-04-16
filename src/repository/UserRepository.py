from repository.UserDao import UserDao
from domain.User import User
class UserRepository:
    dao = UserDao()

    def __init__(self) -> None:
        pass

    def add_user(self, user):
        return self.dao.add_user(user)

    def get_by_username(self, username):
        rows = self.dao.get_by_username(username)
        users = []
        for row in rows:
            users.append(User(row[0],row[1],row[2],row[3],row[4],row[5],
                row[6],row[7],row[8],row[9],row[10])
            )
        return users[0]
