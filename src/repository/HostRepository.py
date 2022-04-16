
from operator import eq
from domain.Credentials import Credentials, PasswordPattern, Status
from domain.Host import Host
from exceptions.exceptions import MissingDataFromRepositoryError
from repository.CredentialsDao import CredentialsDao
from repository.HostDao import HostDao


class HostRepository:

    def __init__(self, user_id) -> None:
        self.user_id = user_id
        self.host_dao = HostDao(user_id)
        self.credentials_dao = CredentialsDao()

    def get_all(self) -> Host:
        host_rows = self.host_dao.get_all()
        return self.extract_hosts_from_rows(host_rows)

    def get_all_by_platform_id(self, platform_id) ->Host:
        host_rows = self.host_dao.find_all_by_platform_id(platform_id)
        return self.extract_hosts_from_rows(host_rows)
    
    def get_all_by_category_id(self, platform_id:int, category_name:str) ->Host:
        host_rows = self.host_dao.find_all_by_category_id(platform_id,category_name)
        return self.extract_hosts_from_rows(host_rows)
    
    def extract_hosts_from_rows(self,host_rows:list) -> list:
        hosts = []
        for host_row in host_rows:
            credentials_rows = self.credentials_dao.find_by_host_id(host_row[1])
            credentials_row = ''
            if len(credentials_rows) != 1 :
                raise MissingDataFromRepositoryError(f'Credentials for host id: {host_row[1]} should exist in db.') 
            else:
                credentials_row = credentials_rows[0]

            credentials = Credentials(
                credentials_row[0],
                credentials_row[1],
                credentials_row[2],
                credentials_row[3],
                credentials_row[4],
                credentials_row[5],
                PasswordPattern(
                    credentials_row[6],
                    credentials_row[7],
                    credentials_row[8],
                    credentials_row[9],
                    credentials_row[10],
                ),
                Status[credentials_row[11]]
                )
            host = Host(host_row[0],
                host_row[1],
                host_row[2],
                host_row[3],
                host_row[4],
                credentials,
                host_row[5],
                host_row[6],
            )
            hosts.append(host)
        return hosts
        
