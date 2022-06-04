
from tkinter import DOTBOX
from src.service.dtos.CategoryDto import CategoryDto
from src.service.CategoryService import CategoryService
from src.service.dtos.HostDto import HostDto
from src.domain.Host import Host
from src.repository.HostRepository import HostRepository
from src.service.adaptors.HostDtoAdaptor import HostDtoAdaptor as Adaptor
from src.service.dtos.CriticalStatusHostsDto import CriticalPwdStatusHostsDto
from src.domain.Credentials import PwdStatus
from src.app.AppContext import AppContext


class HostService:
    def __init__(self, app:AppContext, user_id) -> None:
        self._user_id = user_id
        self._repo = HostRepository(app, user_id)
        self.category_service = CategoryService(app)

    def get_all_by_platform_id(self, platform_id):
        try:
            hosts = self._repo.get_all_by_platform_id(platform_id)
            host_dtos_map = {}
            for host in hosts:
                host_dtos_map[host.id()] = Adaptor.model_to_credentials_dto(
                    host)

            return host_dtos_map
        except Exception as e:
            print(f'Exception: {e}')

    def get_all_by_category_id(self, platform_id, category_name):
        try:
            hosts = self._repo.get_all_by_category_id(
                platform_id, category_name)
            host_dtos_map = {}
            for host in hosts:
                host_dtos_map[host.id()] = Adaptor.model_to_credentials_dto(
                    host)

            return host_dtos_map
        except Exception as e:
            print(f'Exception: {e}')

    def get_by_id(self, id) -> HostDto:
        try:
            host = self._repo.get_by_id(id)
            return Adaptor.model_to_credentials_dto(host)
        except Exception as e:
            print(f'Exception: {e}')

    def get_all_for_credentials(self):
        try:
            hosts = self._repo.get_all()
            host_dtos = [Adaptor.model_to_credentials_dto(
                host)for host in hosts]
            return host_dtos
        except Exception as e:
            print(f'Exception: {e}')

    def get_hosts_with_critical_pwd_grouped_by_severity(self) -> CriticalPwdStatusHostsDto:
        hosts:list[Host] = self._repo.get_hosts_with_critical_pwd()
        grey_hosts_bucket = []
        red_hosts_bucket = []
        yellow_hosts_bucket = []
        for host in hosts:
            if host.credentials().is_status(PwdStatus.GREY_EXPIRED):
                grey_hosts_bucket.append(Adaptor.model_to_credentials_dto(host))
            elif host.credentials().is_status(PwdStatus.RED_EXPIRES_IN_3_DAYS):
                red_hosts_bucket.append(Adaptor.model_to_credentials_dto(host))
            elif host.credentials().is_status(PwdStatus.YELLOW_EXPIRES_IN_10_DAYS):
                yellow_hosts_bucket.append(Adaptor.model_to_credentials_dto(host))
        return CriticalPwdStatusHostsDto(grey_hosts=grey_hosts_bucket,
                                         red_hosts=red_hosts_bucket,
                                         yellow_hosts=yellow_hosts_bucket)

    def retrieve_pwd_retention_period(self,host_id):
        host = self.get_by_id(host_id)
        retention_period = host.custom_pwd_retention_period_in_hours()
        if not retention_period:
            category:CategoryDto = self.category_service.get_by_id()
            retention_period = category.password_retention_period()
        return retention_period
