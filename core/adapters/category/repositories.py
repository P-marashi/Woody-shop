from django.db import IntegrityError, transaction
from core.entities.category.categories import Category
from core.exception.category.exceptions import DuplicateCategoryError
from core.interfaces.category.repositories import ICategoryRepository
from .models import CategoryModel


class CategoryRepository(ICategoryRepository):
    def get_all(self) -> list[Category]:
        """Retrieve all categories that have not been deleted."""
        categories = CategoryModel.objects.filter(deleted_at__isnull=True)
        return [self._to_entity(cat) for cat in categories]

    def get_by_id(self, category_id: int) -> Category:
        """Retrieve a category by its ID."""
        try:
            category = CategoryModel.objects.get(
                id=category_id, deleted_at__isnull=True
            )
            return self._to_entity(category)
        except CategoryModel.DoesNotExist:
            raise ValueError("Category not found")

    def get_by_name(self, name: str) -> Category:
        """Retrieve a category by its name."""
        try:
            category = CategoryModel.objects.get(
                name=name, deleted_at__isnull=True
            )
            return self._to_entity(category)
        except CategoryModel.DoesNotExist:
            return None

    @transaction.atomic
    def add(self, category: Category) -> Category:
        """Add a new category."""
        try:
            category_model = CategoryModel(
                name=category.name,
                description=category.description
            )
            category_model.save()
            return self._to_entity(category_model)
        except IntegrityError:
            raise DuplicateCategoryError(
                f"Category with name '{category.name}' already exists."
            )

    @transaction.atomic
    def update(self, category: Category) -> Category:
        """Update an existing category."""
        try:
            category_model = CategoryModel.objects.get(
                id=category.id, deleted_at__isnull=True
            )

            # Check if the name already exists for another category
            existing_category = CategoryModel.objects.filter(
                name=category.name, deleted_at__isnull=True
            ).exclude(id=category.id).first()

            if existing_category:
                raise DuplicateCategoryError(
                    f"Category with name '{category.name}' already exists."
                )

            category_model.name = category.name

            # Only update the description if a new one is provided
            if category.description:
                category_model.description = category.description

            category_model.save()
            return self._to_entity(category_model)
        except CategoryModel.DoesNotExist:
            raise ValueError("Category not found")
        except IntegrityError:
            raise DuplicateCategoryError(
                f"Category with name '{category.name}' already exists."
            )

    @transaction.atomic
    def delete(self, category_id: int) -> None:
        """Delete a category by marking it as deleted."""
        try:
            category = CategoryModel.objects.get(
                id=category_id, deleted_at__isnull=True
            )
            category.delete()
        except CategoryModel.DoesNotExist:
            raise ValueError("Category not found")

    def _to_entity(self, model: CategoryModel) -> Category:
        """Convert a CategoryModel instance to a Category entity."""
        return Category(
            id=model.id,
            name=model.name,
            description=model.description
        )
