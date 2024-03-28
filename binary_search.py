class No:

	def __init__(self, valor):
		self.valor=valor
		self.esquerda=None
		self.direita=None

	def obter_valor(self):
		return self.valor

	def obter_esquerda(self):
		return self.esquerda

	def obter_direita(self):
		return self.direita
	
	def set_esquerda(self, esquerda):
		self.esquerda=esquerda

	def set_direita(self, direita):
		self.direita=direita

class TreeBinarySearch:
	def __init__(self):
		self.raiz=None
	
	def obter_raiz(self):
		return self.raiz

	def inserir(self, valor):
		no = No(valor)
		# se raiz for vazia sete o primeiro no informado
		if self.raiz is None:
			self.raiz = no
		else:
			# se tiver raiz
			no_atual, no_pai = self.raiz, None
			while True:
				if no_atual is not None:
					no_pai = no_atual
					if no.obter_valor() < no_atual.obter_valor():
						no_atual = no_atual.obter_esquerda()
					else:
						no_atual = no_atual.obter_direita()
				else:
					if no.obter_valor() < no_pai.obter_valor():
						no_pai.set_esquerda(no)
					else:
						no_pai.set_direita(no)
					break

	def mostrar_arvore(self, no_atual):
		if no_atual != None:
			self.mostrar_arvore(no_atual.obter_esquerda())
			print(f'{no_atual.obter_valor()}', end=' ')
			self.mostrar_arvore(no_atual.obter_direita())


# Criando arvore binaria
tree = TreeBinarySearch()
# Inserindo numeros na arvore
tree.inserir(8)
tree.inserir(3)
tree.inserir(6)
tree.inserir(10)
tree.inserir(14)
tree.inserir(1)
tree.inserir(7)
tree.inserir(13)
tree.inserir(4)
# Imprimindo a arvore em ordem simetrica
tree.mostrar_arvore(tree.obter_raiz())
