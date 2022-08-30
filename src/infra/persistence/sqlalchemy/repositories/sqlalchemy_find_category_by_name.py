from typing import Optional
from src.data.protocols.repositories import FindCategoryByNameRepositoryInterface
from src.domain.entities import Category
from src.domain.value_object import CategoryName


class SqlAlchemyFindCategoryByNameRepository(FindCategoryByNameRepositoryInterface):
    def find_by_name(self, category_name: CategoryName) -> Optional[Category]:
        pass
