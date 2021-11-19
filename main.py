from flask import Flask, request
from schemas.main import ProductSchema
from models.product import Product
from models.base import Session


app = Flask(__name__)

session = Session()


@app.get('/')
def home():
    return 'Hi, you are on Home page'

@app.get('/get_products')
def get_products():
    #
    with Session() as session:
        data = session.query(Product).all()
        product_schema = ProductSchema()
        aux = {'data':[]}
        for i in data:
            aux['data'].append(product_schema.dump(i))
        return aux

@app.post('/post_product')
def post_product():
    product = Product(
        name=request.json.get('name'),
        price = request.json.get('price'),
        stock = request.json.get('stock'),
        category = request.json.get('category')
        )
   
    with Session() as session:
        session.add(product)
        session.commit()
    return 'Product added'



app.run(debug=True)