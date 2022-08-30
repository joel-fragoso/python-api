from src.domain.entities import Category as DomainCategory
from src.domain.value_object import CategoryId, CategoryName
from src.infra.persistence.sqlalchemy.entities import Category as EntityCategory


class CategoryMapper:
    @staticmethod
    def entity_to_domain(domain_category: DomainCategory) -> DomainCategory:
        return EntityCategory(domain_category.id, domain_category.name)

    @staticmethod
    def domain_to_entity(entity_category: EntityCategory) -> EntityCategory:
        return DomainCategory(
            CategoryId(entity_category.id), CategoryName(entity_category.name)
        )
