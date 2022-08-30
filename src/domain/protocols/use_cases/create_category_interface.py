from abc import ABCMeta, abstractmethod
from src.domain.entities import Category
from src.domain.dtos import CreateCategoryDTO


class CreateCategoryUseCaseInterface(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data: CreateCategoryDTO) -> Category:
        pass
