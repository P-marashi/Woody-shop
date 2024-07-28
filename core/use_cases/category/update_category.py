from core.entities.category.categories import Category
from core.interfaces.category.repositories import ICategoryRepository


class UpdateCategoryUseCase:
    def __init__(self, repository: ICategoryRepository):
        self.repository = repository

    def execute(self, category_id: int, name: str, description: str) -> Category:
        category = self.repository.get_by_id(category_id)
        category.name = name
        category.description = description
        return self.repository.update(category)
