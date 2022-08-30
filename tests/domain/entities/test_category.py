from faker import Faker
from src.domain.entities import Category
from src.domain.value_object import CategoryId, CategoryName

faker = Faker("pt-BR")


class TestCategory:
    def test_it_should_be_able_to_create_a_category_entity(self) -> None:
        category_name = faker.name()
        sut = Category(CategoryId(CategoryId.generate()), CategoryName(category_name))
        assert sut.id is not None
        assert sut.name == category_name
