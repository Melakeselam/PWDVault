
from operator import eq
from src.domain.Credentials import Credentials, PasswordPattern, PwdStatus
from src.domain.Host import Host
from src.exceptions.exceptions import MissingDataFromRepositoryError
from src.repository.CredentialsDao import CredentialsDao
from src.repository.HostDao import HostDao
import logging

from src.config.logger_config import Log
from src.app.AppContext import AppContext


class HostRepository:

    def __init__(self, app: AppContext, user_id) -> None:
        self.user_id = user_id
        self.host_dao = HostDao(app, user_id)
        self.credentials_dao = CredentialsDao(app)
        self.log: logging.Logger = app.logger()

    def get_all(self) -> list[Host]:
        host_rows = self.host_dao.get_all()
        return [self.generate_host_with_retrieved_host_raw_and_optionally_credentials_row(host_row) for host_row in host_rows]

    def get_all_by_platform_id(self, platform_id) -> list[Host]:
        host_rows = self.host_dao.find_all_by_platform_id(platform_id)
        return [self.generate_host_with_retrieved_host_raw_and_optionally_credentials_row(host_rows) for host_row in host_rows]

    def get_all_by_category_id(self, platform_id: int, category_name: str) -> list[Host]:
        host_rows = self.host_dao.find_all_by_category_id(
            platform_id, category_name)
        return [self.generate_host_with_retrieved_host_raw_and_optionally_credentials_row(host_rows) for host_row in host_rows]

    def get_by_id(self, id: int) -> Host:
        host_row: list[tuple] = self.host_dao.find_by_id(id)
        if len(host_row) == 0:
            return None
        try:
            host = self.generate_host_with_retrieved_host_raw_and_optionally_credentials_row(
                host_row)
            return host if host else None
        except Exception as e:
            print(f'Exception: {e}')

    def get_by_credentials_row(self, credentials_row: tuple[Credentials] = None) -> Host:
        id = credentials_row[0]  # host_id is the first element in the tuple
        host_row: list[tuple] = self.host_dao.find_by_id(id)
        if len(host_row) != 1:
            raise MissingDataFromRepositoryError(
                f"Host for host id: {id} doesn't exist or is more than expected (1) in db. Invalid credentials provided.")
        try:
            host = self.generate_host_with_retrieved_host_raw_and_optionally_credentials_row(
                host_row, credentials_row)[0]
            return host if host else None
        except Exception as e:
            print(f'Exception: {e}')

    def get_hosts_with_critical_pwd(self) -> list[Host]:
        critical_pwd_credentials_rows = self.credentials_dao.find_all_by_critical_pwd()
        return self.generate_hosts_from_retrieved_credentials_for_critical_pwd_rows(critical_pwd_credentials_rows)

    def generate_host_with_retrieved_host_raw_and_optionally_credentials_row(self, host_row: tuple, credentials_row: tuple = None) -> Host:
        host_id = host_row[1]  # host_id is the second element in the tuple
        found_credentials_rows = self.credentials_dao.find_by_host_id(
            host_id) if not credentials_row else [credentials_row]
        if len(found_credentials_rows) != 1:
            raise MissingDataFromRepositoryError(
                f"Credentials for host id: {host_id} doesn't exist or is more than expected (1) in db.")
        else:
            credentials_row = found_credentials_rows[0]

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
            PwdStatus[credentials_row[11]]
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
        return host

    def generate_hosts_from_retrieved_credentials_for_critical_pwd_rows(self, credentials_rows: list[tuple]) -> list[Host]:
        hosts: list[Host] = []
        if credentials_rows == None:
            raise ValueError(
                f"credentials_rows to generate hosts can not be None")
        if len(credentials_rows) > 0:
            self.log.debug(
                f"Retrieving hosts for ids:{[c[0] for c in credentials_rows]}")
            for credentials_row in credentials_rows:
                try:
                    host: Host = self.get_by_credentials_row(credentials_row)
                    hosts.append(host)
                except MissingDataFromRepositoryError as e:
                    self.log.error(e.with_traceback())
        return hosts
