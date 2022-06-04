
import datetime
from unittest import TestCase, mock
from src.service.dtos.CriticalStatusHostsDto import CriticalPwdStatusHostsDto
from src.repository.HostRepository import HostRepository
from src.domain.Credentials import Credentials, PwdStatus
from src.domain.Host import Host
from src.domain.Credentials import PasswordPattern
from src.app.AppContext import AppContext


class HostRepositoryTest(TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.maxDiff = None
        self._user_id = 1
        self.host_repo = HostRepository(AppContext(), self._user_id)

    def build_critical_pwd_host_dao_response(user_id: int, grey: int = 0, red: int = 0, yellow: int = 0):
        grey_hosts = [Host(user_id, 100 + i, f'Grey{i+1}', 1, 'test', Credentials(100 + i, f'Grey{i+1}', f'Pass{100 + i}',
                           30, PwdStatus.GREY_EXPIRED) if not credentials else credentials, f'www.grey{i+1}.com') for i in range(grey)]
        red_hosts = [Host(user_id, 100 + i, f'Red{i+1}', 1, 'test', Credentials(200 + i, f'Red{i+1}', f'Pass{200 + i}', 30,
                          PwdStatus.RED_EXPIRES_IN_3_DAYS) if not credentials else credentials, f'www.red{i+1}.com') for i in range(red)]
        yellow_hosts = [Host(user_id, 100 + i, f'Yellow{i+1}', 1, 'test', Credentials(300 + i, f'Yellow{i+1}', f'Pass{300 + i}', 30,
                             PwdStatus.YELLOW_EXPIRES_IN_10_DAYS if not credentials else credentials), f'www.yellow{i+1}.com') for i in range(yellow)]
        return grey_hosts + red_hosts + yellow_hosts

    def build_credentials_from_tuple(credentials_row: tuple):
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
        return credentials

    def build_critical_pwd_host_repo_response(user_id=1, grey: int = 0, red: int = 0, yellow: int = 0) -> CriticalPwdStatusHostsDto:

        grey_hosts = [Host(user_id, 100 + i, f'Grey{i+1}', 1, 'test',
                           Credentials(
                               100 + i, f'Grey{i+1}', f'Pass{100 + i}', 30, PwdStatus.GREY_EXPIRED),
                           f'www.grey{i+1}.com')
                      for i in range(grey)]
        red_hosts = [Host(user_id, 100 + i, f'Red{i+1}', 1, 'test',
                          Credentials(
                              200 + i, f'Red{i+1}', f'Pass{200 + i}', 30, PwdStatus.RED_EXPIRES_IN_3_DAYS),
                          f'www.red{i+1}.com')
                     for i in range(red)]
        yellow_hosts = [Host(user_id, 100 + i, f'Yellow{i+1}', 1, 'test',
                             Credentials(
                                 300 + i, f'Yellow{i+1}', f'Pass{300 + i}', 30, PwdStatus.YELLOW_EXPIRES_IN_10_DAYS),
                             f'www.yellow{i+1}.com')
                        for i in range(yellow)]
        hosts = grey_hosts + red_hosts + yellow_hosts
        return hosts[0] if len(hosts) == 1 else hosts

    def build_host_from_tuples(credentials_row: tuple, host_row: tuple):
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

    def convert_to_str_list(self, obj_list):
        return [str(obj) for obj in obj_list] if obj_list else []

    def build_credentials_tuples(fields: dict = dict(), count=1):
        keys = fields.keys()
        pwd_pattern = PasswordPattern()
        return [(
            fields['host_id'] if 'host_id' in keys else 123 + i,
            fields['username'] if 'username' in keys else 'test' + str(i),
            fields['password'] if 'password' in keys else '12345' + str(i),
            fields['date_created'] if 'date_created' in keys else datetime.datetime(
                1956, 1, 31),
            fields['pwd_updated_date'] if 'pwd_updated_date' in keys else datetime.datetime(
                1956, 1, 31),
            fields['pwd_expiration_date'] if 'pwd_expiration_date' in keys else datetime.datetime(
                1956, 3, 2),
            fields['pwd_size'] if 'pwd_size' in keys else pwd_pattern.pwd_size(),
            fields['pwd_min_num_req'] if 'pwd_min_num_req' in keys else pwd_pattern.pwd_min_num_req(),
            fields['pwd_min_upper_req'] if 'pwd_min_upper_req' in keys else pwd_pattern.pwd_min_upper_req(),
            fields['pwd_min_special_req'] if 'pwd_min_special_req' in keys else pwd_pattern.pwd_min_special_req(),
            fields['pwd_special_req'] if 'pwd_special_req' in keys else pwd_pattern.pwd_special_req(),
            fields['status'] if 'status' in keys else PwdStatus.CREATED.name,
        ) for i in range(count)]

    def build_host_tuple(fields: dict = dict()):
        keys = fields.keys()
        return (
            fields['user_id'] if 'user_id' in keys else 123,
            fields['host_id'] if 'host_id' in keys else 123,
            fields['host_name'] if 'host_name' in keys else 'test_host',
            fields['platform_id'] if 'platform_id' in keys else 123,
            fields['category_name'] if 'category_name' in keys else 'test_catagory',
            fields['address'] if 'address' in keys else 'test_address',
            fields['custom_pwd_retention_period_in_hours'] if 'custom_pwd_retention_period_in_hours' in keys else 30*24,
        )

    def hosts_1():
        credentials_rows = HostRepositoryTest.build_credentials_tuples()
        host_row = HostRepositoryTest.build_host_tuple()
        one_host = HostRepositoryTest.build_host_from_tuples(
            credentials_rows[0], host_row)
        return [one_host]

    def hosts_2():
        credentials_rows = HostRepositoryTest.build_credentials_tuples(count=2)
        host_row = HostRepositoryTest.build_host_tuple()
        host1 = HostRepositoryTest.build_host_from_tuples(
            credentials_rows[0], host_row)
        host2 = HostRepositoryTest.build_host_from_tuples(
            credentials_rows[1], host_row)
        return [host1, host2]

    def test_generate_hosts_by_retrieving_for_critical_pwds_should_return_empty_host_list(self):
        credentials_rows = []
        expected_return_value = []
        actual_return_value = self.host_repo.generate_hosts_from_retrieved_credentials_for_critical_pwd_rows(
            credentials_rows)
        self.assertListEqual(expected_return_value, actual_return_value)

    @mock.patch("src.repository.HostRepository.HostRepository.get_by_credentials_row", return_value=build_host_from_tuples(build_credentials_tuples()[0], build_host_tuple()))
    def test_generate_hosts_by_retrieving_for_critical_pwds_should_return_one_host(self, *mock_output):

        credentials_rows = HostRepositoryTest.build_credentials_tuples()
        expected_return_value = HostRepositoryTest.hosts_1()
        actual_return_value = self.host_repo.generate_hosts_from_retrieved_credentials_for_critical_pwd_rows(
            credentials_rows)

        self.assertListEqual(self.convert_to_str_list(
            expected_return_value), self.convert_to_str_list(actual_return_value))

    @mock.patch("src.repository.HostRepository.HostRepository.get_by_credentials_row", side_effect=[
        build_host_from_tuples(build_credentials_tuples(count=2)[0], build_host_tuple()),
        build_host_from_tuples(build_credentials_tuples(count=2)[1], build_host_tuple()),
        ])
    def test_generate_hosts_by_retrieving_for_critical_pwds_should_return_two_hosts(self, *mock_output):

        credentials_rows = HostRepositoryTest.build_credentials_tuples(count=2)
        expected_return_value = HostRepositoryTest.hosts_2()
        actual_return_value = self.host_repo.generate_hosts_from_retrieved_credentials_for_critical_pwd_rows(
            credentials_rows)

        self.assertListEqual(self.convert_to_str_list(
            expected_return_value), self.convert_to_str_list(actual_return_value))

    # @mock.patch("repository.HostRepository.CredentialsDao.find_all_by_critical_pwd", return_value=[])
    # @mock.patch("repository.HostRepository.HostRepository.generate_hosts_from_retrieved_for_critical_pwd_rows", return_value=[])
    # def test_should_return_empty_host_with_critical_pwd(self, *mock_output):
    #     expected_return_value = []
    #     actual_return_value = self.host_repo.get_hosts_with_critical_pwd()
    #     self.assertListEqual(self.convert_to_str_list(
    #         expected_return_value), self.convert_to_str_list(actual_return_value))

    # @mock.patch('repository.HostRepository.CredentialsDao.find_all_by_critical_pwd',return_value=[])
    # def test_should_return_one_host_with_critical_pwd(self,mock_check_output):

    #     expected_return_value = self.build_critical_pwd_host_repo_response(grey=1)
    #     actual_return_value = self.host_repo.get_hosts_with_critical_pwd()
    #     self.assertListEqual(self.convert_to_str_list(expected_return_value), self.convert_to_str_list(actual_return_value))
