from multipledispatch import dispatch

from src.app.AppContext import AppContext

class CategoryDao:

    def __init__(self, app:AppContext) -> None:
        self.persist = app.persistence()


    def insert(self, platform_id, name, description, password_retention_period_in_hours):
        fields_to_insert = dict(platform_id=platform_id, name=name, description=description, pwd_retention_hours=password_retention_period_in_hours)
        self.persist.insert_into_table('Category', fields_to_insert)


    def update(self, platform_id, name, description, password_retention_period_in_hours):
        fields_to_update = dict(description=description,  pwd_retention_hours=password_retention_period_in_hours)
        conditions = dict(platform_id=platform_id, name=name)

        self.persist.update_table('Category', fields_to_update, conditions)

    def delete_by_id(self, platform_id, category_name):
        conditions = dict(platform_id=platform_id, name=category_name)
        self.persist.delete_by_fields('Category',conditions)

    def get_all(self):
        return self.persist.find_all_in_table('Category')

    def get_by_id(self,platform_id:int,name:str):
        
        fields = ['platform_id','name']
        values = [platform_id,name]
        rows = self.persist.find_by_fields_in_table('Category',fields,values)
        return rows[0]
        
