from abc import ABCMeta, abstractmethod
from src.domain.dtos import CreateCategoryDTO


class CreateCategoryRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def create(self, data: CreateCategoryDTO) -> None:
        pass
