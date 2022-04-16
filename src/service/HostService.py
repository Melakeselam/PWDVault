
from tkinter import DOTBOX
from domain.Host import Host
from repository.HostRepository import HostRepository
from service.adaptors.HostDtoAdaptor import HostDtoAdaptor as Adaptor


class HostService:
    def __init__(self,user_id) -> None:
        self.user_id = user_id
        self.repo = HostRepository(user_id)

    def get_all_by_platform_id(self, platform_id):
        try:
            hosts = self.repo.get_all_by_platform_id(platform_id)
            host_dtos_map = {}
            for host in hosts:
                host_dtos_map[host.id()] = Adaptor.model_to_credentials_dto(host)

            return host_dtos_map
        except Exception as e:
            print(f'Exception: {e}')
    
    def get_all_by_category_id(self, platform_id,category_name):
        try:
            hosts = self.repo.get_all_by_category_id(platform_id,category_name)
            host_dtos_map = {}
            for host in hosts:
                host_dtos_map[host.id()] = Adaptor.model_to_credentials_dto(host)

            return host_dtos_map
        except Exception as e:
            print(f'Exception: {e}')

    def get_all(self):
        try:
            hosts = self.repo.get_all()
            host_dtos =[Adaptor.model_to_credentials_dto(host)for host in hosts]
            return host_dtos
        except Exception as e:
            print(f'Exception: {e}')
