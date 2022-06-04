from src.repository.CategoryDao import CategoryDao
from src.domain.Category import Category, PasswordRetentionPeriod
from src.app.AppContext import AppContext


class CategoryRepository:
    

    def __init__(self, app:AppContext) -> None:
        self.categoryDao = CategoryDao(app)

    def add(self, category):
            self.categoryDao.insert(category.platform_id(), category.name(), category.description(),category.password_retention_period().in_hours())
    
    def update(self, category):
            self.categoryDao.update(category.platform_id(), category.name(), category.description(),category.password_retention_period().in_hours())
        
    def delete_by_id(self, platform_id,category_name):
        self.categoryDao.delete_by_id( platform_id,category_name)

    def get_all(self):
        categories = []
        rows = self.categoryDao.get_all()
        for row in rows:
            categories.append(Category(row[0], row[1], row[2], PasswordRetentionPeriod(hours=row[3])))
        
        return categories

    def get_by_id(self,platform_id:int,name:str):
        try:
            row = self.categoryDao.get_by_id(platform_id,name)
            return Category(row[0], row[1], row[2], PasswordRetentionPeriod(hours=row[3]))
        except Exception as e:
            print(f'Exception: {e}')
