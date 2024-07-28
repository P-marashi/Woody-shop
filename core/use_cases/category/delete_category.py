from core.interfaces.category.repositories import ICategoryRepository


class DeleteCategoryUseCase:
    def __init__(self, repository: ICategoryRepository):
        self.repository = repository

    def execute(self, category_id: int) -> None:
        self.repository.delete(category_id)
