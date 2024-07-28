# core/interfaces/category/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from core.use_cases.category.create_category import CreateCategoryUseCase
from core.use_cases.category.list_categories import ListCategoriesUseCase
from core.use_cases.category.get_category import GetCategoryUseCase
from core.use_cases.category.update_category import UpdateCategoryUseCase
from core.use_cases.category.delete_category import DeleteCategoryUseCase
from .serializers import (
    CategorySerializer,
    CategoryCreateSerializer,
    CategoryUpdateSerializer,
)

from core.adapters.category.repositories import CategoryRepository
from core.exception.category.exceptions import (
    DuplicateCategoryError,
    CategoryNotFoundError,
)


class CategoryListView(APIView):
    """
    View use to create new category
    """

    def get(self, request):
        repository = CategoryRepository()
        use_case = ListCategoriesUseCase(repository)
        categories = use_case.execute()

        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=CategorySerializer(many=True), responses=CategorySerializer)
    def post(self, request):
        try:
            serializer = CategoryCreateSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                repository = CategoryRepository()
                use_case = CreateCategoryUseCase(repository)

                created_category = use_case.execute(
                    name=serializer.validated_data["name"],
                    description=serializer.validated_data.get("description", ""),
                )

                response_serializer = CategorySerializer(created_category)
                return Response(
                    response_serializer.data, status=status.HTTP_201_CREATED
                )

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except DuplicateCategoryError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):
    """
    View برای عملیات خواندن، به‌روزرسانی و حذف دسته‌بندی‌ها
    """

    def get(self, request, category_id):
        repository = CategoryRepository()
        use_case = GetCategoryUseCase(repository)

        try:
            category = use_case.execute(category_id=category_id)
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError:
            return Response(
                {"detail": "دسته‌بندی مورد نظر یافت نشد."},
                status=status.HTTP_404_NOT_FOUND,
            )

    @extend_schema(request=CategorySerializer(many=True), responses=CategorySerializer)
    def put(self, request, category_id):
        serializer = CategoryUpdateSerializer(data=request.data, partial=True)

        if serializer.is_valid():
            repository = CategoryRepository()
            use_case = UpdateCategoryUseCase(repository)

            try:
                updated_category = use_case.execute(
                    category_id=category_id,
                    name=serializer.validated_data.get("name"),
                    description=serializer.validated_data.get("description"),
                )
                response_serializer = CategorySerializer(updated_category)
                return Response(response_serializer.data, status=status.HTTP_200_OK)

            except DuplicateCategoryError as e:
                return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

            except CategoryNotFoundError:
                return Response(
                    {"detail": "دسته‌بندی مورد نظر یافت نشد."},
                    status=status.HTTP_404_NOT_FOUND,
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(request=CategorySerializer(many=True), responses=CategorySerializer)
    def delete(self, request, category_id):
        repository = CategoryRepository()
        use_case = DeleteCategoryUseCase(repository)

        try:
            use_case.execute(category_id=category_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValueError:
            return Response(
                {"detail": "دسته‌بندی مورد نظر یافت نشد."},
                status=status.HTTP_404_NOT_FOUND,
            )
