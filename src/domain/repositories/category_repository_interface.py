from abc import ABCMeta, abstractmethod
from typing import Optional
from src.domain.entities import Category
from src.domain.dtos import CreateCategoryDTO
from src.domain.value_object import CategoryName


class CategoryRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def find_by_id(self, category_name: CategoryName) -> Optional[Category]:
        pass

    @abstractmethod
    def create(self, data: CreateCategoryDTO) -> None:
        pass
