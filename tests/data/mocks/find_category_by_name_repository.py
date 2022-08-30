from typing import Optional
from src.domain.entities import Category
from src.domain.value_object import CategoryId, CategoryName
from src.data.protocols.repositories import FindCategoryByNameRepositoryInterface


class FindCategoryByNameRepositorySpy(FindCategoryByNameRepositoryInterface):
    name: str
    duplicated_name: str

    def __init__(self) -> None:
        self.duplicated_name = ""

    def find_by_name(self, category_name: CategoryName) -> Optional[Category]:
        if self.duplicated_name != category_name.value:
            return None
        return Category(CategoryId(CategoryId.generate()), CategoryName(category_name))
