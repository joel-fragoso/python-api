from pytest import raises
from src.domain.value_object import CategoryId
from src.domain.exceptions import InvalidUuidv4Exception


class TestCategoryId:
    def test_it_should_be_able_to_create_a_category_id(self) -> None:
        category_id = "00000000-0000-0000-0000-000000000000"
        sut = CategoryId(category_id)
        assert sut.value == category_id

    def test_it_should_not_be_able_to_create_a_category_id_if_is_invalid(self) -> None:
        category_id = "invalid_category_id"
        with raises(InvalidUuidv4Exception) as excinfo:
            CategoryId(category_id)
        assert "O uuid é inválido" in str(excinfo.value)
