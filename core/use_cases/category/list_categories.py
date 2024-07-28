from core.entities.category.categories import Category
from core.interfaces.category.repositories import ICategoryRepository


class ListCategoriesUseCase:
    def __init__(self, repository: ICategoryRepository):
        self.repository = repository

    def execute(self) -> list[Category]:
        return self.repository.get_all()
