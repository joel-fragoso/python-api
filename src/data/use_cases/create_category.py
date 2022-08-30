from src.domain.entities import Category
from src.domain.dtos import CreateCategoryDTO
from src.domain.value_object import CategoryId, CategoryName
from src.domain.exceptions import DuplicatedCategoryException
from src.domain.protocols.use_cases import CreateCategoryUseCaseInterface
from src.data.protocols.repositories import (
    CreateCategoryRepositoryInterface,
    FindCategoryByNameRepositoryInterface,
)


class CreateCategoryUseCase(CreateCategoryUseCaseInterface):
    def __init__(
        self,
        find_category_by_name_repository: FindCategoryByNameRepositoryInterface,
        create_category_repository: CreateCategoryRepositoryInterface,
    ) -> None:
        self.__find_category_by_name = find_category_by_name_repository
        self.__create_category_repository = create_category_repository

    def execute(self, data: CreateCategoryDTO) -> Category:
        find_category = self.__find_category_by_name.find_by_name(
            CategoryName(data.name)
        )
        if find_category:
            raise DuplicatedCategoryException()
        self.__create_category_repository.create(data)
        category = Category(CategoryId(CategoryId.generate()), CategoryName(data.name))
        return category
