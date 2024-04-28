from flask_restful import Resource, reqparse
import uuid

from models.seller import SellerModel

class Sellers(Resource):
	def get(self):
		return { "data": [ seller.json() for seller in SellerModel.query.all()] }

class Seller(Resource):
	args = reqparse.RequestParser()
	args.add_argument('nome', type = str, required = True, help = "O campo 'nome' é obrigatório.")
	args.add_argument('CPF', type = str, required = True, help = "O campo 'CPF' é obrigatório.")
	args.add_argument('CEP', type = str, required = True, help = "O campo 'CEP' é obrigatório.")
	args.add_argument('endereco', type = str)
	args.add_argument('cidade', type = str)
	args.add_argument('UF', type = str)

	def get(self, id):
		seller = SellerModel.find(id)
		if seller:
			return seller.json()

		return { "message": f"Vendedor com id '{id}' não encontrado." }, 404

	def post(self):
		data = Seller.args.parse_args()
		new_seller = SellerModel(str(uuid.uuid4()), **data)
		
		try:
			new_seller.save()
		except:
			return { "message": f"Erro interno ao tentar salvar o vendedor com o nome '{new_seller.nome}'." }, 500

		return new_seller.json(), 201

	def put(self, id):
		seller = SellerModel.find(id)
		if seller:
			data = Seller.args.parse_args()
			seller.update(**data)

			try:
				seller.save()
			except:
				return { "message": f"Erro interno ao tentar atualizar o vendedor com o nome '{seller.nome}'." }, 500

			return seller.json(), 200

		return { "message": f"Vendedor com id '{id}' não encontrado." }, 404

	def delete(self, id):
		seller = SellerModel.find(id)
		if seller:

			try:
				seller.delete()
			except:
				return { "message": f"Erro interno ao tentar excluir o vendedor com o nome '{seller.nome}'." }, 500
		
			return { "message": f"Vendedor com id '{id}' excluído." }, 200

		return { "message": f"Vendedor com id '{id}' não encontrado." }, 404