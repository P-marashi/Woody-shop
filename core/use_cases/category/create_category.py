from core.entities.category.categories import Category
from core.interfaces.category.repositories import ICategoryRepository
from core.exception.category.exceptions import DuplicateCategoryError


class CreateCategoryUseCase:
    def __init__(self, repository: ICategoryRepository):
        self.repository = repository

    def execute(self, name: str, description: str) -> Category:
        existing_category = self.repository.get_by_name(name)
        if existing_category:
            raise DuplicateCategoryError(f"Category with name '{name}' already exists.")

        new_category = Category(id=0, name=name, description=description)
        return self.repository.add(new_category)
