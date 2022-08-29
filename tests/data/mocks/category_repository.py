from typing import Optional
from src.domain.repositories import CategoryRepositoryInterface
from src.domain.value_object import CategoryId, CategoryName
from src.domain.entities import Category
from src.domain.dtos import CreateCategoryDTO


class CategoryRepositorySpy(CategoryRepositoryInterface):
    id: str
    name: str
    duplicated_category: str

    def __init__(self) -> None:
        self.duplicated_category = ""

    def find_by_id(self, category_name: CategoryName) -> Optional[Category]:
        if self.duplicated_category != category_name.value:
            return None
        return Category(CategoryId.generate(), CategoryName(category_name))

    def create(self, data: CreateCategoryDTO) -> None:
        pass