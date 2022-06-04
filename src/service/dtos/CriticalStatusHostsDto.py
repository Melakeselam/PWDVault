# expiration severity periods
# 10 days to expire -> yellow status
# 3 days to expire -> red status
# expired -> grey stats

from multipledispatch import dispatch

class CriticalPwdStatusHostsDto:
    _expired:list
    _3_days_to_expire:list
    _10_days_to_expire:list

    def __init__(self,grey_hosts:list =[], red_hosts:list =[], yellow_hosts:list =[]) -> None:
        self._expired = grey_hosts
        self._3_days_to_expire = red_hosts
        self._10_days_to_expire = yellow_hosts

    def grey_status_hosts(self):
        return self._expired

    def red_status_hosts(self):
        return self._3_days_to_expire
    
    def yellow_stats_hosts(self):
        return self._10_days_to_expire
