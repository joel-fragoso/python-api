from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from src.main.config import env


class DatabaseConnectionHandler:
    def __init__(self) -> None:
        self.__database_url = env["database_url"]
        self.session = None

    def get_engine(self) -> Engine:
        return create_engine(self.__database_url)

    def __enter__(self) -> "DatabaseConnectionHandler":
        engine = self.get_engine()
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.session.close()
