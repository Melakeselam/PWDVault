from src.service.dtos.CriticalStatusHostsDto import CriticalPwdStatusHostsDto
from src.app.AppContext import AppContext


class HostCommandMenu:
    def __init__(self, app:AppContext, user_id:int) -> None:
        self._user_id = user_id

    def exec_update_for_critical_passwords(self, grouped_critical_pwd_hosts:CriticalPwdStatusHostsDto):
        grouped_hosts = self.retrieve_critical_pwd_grouped_by_severity()

    
