from numpy import array
from src.service.CategoryService import CategoryService
from src.service.HostService import HostService
from src.service.PlatformService import PlatformService
from src.service.dtos.HostDto import HostDto
from src.app.AppContext import AppContext
from src.ui.Menus import Menus
from src.ui.main_menu_sub_menus.CategoryMenu import CategoryMenu
from src.utils.UiUtils import UiUtils


class HostQueryMenu:
    def __init__(self, app:AppContext, user_id:int) -> None:
        self._user_id = user_id
        self._hosts = None
        self.platform_service = PlatformService(app)
        self.category_service = CategoryService(app)
        self.service = HostService(app, user_id)

    def exec_query_credentials_menu(self, return_value:bool = False) -> HostDto:
        remain_at_current_menu_level = True
        show_result_on_pause = False if return_value else True
        while remain_at_current_menu_level:
            UiUtils.clear()
            menu_choice = UiUtils.disp_and_select_from_menu(
                Menus.retrieve_credentials_menu)
            retrieved_host = None
            try:
                retrieved_host = self.exec_menu_choice(
                    int(menu_choice), show_result_on_pause)

                if retrieved_host == 'return':
                    remain_at_current_menu_level = False
                    retrieved_host = None
                elif return_value:
                    remain_at_current_menu_level = False
                else:
                    remain_at_current_menu_level = True
            
            except Exception as e:
                remain_at_current_menu_level = True

            
        return retrieved_host
        
    def exec_menu_choice(self, choice:int, show_on_pause:bool):
        retrieved_host = None
        if choice == 1:
            retrieved_host = self.retrieve_by_platform(show_on_pause)
        elif choice == 2:
            retrieved_host = self.retrieve_by_category(show_on_pause)
        elif choice == 3:
            retrieved_host = self.retrieve_by_address(show_on_pause)
        elif choice == 4:
            retrieved_host = self.retrieve_by_host_name(show_on_pause)
        elif choice == 5:
            retrieved_host = self.retrieve_by_host_id(show_on_pause)
        elif choice == 6:
            return 'return'
        else:
            input("This menu choice is not available!")
            raise Exception('Improper Menu Selection')
        return retrieved_host

    def retrieve_by_platform(self,show_on_pause:bool = True) -> HostDto:
        if not self._hosts:
            self._hosts = self.service.get_all_for_credentials()
        self.show_platform_id_and_name_columns_on_pause(False)
        platform_id = int(input('Select Platform Id: '))
        hosts = self.map_host_to_id_filtered_by_platform_id(platform_id)
        if len(hosts):
            self.show_host_info_on_pause(False, hosts.values())
            host_id = int(input('Select Host by id: '))
            selected_host = hosts[host_id]
            self.show_credentials(selected_host,show_on_pause)
            return selected_host
        else:
            print(f'There are no hosts with PLATFORM_ID: {platform_id}')
            input('Press <enter> to continue...')
        return None

    def retrieve_by_category(self,show_on_pause:bool = True) -> HostDto:
        if not self._hosts:
            self._hosts = self.service.get_all_for_credentials()
        id_maps = self.show_category_by_platform_id_and_category_name_columns_on_pause(False)
        id_num = int(input('Select ID_NO: '))
        id_map = id_maps[id_num-1]
        host_map = self.map_host_to_id_filtered_by_category(id_map['platform_id'], id_map['category_name'])
        if len(host_map):
            self.show_host_info_on_pause(False, host_map.values())
            host_id = int(input('Select Host by ID: '))
            selected_host = host_map[host_id]
            self.show_credentials(selected_host,show_on_pause)
            return selected_host
        else:
            input(
                f'There are no hosts with PLATFORM_ID: {id_map["platform_id"]} and CATEGORY_NAME: {id_map["category_name"]}')
        return None

    def retrieve_by_address(self,show_on_pause:bool = True) -> HostDto:
        if not self._hosts:
            self._hosts = self.service.get_all_for_credentials()
        address_maps = self.show_host_address_columns_on_pause(False)
        item_num = int(input('Select ADDR_NO: '))
        address_map = address_maps[item_num-1]
        host_map = self.map_host_to_id_filtered_by_address(address_map['host_address'])
        if len(host_map):
            self.show_host_info_on_pause(False, host_map.values())
            host_id = int(input('Select Host by ID: '))
            selected_host = host_map[host_id]
            self.show_credentials(selected_host,show_on_pause)
            return selected_host
        else:
            input(
                f"There are no hosts with HOST_ADDRESS: {address_map['host_address']}")
        return None

    def retrieve_by_host_name(self,show_on_pause:bool = True) -> HostDto:
        if not self._hosts:
            self._hosts = self.service.get_all_for_credentials()
        name_maps = self.show_host_name_columns_on_pause(False)
        item_num = int(input('Select NAME_NO: '))
        name_map = name_maps[item_num-1]
        host_map = self.map_host_to_id_filtered_by_name(name_map['host_name'])
        if len(host_map):
            self.show_host_info_on_pause(False, host_map.values())
            host_id = int(input('Select Host by ID: '))
            selected_host = host_map[host_id]
            self.show_credentials(selected_host,show_on_pause)
            return selected_host
        else:
            input(
                f"There are no hosts with HOST_NAME: {name_map['host_name']}")
        return None
    
    def retrieve_by_host_id(self,show_on_pause:bool = True) -> HostDto:
        if not self._hosts:
            self._hosts = self.service.get_all_for_credentials()
        host_map = self.map_host_to_id()
        if len(host_map):
            self.show_host_info_on_pause(False, host_map.values())
            host_id = int(input('Select Host by ID: '))
            selected_host = host_map[host_id]
            self.show_credentials(selected_host,show_on_pause)
            return selected_host
        else:
            input(
                f"There are no hosts.")
        return None

    def show_platform_id_and_name_columns_on_pause(self, pause: bool):
        try:
            platform_ids = {host.platform_id() for host in self._hosts}
            platforms = self.platform_service.get_all_by_ids(platform_ids)
            field_names = ["PLATFORM_ID", "PLATFORM_NAME"]
            platform_maps = [dict(platform_id=platform.id(), platform_name=platform.name())
                             for platform in platforms]
            UiUtils.clear()
            UiUtils.disp_as_columns(field_names, platform_maps)
            if pause:
                input("Press <enter> to continue...")
        except Exception as e:
            input(
                f"ERR: exception occured while displaying 'Platforms' as columns: {str(e)}")
            return False

    def show_category_by_platform_id_and_category_name_columns_on_pause(self, pause: bool):
        try:
            field_names = ["ID_NO","PLATFORM_ID", "CATEGORY_NAME"]
            category_ids = {(host.platform_id(),host.category_name()) for host in self._hosts}
            category_id_maps = [{'id_no':i+1,'platform_id':category_id[0], 'category_name':category_id[1]}
                             for i,category_id in enumerate(category_ids)]
            UiUtils.clear()
            UiUtils.disp_as_columns(field_names, category_id_maps)
            if pause:
                input("Press <enter> to continue...")
            return category_id_maps
        except Exception as e:
            input(
                f"ERR: exception occured while displaying 'Categories' as columns: {str(e)}")
            return False

    def show_host_address_columns_on_pause(self, pause: bool):
        try:
            field_names = ["ADDR_NO","HOST_ADDRESS"]
            unique_host_adddresses = {host.address() for host in self._hosts}
            host_address_maps = [{'addr_no':i+1,'host_address':address}
                             for i,address in enumerate(unique_host_adddresses)]
            UiUtils.clear()
            UiUtils.disp_as_columns(field_names, host_address_maps)
            if pause:
                input("Press <enter> to continue...")
            return host_address_maps
        except Exception as e:
            input(
                f"ERR: exception occured while displaying 'Host Address' as columns: {str(e)}")
            return False

    def show_host_name_columns_on_pause(self, pause: bool):
        try:
            field_names = ["NAME_NO","HOST_NAME"]
            unique_host_names = {host.name() for host in self._hosts}
            host_name_maps = [{'name_no':i+1,'host_name':name}
                             for i,name in enumerate(unique_host_names)]
            UiUtils.clear()
            UiUtils.disp_as_columns(field_names, host_name_maps)
            if pause:
                input("Press <enter> to continue...")
            return host_name_maps
        except Exception as e:
            input(
                f"ERR: exception occured while displaying 'Host Name' as columns: {str(e)}")
            return False

    def show_host_info_on_pause(self, pause: bool, hosts: list):
        try:
            UiUtils.clear()
            field_names = ["ID", "HOST_NAME", "ADDRESS"]
            host_maps = [dict(id=host.id(), host_name=host.name(), address=host.address())
                         for host in hosts]
            UiUtils.disp_as_columns(field_names, host_maps)
            if pause:
                input("Press <enter> to continue...")
        except Exception as e:
            input(
                f"ERR: exception occured while displaying 'Hosts' as columns: {str(e)}")
            return False

    def show_credentials(self, host: HostDto, pause: bool):
        platform = self.platform_service.get_by_id(host.platform_id())
        UiUtils.clear()
        print(
            f"PLATFORM: {platform.name() if platform else ''}\nADDRESS: {host.address()}\n\tUSERNAME: {host.credentials().username()}\n\tPASSWORD: {host.credentials().password()}")
        if pause:
            input('\nPress <enter> to continue...')

    def map_host_to_id_filtered_by_platform_id(self, platform_id):
        try:
            host_dtos_map = {}
            for host in self._hosts:
                if host.platform_id() == platform_id:
                    host_dtos_map[host.id()] = host

            return host_dtos_map
        except Exception as e:
            print(f'Exception: {e}')

    def map_host_to_id_filtered_by_category(self, platform_id:int, category_name:str):
        hosts = [filtered for filtered in filter(lambda host: host.platform_id() == platform_id 
            and host.category_name() == category_name,self._hosts)]
        return {host.id():host for host in hosts}

    def map_host_to_id_filtered_by_address(self, address:str):
        hosts = [filtered for filtered in filter(lambda host: host.address() == address,self._hosts)]
        return {host.id():host for host in hosts}
    
    def map_host_to_id_filtered_by_name(self, name:str):
        hosts = [filtered for filtered in filter(lambda host: host.name() == name,self._hosts)]
        return {host.id():host for host in hosts}
    
    def map_host_to_id(self):
        return {host.id():host for host in self._hosts}
    