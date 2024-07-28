from core.entities.category.categories import Category
from core.interfaces.category.repositories import ICategoryRepository


class GetCategoryUseCase:
    def __init__(self, repository: ICategoryRepository):
        self.repository = repository

    def execute(self, category_id: int) -> Category:
        return self.repository.get_by_id(category_id)
