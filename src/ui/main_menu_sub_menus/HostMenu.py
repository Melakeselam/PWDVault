from numpy import array
from service.CategoryService import CategoryService
from service.HostService import HostService
from service.PlatformService import PlatformService
from service.dtos.HostDto import HostDto
from ui.Menus import Menus
from ui.main_menu_sub_menus.CategoryMenu import CategoryMenu
from utils.UiUtils import UiUtils


class HostMenu:
    def __init__(self, user_id) -> None:
        self.user_id = user_id
        self.hosts = None
        self.platform_service = PlatformService()
        self.category_service = CategoryService()
        self.service = HostService(user_id)

    def exec_retrieve_credentials_menu(self):
        retrieve_credentials_menu_level = True
        while retrieve_credentials_menu_level:
            UiUtils.clear()
            menu_choice = UiUtils.disp_and_select_from_menu(
                Menus.retrieve_credentials_menu)
            retrieve_credentials_menu_level = self.exec_menu_choice(
                int(menu_choice))

    def exec_menu_choice(self, choice):
        if choice == 1:
            self.retrieve_by_platform()
        elif choice == 2:
            self.retrieve_by_category()
        elif choice == 3:
            self.retrieve_by_address()
        elif choice == 3:
            self.retrieve_by_host_name()
        elif choice == 4:
            input("show all Hosts")
        elif choice == 5:
            input("retrieve by id")
        elif choice == 6:
            return False
        else:
            input("This menu choice is not available!")
        return True

    def retrieve_by_platform(self):
        if not self.hosts:
            self.hosts = self.service.get_all()
        self.show_platform_id_and_name_columns_on_pause(False)
        platform_id = int(input('Select Platform Id: '))
        host_credentials_map = self.extract_by_platform_id(platform_id)
        if len(host_credentials_map):
            self.show_host_names_on_pause(False, host_credentials_map.values())
            host_id = int(input('Select Host by id: '))
            selected_host = host_credentials_map[host_id]
            self.show_credentials(selected_host)
        else:
            print(f'There are no hosts with PLATFORM_ID: {platform_id}')
            input('Press <enter> to continue...')

    def retrieve_by_category(self):
        if not self.hosts:
            self.hosts = self.service.get_all()
        id_maps = self.show_category_by_platform_id_and_category_name_columns_on_pause(False)
        id_num = int(input('Select ID_NO: '))
        id_map = id_maps[id_num-1]
        host_map = self.extract_host_by_category(id_map['platform_id'], id_map['category_name'])
        if len(host_map):
            self.show_host_names_on_pause(False, host_map.values())
            host_id = int(input('Select Host by ID: '))
            selected_host = host_map[host_id]
            self.show_credentials(selected_host)
        else:
            input(
                f'There are no hosts with PLATFORM_ID: {id_map["platform_id"]} and CATEGORY_NAME: {id_map["category_name"]}')
    
    def retrieve_by_address(self):
        if not self.hosts:
            self.hosts = self.service.get_all()
        id_maps = self.show_category_by_platform_id_and_category_name_columns_on_pause(False)
        id_num = int(input('Select ID_NO: '))
        id_map = id_maps[id_num-1]
        host_map = self.extract_host_by_category(id_map['platform_id'], id_map['category_name'])
        if len(host_map):
            self.show_host_names_on_pause(False, host_map.values())
            host_id = int(input('Select Host by ID: '))
            selected_host = host_map[host_id]
            self.show_credentials(selected_host)
        else:
            input(
                f'There are no hosts with PLATFORM_ID: {id_map["platform_id"]} and CATEGORY_NAME: {id_map["category_name"]}')

    def retrieve_by_host_name(self):
        hosts = self.service.get_all()
        self.show_host_name_address_columns_on_pause(False, hosts)
        host_name = input('Enter Host Name: ')
        host_credentials_map = self.service.get_all_by_host_name(host_name)
        if len(host_credentials_map) > 0:
            self.show_host_names_on_pause(False, host_credentials_map.values())
            host_id = int(input('Select Host by id: '))
            selected_host = host_credentials_map[host_id]
            self.show_credentials(selected_host)
        else:
            input(f'There are no hosts with HOST_NAME: {host_name}')

    def show_platform_id_and_name_columns_on_pause(self, pause: bool):
        try:
            platform_ids = {host.platform_id() for host in self.hosts}
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
            self.hosts
            category_ids = {(host.platform_id(),host.category_name()) for host in self.hosts}
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

    def show_host_names_on_pause(self, pause: bool, host_credentials: list):
        try:
            UiUtils.clear()
            field_names = ["ID", "HOST_NAME"]
            host_maps = [dict(id=host.id(), host_name=host.name())
                         for host in host_credentials]
            UiUtils.disp_as_columns(field_names, host_maps)
            if pause:
                input("Press <enter> to continue...")
        except Exception as e:
            input(
                f"ERR: exception occured while displaying 'Hosts List Menu' as columns: {str(e)}")
            return False

    def show_credentials(self, host: HostDto):
        UiUtils.clear()
        print(
            f'USERNAME: {host.credentials().username()} \nPASSWORD: {host.credentials().password()}')
        input('Press <enter> to continue...')

    def extract_by_platform_id(self, platform_id):
        try:
            host_dtos_map = {}
            for host in self.hosts:
                if host.platform_id() == platform_id:
                    host_dtos_map[host.id()] = host

            return host_dtos_map
        except Exception as e:
            print(f'Exception: {e}')

    def extract_host_by_category(self, platform_id:int, category_name:str):
        hosts = [filtered for filtered in filter(lambda host: host.platform_id() == platform_id 
            and host.category_name() == category_name,self.hosts)]
        return {i+1:host  for i,host in enumerate(hosts)}