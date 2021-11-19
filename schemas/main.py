from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from models.product import Product


class ProductSchema(SQLAlchemySchema):
    class Meta:
        model = Product
        load_instance = True

    product_id = auto_field()
    stock = auto_field()
    category = auto_field()
    price = auto_field()
    name = auto_field()

