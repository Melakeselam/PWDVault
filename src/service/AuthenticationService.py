from service.UserService import UserService as UserService



class AuthenticationService:
    user_service = UserService()
    def __init__(self) -> None:
        pass

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

