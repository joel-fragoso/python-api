from src.domain.entities import Category
from src.domain.value_object import CategoryId, CategoryName
from src.domain.exceptions import DuplicatedCategoryException
from src.data.dtos import CreateCategoryDTO
from src.data.repositories import CategoryRepositoryInterface


class CreateCategoryUseCase:
    def __init__(self, category_repository: CategoryRepositoryInterface) -> None:
        self.__category_repository = category_repository

    def execute(self, data: CreateCategoryDTO) -> Category:
        find_category = self.__category_repository.find_by_id(CategoryName(data.name))
        if find_category:
            raise DuplicatedCategoryException()
        self.__category_repository.create(data)
        category = Category(CategoryId(CategoryId.generate()), CategoryName(data.name))
        return category
