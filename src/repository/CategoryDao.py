from persistence.persistence import Persistence as Persist
from multipledispatch import dispatch

class CategoryDao:
    persist = Persist()

    def __init__(self) -> None:
        pass


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
        
