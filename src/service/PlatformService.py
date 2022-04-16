import imp
from repository.PlatformRepository import PlatformRepository as Repository
from domain.Platform import Platform
from service.dtos.PlatformDto import PlatformDto
from service.adaptors.PlatformDtoAdaptor import PlatformDtoAdaptor as Adaptor



class PlatformService:
    platform_repo = Repository()

    def __init__(self) -> None:
        pass

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

    def get_all_by_ids(self,ids:list):
        platforms = self.platform_repo.get_all_by_ids(ids)
        platform_dtos = [Adaptor.model_to_dto(platform) for platform in platforms]
        return platform_dtos


