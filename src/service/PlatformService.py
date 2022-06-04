import imp
from src.repository.PlatformRepository import PlatformRepository as Repository
from src.domain.Platform import Platform
from src.service.dtos.PlatformDto import PlatformDto
from src.service.adaptors.PlatformDtoAdaptor import PlatformDtoAdaptor as Adaptor
from src.app.AppContext import AppContext



class PlatformService:
    
    def __init__(self, app:AppContext) -> None:
        self.platform_repo = Repository(app)

    def add_platform(self, platform_dto):
        self.platform_repo.save(Adaptor.dto_to_model(platform_dto))

    def update_platform(self,platform_dto):
        self.platform_repo.save(Adaptor.dto_to_model(platform_dto))

    def remove_platform(self, id):
        self.platform_repo.delete_by_id(id)

    def get_all(self):
        platforms = self.platform_repo.get_all()
        platform_dtos = [Adaptor.model_to_dto(platform) for platform in platforms]
        return platform_dtos

    def get_by_id(self,id:int) -> PlatformDto:
        platform = self.platform_repo.get_by_id(id)
        return Adaptor.model_to_dto(platform) if platform else None

    def get_all_by_ids(self,ids:list):
        platforms = self.platform_repo.get_all_by_ids(ids)
        platform_dtos = [Adaptor.model_to_dto(platform) for platform in platforms]
        return platform_dtos


