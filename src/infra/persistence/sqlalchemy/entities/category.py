from sqlalchemy import Column, String
from src.infra.persistence.sqlalchemy.config import Base


class Category(Base):
    __tablename__ = "categories"

    id: Column(String, primary_key=True, autoincrement=False)
    name: Column(String(45), nullable=False, unique=True)
