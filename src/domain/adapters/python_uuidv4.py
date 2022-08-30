from uuid import UUID, uuid4
from src.domain.protocols.adapters import Uuidv4AdapterInterface


class PythonUuidv4Adapter(Uuidv4AdapterInterface):
    @staticmethod
    def generate() -> str:
        return str(uuid4())

    @staticmethod
    def is_valid(value: str) -> bool:
        try:
            UUID(str(value))
            return True
        except ValueError:
            return False
