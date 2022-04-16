from domain.User import User
from service.dtos.UserDto import UserDto

class UserDtoAdaptor:
    def __init__(self) -> None:
        pass

    def model_to_info_dto(user) -> UserDto:
        return UserDto(
            user.id(), 
            user.first_name(), 
            user.last_name(),
            user.username()
            )

    def model_to_auth_dto(user) -> UserDto:
        return UserDto(
            user.id(),
            user.username(),
            user.password(),
            user.sq_1(),
            user.sq_ans_1(),
            user.sq_2(),
            user.sq_ans_2(),
            user.sq_3(),
            user.sq_ans_3()

            )
    
    def dto_to_model(user_dto) -> User:
        return User(
            user_dto.id(),
            user_dto.first_name(), 
            user_dto.last_name(),
            user_dto.username(),
            user_dto.password(),
            user_dto.sq_1(),
            user_dto.sq_ans_1(),
            user_dto.sq_2(),
            user_dto.sq_ans_2(),
            user_dto.sq_3(),
            user_dto.sq_ans_3()
            )