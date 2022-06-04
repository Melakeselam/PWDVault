# from pathlib import Path
import unittest
from unittest import mock
from src.app.AppContext import AppContext
from src.service.dtos.HostDto import HostDto
from src.domain.Host import Host

from src.service.HostService import HostService
from src.service.dtos.CriticalStatusHostsDto import CriticalPwdStatusHostsDto
from src.domain.Credentials import Credentials,PwdStatus


class Test_HostService(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self._user_id = 1
        self.host_service = HostService(AppContext(),self._user_id)
    
    def build_critical_pwd_host_repo_response(user_id:int,grey:int=0,red:int=0,yellow:int=0) -> list:
        grey_hosts =[Host(user_id,100 + i,f'Grey{i+1}',1,'test',Credentials(100 + i,f'Grey{i+1}', f'Pass{100 + i}',30,PwdStatus.GREY_EXPIRED),f'www.grey{i+1}.com') for i in range(grey)]
        red_hosts =[Host(user_id,100 + i,f'Red{i+1}',1,'test',Credentials(200 + i,f'Red{i+1}', f'Pass{200 + i}',30,PwdStatus.RED_EXPIRES_IN_3_DAYS),f'www.red{i+1}.com') for i in range(red)]
        yellow_hosts =[Host(user_id,100 + i,f'Yellow{i+1}',1,'test',Credentials(300 + i,f'Yellow{i+1}', f'Pass{300 + i}',30,PwdStatus.YELLOW_EXPIRES_IN_10_DAYS),f'www.yellow{i+1}.com') for i in range(yellow)]
        return grey_hosts + red_hosts + yellow_hosts

    @mock.patch('src.service.HostService.HostRepository.get_hosts_with_critical_pwd',return_value=build_critical_pwd_host_repo_response(1))
    def test_should_return_empty_hosts_dto_with_critical_pwd(self,mock_check_output):
        expected_return_value = CriticalPwdStatusHostsDto()
        actual_return_value = self.host_service.get_hosts_with_critical_pwd_grouped_by_severity()
        self.assert_expected_is_actual(expected_return_value, actual_return_value)    
    
    @mock.patch('src.service.HostService.HostRepository.get_hosts_with_critical_pwd',return_value=build_critical_pwd_host_repo_response(user_id=1,grey=1))
    def test_should_return_hosts_dto_with_one_expired_pwd(self,mock_check_output):
        expected_return_value = CriticalPwdStatusHostsDto(grey_hosts=[HostDto(100,Credentials(100,'Grey1', 'Pass100',30,PwdStatus.GREY_EXPIRED))])
        actual_return_value = self.host_service.get_hosts_with_critical_pwd_grouped_by_severity()
        self.assert_expected_is_actual(expected_return_value, actual_return_value)

    @mock.patch('src.service.HostService.HostRepository.get_hosts_with_critical_pwd',return_value=build_critical_pwd_host_repo_response(user_id=1,red=1))
    def test_should_return_hosts_dto_with_one_pwd_with_3_days_to_expire(self,mock_check_output):
        expected_return_value = CriticalPwdStatusHostsDto(red_hosts=[HostDto(200,Credentials(200,'Red1', 'Pass200',30,PwdStatus.RED_EXPIRES_IN_3_DAYS))])
        actual_return_value = self.host_service.get_hosts_with_critical_pwd_grouped_by_severity()
        self.assert_expected_is_actual(expected_return_value, actual_return_value)

    @mock.patch('src.service.HostService.HostRepository.get_hosts_with_critical_pwd',return_value=build_critical_pwd_host_repo_response(user_id=1,yellow=1))
    def test_should_return_hosts_dto_with_one_pwd_with_10_days_to_expire(self,mock_check_output):
        expected_return_value = CriticalPwdStatusHostsDto(yellow_hosts=[HostDto(300,Credentials(300,'Yellow1', 'Pass300',30,PwdStatus.YELLOW_EXPIRES_IN_10_DAYS))])
        actual_return_value = self.host_service.get_hosts_with_critical_pwd_grouped_by_severity()
        self.assert_expected_is_actual(expected_return_value, actual_return_value)

    @mock.patch('src.service.HostService.HostRepository.get_hosts_with_critical_pwd',return_value=build_critical_pwd_host_repo_response(user_id=1,yellow=2,red=3,grey=1))
    def test_should_return_hosts_dto_with_multiple_pwds_of_each_status_type(self,mock_check_output):
        expected_return_value = CriticalPwdStatusHostsDto(
            yellow_hosts=[HostDto(300,Credentials(300,'Yellow1', 'Pass300',30,PwdStatus.YELLOW_EXPIRES_IN_10_DAYS)),
            HostDto(301,Credentials(301,'Yellow2', 'Pass301',30,PwdStatus.YELLOW_EXPIRES_IN_10_DAYS))],
            red_hosts=[HostDto(200,Credentials(200,'Red1', 'Pass200',30,PwdStatus.RED_EXPIRES_IN_3_DAYS)),
                HostDto(201,Credentials(201,'Red2', 'Pass201',30,PwdStatus.RED_EXPIRES_IN_3_DAYS)),
                HostDto(202,Credentials(202,'Red3', 'Pass202',30,PwdStatus.RED_EXPIRES_IN_3_DAYS))],
            grey_hosts=[HostDto(100,Credentials(100,'Grey1', 'Pass100',30,PwdStatus.GREY_EXPIRED))]
            )
        actual_return_value = self.host_service.get_hosts_with_critical_pwd_grouped_by_severity()
        self.assert_expected_is_actual(expected_return_value, actual_return_value)
        
    def assert_expected_is_actual(self,expected_return_value:CriticalPwdStatusHostsDto, actual_return_value:CriticalPwdStatusHostsDto):
        self.assertIsNotNone(actual_return_value,"method should return a none 'None' object")
        self.assertEqual(type(expected_return_value),type(actual_return_value))
        self.assertEqual(len(expected_return_value.grey_status_hosts()),len(actual_return_value.grey_status_hosts()),  "method should return dto with hosts that have expired passwords.")
        self.assertEqual(len(expected_return_value.red_status_hosts()),len(actual_return_value.red_status_hosts()), "method should return dto with hosts that have passwords expiring within 3 days.")
        self.assertEqual(len(expected_return_value.yellow_stats_hosts()),len(actual_return_value.yellow_stats_hosts()), "method should return dto with hosts that have passwords expiring btn 3 and 10 days.")

if __name__ == '__main__':
    unittest.main()