
from src.persistence.persistence import Persistence
from src.app.AppContext import AppContext


class CredentialsDao:

    def __init__(self, app:AppContext) -> None:
        self.persist = app.persistence()

    def find_by_host_id(self, host_id):
        return self.persist.find_by_field_in_table('Credentials', 'host_id', host_id)

    def find_all_by_critical_pwd(self):
        pass
