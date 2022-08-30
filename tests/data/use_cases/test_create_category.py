from faker import Faker
from pytest import raises
from src.domain.exceptions import DuplicatedCategoryException
from src.domain.dtos import CreateCategoryDTO
from src.data.use_cases import CreateCategoryUseCase
from src.data.protocols.repositories import (
    CreateCategoryRepositoryInterface,
    FindCategoryByNameRepositoryInterface,
)
from tests.data.mocks import (
    CreateCategoryRepositorySpy,
    FindCategoryByNameRepositorySpy,
)

faker = Faker("pt-BR")


class SutType:
    def __init__(
        self,
        sut: CreateCategoryUseCase,
        find_category_by_name_repository: FindCategoryByNameRepositoryInterface,
        create_category_repository: CreateCategoryRepositoryInterface,
    ) -> None:
        self.__sut = sut
        self.__find_category_by_name_repository = find_category_by_name_repository
        self.__create_category_repository = create_category_repository

    @property
    def sut(self) -> CreateCategoryUseCase:
        return self.__sut

    @property
    def find_category_by_name_repository(self) -> FindCategoryByNameRepositoryInterface:
        return self.__find_category_by_name_repository

    @property
    def create_category_repository(self) -> CreateCategoryRepositoryInterface:
        return self.__create_category_repository


class CreateCategoryUseCaseFactory:
    @staticmethod
    def create() -> SutType:
        find_category_by_name_repository = FindCategoryByNameRepositorySpy()
        create_category_repository = CreateCategoryRepositorySpy()
        sut = CreateCategoryUseCase(
            find_category_by_name_repository, create_category_repository
        )
        sut_type = SutType(
            sut, find_category_by_name_repository, create_category_repository
        )
        return (
            sut_type.sut,
            sut_type.find_category_by_name_repository,
            sut_type.create_category_repository,
        )


class TestCreateCategoryUseCase:
    def test_it_should_be_able_to_create_a_category(self) -> None:
        category_name = faker.name()
        (
            sut,
            find_category_by_name_repository,
            create_category_repository,
        ) = CreateCategoryUseCaseFactory.create()
        find_category_by_name_repository.name = ""
        create_category_repository.name = category_name
        create_category_dto = CreateCategoryDTO(category_name)
        category = sut.execute(create_category_dto)
        assert category.id is not None
        assert category.name == create_category_repository.name

    def test_it_should_not_be_able_to_create_a_category_with_the_same_name(
        self,
    ) -> None:
        category_name = faker.name()
        sut, find_category_by_name_repository, _ = CreateCategoryUseCaseFactory.create()
        find_category_by_name_repository.name = category_name
        create_category_dto = CreateCategoryDTO(category_name)
        sut.execute(create_category_dto)
        find_category_by_name_repository.duplicated_name = category_name
        with raises(DuplicatedCategoryException) as excinfo:
            sut.execute(create_category_dto)
        assert "A categoria já está em uso" in str(excinfo.value)
