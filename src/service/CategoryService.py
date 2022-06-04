from src.service.dtos.CategoryDto import CategoryDto
from src.domain.Category import Category
from src.repository.CategoryRepository import CategoryRepository as Repository
from src.service.adaptors.CategoryDtoAdaptor import CategoryDtoAdaptor as Adaptor
from src.app.AppContext import AppContext
class CategoryService:
    

    def __init__(self, app:AppContext) -> None:
        self.category_repo = Repository(app)

    def add_category(self, category_dto):
        
        self.category_repo.add(Adaptor.dto_to_model(category_dto))

    def update_category(self,category_dto):
        self.category_repo.update(Adaptor.dto_to_model(category_dto))

    def remove_category(self, platform_id, category_name):
        self.category_repo.delete_by_id(platform_id,category_name)

    def get_all(self):
        category_dtos = []
        categories = self.category_repo.get_all()
        for category in categories:
            category_dtos.append(Adaptor.model_to_dto(category))
        return category_dtos

    def get_by_id(self,platform_id:int, name:str) -> CategoryDto:
        category = self.category_repo.get_by_id(platform_id,name)
        return Adaptor.model_to_dto(category)
