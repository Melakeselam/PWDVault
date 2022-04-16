from repository.PlatformDao import PlatformDao
from domain.Platform import Platform


class PlatformRepository:
    platformDao = PlatformDao()

    def __init__(self) -> None:
        pass

    def save(self, platform):
        if platform.id() is None:
            self.platformDao.save(platform.name(), platform.description())
        else:
            self.platformDao.save(
                platform.id(), platform.name(), platform.description())

    def delete_by_id(self, id):
        self.platformDao.delete_by_id(id)

    def get_all(self):
        platforms = []
        rows = self.platformDao.get_all()

        for tuple in rows:
            platforms.append(Platform(tuple[0], tuple[1], tuple[2]))
        
        return platforms

    def get_by_id(self, id:int) -> Platform:
        row = self.platformDao.get_by_id(id)
        return Platform(row[0], row[1], row[2]) if len(row) else None


    def get_all_by_ids(self, ids:list):
        platforms = []
        rows = self.platformDao.get_all_by_ids(ids)

        for tuple in rows:
            platforms.append(Platform(tuple[0], tuple[1], tuple[2]))
        
        return platforms

