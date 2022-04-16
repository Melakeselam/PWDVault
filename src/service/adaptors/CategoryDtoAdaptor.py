from domain.Category import Category
from service.dtos.CategoryDto import CategoryDto

class CategoryDtoAdaptor:
    def __init__(self) -> None:
        pass

    def model_to_dto(category) -> CategoryDto:
        return CategoryDto(category.platform_id(), category.name(), category.description(), category.password_retention_period())
    
    def dto_to_model(category_dto) -> Category:
        return Category(category_dto.platform_id(), category_dto.name(), category_dto.description(), category_dto.password_retention_period())