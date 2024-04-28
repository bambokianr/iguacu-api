from flask import Flask
from flask_restful import Api

from resources.seller import Sellers, Seller

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iguacu.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

@app.before_first_request
def create_database():
	database.create_all()

api.add_resource(Sellers, '/sellers')
api.add_resource(Seller, '/sellers', '/sellers/<string:id>')

if __name__ == '__main__':
	from sql_alchemy import database
	database.init_app(app)

	app.run(debug = True)