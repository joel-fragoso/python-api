from faker import Faker
from pytest import raises
from src.data.use_cases import CreateCategoryUseCase
from src.domain.repositories import CategoryRepositoryInterface
from src.domain.dtos import CreateCategoryDTO
from src.domain.exceptions import DuplicatedCategoryException
from tests.data.mocks import CategoryRepositorySpy

faker = Faker("pt-BR")


class SutType:
    def __init__(
        self,
        sut: CreateCategoryUseCase,
        category_repository: CategoryRepositoryInterface,
    ) -> None:
        self.__sut = sut
        self.__category_repository = category_repository

    @property
    def sut(self) -> CreateCategoryUseCase:
        return self.__sut

    @property
    def category_repository(self) -> CategoryRepositoryInterface:
        return self.__category_repository


class CreateCategoryUseCaseFactory:
    @staticmethod
    def create() -> SutType:
        category_repository = CategoryRepositorySpy()
        sut = CreateCategoryUseCase(category_repository)
        sut_type = SutType(sut, category_repository)
        return sut_type.sut, sut_type.category_repository


class TestCreateCategoryUseCase:
    def test_it_should_be_able_to_create_a_category(self):
        category_name = faker.name()
        sut, category_repository = CreateCategoryUseCaseFactory.create()
        category_repository.id = "category_id"
        category_repository.name = category_name
        create_category_dto = CreateCategoryDTO(category_name)
        category = sut.execute(create_category_dto)
        assert category.id == category_repository.id
        assert category.name == category_repository.name

    # def test_it_should_be_able_to_create_a_category_name_with_major_than_three_characteres(self):
    #     category_name = "Ca"
    #     sut, category_repository = CreateCategoryUseCaseFactory.create()
    #     category_repository.id = 'category_id'
    #     category_repository.name = category_name
    #     create_category_dto = CreateCategoryDTO(category_name)
    #     with raises(InvalidCategoryException) as excinfo:
    #         sut.execute(create_category_dto)
    #     assert "A categoria é inválida" in str(excinfo.value)

    def test_it_should_not_be_able_to_create_a_category_with_the_same_name(self):
        category_name = faker.name()
        sut, category_repository = CreateCategoryUseCaseFactory.create()
        category_repository.id = "category_id"
        category_repository.name = category_name
        create_category_dto = CreateCategoryDTO(category_name)
        sut.execute(create_category_dto)
        category_repository.duplicated_category = category_name
        with raises(DuplicatedCategoryException) as excinfo:
            sut.execute(create_category_dto)
        assert "A categoria já está em uso" in str(excinfo.value)
