from src.app.AppContext import AppContext


class HostDao:

    def __init__(self, app:AppContext, user_id) -> None:
        self.user_id = user_id
        self.persist = app.persistence()

    def get_all(self) -> list:
        fields = ['user_id']
        values = [self.user_id]
        return self.persist.find_by_fields_in_table('Host',fields, values)

    def find_all_by_platform_id(self, platform_id):
        fields = ['user_id','platform_id']
        values = [self.user_id, platform_id]
        return self.persist.find_by_fields_in_table('Host',fields, values)
    
    def find_all_by_category_id(self, platform_id,category_name):
        fields = ['user_id','platform_id','category_name']
        values = [self.user_id, platform_id,category_name]
        return self.persist.find_by_fields_in_table('Host',fields, values)

    def find_by_id(self, id):
        fields = ['user_id','id']
        values = [self.user_id, id]
        return self.persist.find_by_fields_in_table('Host',fields, values)