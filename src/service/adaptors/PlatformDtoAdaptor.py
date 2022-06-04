from src.domain.Platform import Platform
from src.service.dtos.PlatformDto import PlatformDto

class PlatformDtoAdaptor:
    def __init__(self) -> None:
        pass

    def model_to_dto(platform) -> PlatformDto:
        return PlatformDto(platform.id(), platform.name(), platform.description())
    
    def dto_to_model(platform_dto) -> Platform:
        return Platform(platform_dto.id(), platform_dto.name(), platform_dto.description())