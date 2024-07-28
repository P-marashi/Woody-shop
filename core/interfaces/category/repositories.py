from abc import ABC, abstractmethod
from typing import List
from core.entities.category.categories import Category


class ICategoryRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Category]:
        pass

    @abstractmethod
    def get_by_id(self, category_id: int) -> Category:
        pass

    @abstractmethod
    def add(self, category: Category) -> Category:
        pass

    @abstractmethod
    def update(self, category: Category) -> Category:
        pass

    @abstractmethod
    def delete(self, category_id: int) -> None:
        pass
