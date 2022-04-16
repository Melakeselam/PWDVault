from service.dtos.UserDto import UserDto
from utils.UiUtils import UiUtils
from ui.Menus import Menus
from service.AuthenticationService import AuthenticationService as AuthService
from service.UserService import UserService

class LoginMenu:

    user_service = UserService()

    def __init__(self) -> None:
        self.auth_service = AuthService()

    def exec_login_menu(self):
        user_id = -1
        while user_id == -1:
            UiUtils.clear()
            menu_choice = UiUtils.disp_and_select_from_menu(Menus.login_menu)
            user_id = self.exec_login_menu_choice(int(menu_choice))
        return user_id

    def exec_login_menu_choice(self, choice):
        if choice == 1:
            return self.login()
        elif choice == 2:
            return self.create_user()
        elif choice == 3:
            return 0
        else:
            input("This menu choice is not available!")
        return -1

    def login(self):
        UiUtils.clear()
        request = dict(title = 'LOGIN',username = 'Enter Username: ',password='Enter Password: ')
        username_password = UiUtils.request_input(request)
        user_id = self.auth_service.authenticate(username_password)
        if user_id == -1:
            input('Username does not exit.')
            user_id = False
        elif user_id == -2:
            input('Provided credentials failed authentication.')
            user_id = False
        return user_id

    def create_user(self):
        UiUtils.clear()
        request_user_info = dict(title = 'CREATE USER',
            first_name = "First Name: ",
            last_name = "Last Name: ",
            username = 'Username: ',
            password='Password: '
            )
        user_info = UiUtils.request_input(request_user_info)
        UiUtils.clear()
        request_security_question = dict(title = 'SECURITY QUESTIONS AND ANSWERS',
            sq_1 = "Provide Security Question 1: ",
            sq_ans_1 = "Security Question 1 Answer: ",
            sq_2 = "Provide Security Question 2: ",
            sq_ans_2 = "Security Question 2 Answer: ",
            sq_3 = "Provide Security Question 3: ",
            sq_ans_3 = "Security Question 3 Answer: "
        )
        security_info = UiUtils.request_input(request_security_question)
        user_id = self.user_service.add_user(self.combine_user_info(
            user_info, security_info
        ))
        return user_id

    
    def combine_user_info(self, ui, sq):
        
        return UserDto(
            -1, ui['first_name'], ui['last_name'], 
            ui['username'], ui['password'], 
            sq['sq_1'], sq['sq_ans_1'],
            sq['sq_2'], sq['sq_ans_2'],
            sq['sq_3'], sq['sq_ans_3']
        )

