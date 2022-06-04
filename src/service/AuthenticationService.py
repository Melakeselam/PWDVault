from src.service.UserService import UserService as UserService
from src.app.AppContext import AppContext

class AuthenticationService:
    
    def __init__(self, app:AppContext) -> None:
        self.user_service = UserService(app)

    def authenticate(self, username_password):
        try:
            user = self.user_service.get_user_to_authenticate_by_username(username_password['username'])
        except Exception as e:
            print(f'Exception thrown: {e}')
        if user is None:
            return -1
        elif user.authenticate(username_password['password']) is False:
            return -2
        else: return user.id()

