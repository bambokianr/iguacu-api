from sql_alchemy import database

class SellerModel(database.Model):
	__tablename__ = 'sellers'

	id = database.Column(database.String, primary_key = True)
	nome = database.Column(database.String(255))
	CPF = database.Column(database.String(11))
	CEP = database.Column(database.String(8))
	endereco = database.Column(database.String(150))
	cidade = database.Column(database.String(60))
	UF = database.Column(database.String(2))

	def __init__(self, id, nome, CPF, CEP, endereco, cidade, UF):
		self.id = id
		self.nome = nome
		self.CPF = CPF
		self.CEP = CEP
		self.endereco = endereco
		self.cidade = cidade
		self.UF = UF
	
	def json(self):
		return {
			'id': self.id,
			'nome': self.nome,
			'CPF': self.CPF,
			'CEP': self.CEP,
			'endereco': self.endereco,
			'cidade': self.cidade,
			'UF': self.UF
		}

	@classmethod
	def find(cls, id):
		seller = cls.query.filter_by(id = id).first() # SELECT * FROM sellers WHERE id=id LIMIT 1
		if seller:
			return seller
		return None
	
	def save(self):
		database.session.add(self)
		database.session.commit()
	
	def update(self, nome, CPF, CEP, endereco, cidade, UF):
		self.nome = nome
		self.CPF = CPF
		self.CEP = CEP
		self.endereco = endereco
		self.cidade = cidade
		self.UF = UF

	def delete(self):
		database.session.delete(self)
		database.session.commit()