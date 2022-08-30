from src.data.protocols.repositories import CreateCategoryRepositoryInterface
from src.domain.dtos import CreateCategoryDTO


class SqlAlchemyCreateCategoryRepository(CreateCategoryRepositoryInterface):
    def create(self, data: CreateCategoryDTO) -> None:
        pass
