from faker import Faker
from src.domain.value_object import CategoryName

faker = Faker("pt-BR")


class TestCategoryName:
    def test_it_should_be_able_to_create_a_category_name(self) -> None:
        category_name = faker.name()
        sut = CategoryName(category_name)
        assert sut.value == category_name
