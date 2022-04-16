from domain.Category import Category
from repository.CategoryRepository import CategoryRepository as Repository
from service.adaptors.CategoryDtoAdaptor import CategoryDtoAdaptor as Adaptor
class CategoryService:
    category_repo = Repository()

    def __init__(self) -> None:
        pass

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
