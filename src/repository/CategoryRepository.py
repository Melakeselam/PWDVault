from repository.CategoryDao import CategoryDao
from domain.Category import Category, PasswordRetentionPeriod


class CategoryRepository:
    categoryDao = CategoryDao()

    def __init__(self) -> None:
        pass

    def add(self, category):
            self.categoryDao.insert(category.platform_id(), category.name(), category.description(),category.password_retention_period().in_hours())
    
    def update(self, category):
            self.categoryDao.update(category.platform_id(), category.name(), category.description(),category.password_retention_period().in_hours())
        
    def delete_by_id(self, platform_id,category_name):
        self.categoryDao.delete_by_id( platform_id,category_name)

    def get_all(self):
        categories = []
        rows = self.categoryDao.get_all()
        for tuple in rows:
            categories.append(Category(tuple[0], tuple[1], tuple[2], PasswordRetentionPeriod(hours=tuple[3])))
        
        return categories
