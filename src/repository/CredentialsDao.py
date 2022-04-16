
from persistence.persistence import Persistence


class CredentialsDao:
    persist = Persistence()

    def __init__(self) -> None:
        pass

    def find_by_host_id(self, host_id):
        return self.persist.find_by_field_in_table('Credentials', 'host_id', host_id)
