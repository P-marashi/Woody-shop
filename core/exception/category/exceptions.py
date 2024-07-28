class DuplicateCategoryError(Exception):
    """Exception raised when a category already exists."""
    pass


class CategoryNotFoundError(Exception):
    """Exception raised when a category is not found."""
    pass
