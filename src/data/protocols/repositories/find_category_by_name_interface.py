from abc import ABCMeta, abstractmethod
from typing import Optional
from src.domain.entities import Category
from src.domain.value_object import CategoryName


class FindCategoryByNameRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def find_by_name(self, category_name: CategoryName) -> Optional[Category]:
        pass
