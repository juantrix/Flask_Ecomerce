import re
from flask import Flask


app = Flask(__name__)


@app.get('/')
def home():
    return 'Hi, you are on Home page'


app.run(debug=True)