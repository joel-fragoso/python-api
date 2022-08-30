from src.domain.dtos import CreateCategoryDTO
from src.data.protocols.repositories import CreateCategoryRepositoryInterface


class CreateCategoryRepositorySpy(CreateCategoryRepositoryInterface):
    name: str

    def create(self, data: CreateCategoryDTO) -> None:
        pass
