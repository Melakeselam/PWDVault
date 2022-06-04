from src.repository.UserRepository import UserRepository
from src.service.adaptors.UserDtoAdaptor import UserDtoAdaptor as Adaptor
from src.app.AppContext import AppContext
class UserService:

    def __init__(self,app:AppContext) -> None:
        self.repo = UserRepository(app)

    def add_user(self, user_dto):
        try:
            return self.repo.add_user(Adaptor.dto_to_model(user_dto))
        except Exception as e:
            input(e)
    
    def get_user_to_authenticate_by_username(self, username):
        return Adaptor.model_to_auth_dto(self.repo.get_by_username(username))