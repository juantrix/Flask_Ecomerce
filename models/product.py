import sqlalchemy as sa
from models.base import  Base, engine


class Product(Base):
    __tablename__ = "Product"

    product_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)
    price = sa.Column(sa.REAL, nullable=False)
    stock = sa.Column(sa.Integer, default=0)
    category = sa.Column(sa.String, nullable=False)

    def __str__(self):
        return self.name

Base.metadata.create_all(engine)
