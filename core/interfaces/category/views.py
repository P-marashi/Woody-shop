from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, extend_schema_view

from core.use_cases.category.create_category import CreateCategoryUseCase
from core.use_cases.category.list_categories import ListCategoriesUseCase
from core.use_cases.category.get_category import GetCategoryUseCase
from core.use_cases.category.update_category import UpdateCategoryUseCase
from core.use_cases.category.delete_category import DeleteCategoryUseCase
from core.adapters.category.repositories import CategoryRepository
from core.exception.category.exceptions import (
    DuplicateCategoryError,
    CategoryNotFoundError,
)

from .serializers import (
    CategorySerializer,
    CategoryCreateSerializer,
    CategoryUpdateSerializer,
)

@extend_schema_view(
    list=extend_schema(
        request=None,
        responses=CategorySerializer(many=True)
    ),
    create=extend_schema(
        request=CategoryCreateSerializer,
        responses=CategorySerializer
    ),
    retrieve=extend_schema(
        request=None,
        responses=CategorySerializer
    ),
    update=extend_schema(
        request=CategoryUpdateSerializer,
        responses=CategorySerializer
    ),
    destroy=extend_schema(
        request=None,
        responses=None
    ),
)
class CategoryViewSet(viewsets.ViewSet):
    """
    ViewSet for listing, retrieving,
    creating, updating, and deleting categories.
    """

    def list(self, request):
        """List all categories."""
        repository = CategoryRepository()
        use_case = ListCategoriesUseCase(repository)
        categories = use_case.execute()

        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Create a new category."""
        serializer = CategoryCreateSerializer(data=request.data)
        if serializer.is_valid():
            repository = CategoryRepository()
            use_case = CreateCategoryUseCase(repository)

            try:
                created_category = use_case.execute(
                    name=serializer.validated_data["name"],
                    description=serializer.validated_data.get("description", ""),
                )

                response_serializer = CategorySerializer(created_category)
                return Response(
                    response_serializer.data,
                    status=status.HTTP_201_CREATED
                )
            except DuplicateCategoryError as e:
                return Response(
                    {"error": str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Retrieve a single category by ID."""
        repository = CategoryRepository()
        use_case = GetCategoryUseCase(repository)

        try:
            category = use_case.execute(category_id=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CategoryNotFoundError:
            return Response(
                {"detail": "دسته‌بندی مورد نظر یافت نشد."},
                status=status.HTTP_404_NOT_FOUND,
            )

    def update(self, request, pk=None):
        """Update an existing category by ID."""
        serializer = CategoryUpdateSerializer(data=request.data, partial=True)

        if serializer.is_valid():
            repository = CategoryRepository()
            use_case = UpdateCategoryUseCase(repository)

            try:
                updated_category = use_case.execute(
                    category_id=pk,
                    name=serializer.validated_data.get("name"),
                    description=serializer.validated_data.get("description"),
                )
                response_serializer = CategorySerializer(updated_category)
                return Response(
                    response_serializer.data,
                    status=status.HTTP_200_OK
                )
            except DuplicateCategoryError as e:
                return Response(
                    {"detail": str(e)}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            except CategoryNotFoundError:
                return Response(
                    {"detail": "دسته‌بندی مورد نظر یافت نشد."},
                    status=status.HTTP_404_NOT_FOUND,
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Delete a category by ID."""
        repository = CategoryRepository()
        use_case = DeleteCategoryUseCase(repository)

        try:
            use_case.execute(category_id=pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CategoryNotFoundError:
            return Response(
                {"detail": "دسته‌بندی مورد نظر یافت نشد."},
                status=status.HTTP_404_NOT_FOUND,
            )
