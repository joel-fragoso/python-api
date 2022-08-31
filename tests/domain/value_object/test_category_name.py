from faker import Faker
from pytest import raises
from src.domain.value_object import CategoryName
from src.domain.exceptions import InvalidCategoryException

faker = Faker("pt-BR")


class TestCategoryName:
    def test_it_should_be_able_to_create_a_category_name(self) -> None:
        category_name = faker.name()
        sut = CategoryName(category_name)
        assert sut.value == category_name

    def test_it_should_not_be_able_to_create_a_category_name_if_is_empty(self) -> None:
        with raises(InvalidCategoryException) as excinfo:
            CategoryName("")
        assert "A categoria é inválida" in str(excinfo.value)

    def test_it_should_not_be_able_to_create_a_category_name_if_is_than_major_to_forty_five_characteres(
        self,
    ) -> None:
        forty_six_characteres = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        with raises(InvalidCategoryException) as excinfo:
            CategoryName(forty_six_characteres)
        assert "A categoria é inválida" in str(excinfo.value)
