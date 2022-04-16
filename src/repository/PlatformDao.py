from persistence.persistence import Persistence as Persist, entity_tables as tables
from multipledispatch import dispatch

class PlatformDao:
    persist = Persist()

    def __init__(self) -> None:
        pass

    @dispatch(str,str)
    def save(self, name, description):
        fields_to_insert = dict(name=name, description=description)
        self.persist.insert_into_table('Platform', fields_to_insert)

    @dispatch(int,str,str)
    def save(self, id, name, description):
        fields_to_save = dict(name=name,description=description)
        conditions = dict(id=id)
        self.persist.update_table('Platform', fields_to_save, conditions)

    def delete_by_id(self,id):
        self.persist.delete_by_field('Platform','id',id)

    def get_all(self):
        return self.persist.find_all_in_table('Platform')

    def get_all_by_ids(self,ids):
        return self.persist.find_all_in_table_by_values('Platform','id',ids)
        
