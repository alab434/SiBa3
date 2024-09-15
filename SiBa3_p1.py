##### *************************************************************************
##### INTERFACE
from abc import ABC, abstractproperty, abstractclassmethod

class Transacao(ABC):	##    classe abstrata
	@property
	@abstractproperty
	def valor(self):
		pass

	## métodos públicos da classe abstrata
	@abstractclassmethod
	def registrar(self, conta):	## 
		pass


##### -------------------------------------------------------------------------
class Deposito(Transacao):		## extende a classe abstrata Transacao
	## construtor
	def __init__(self, valor):
		## atributos privados
		self._valor = valor		## extende a classe abstrata Transacao

	@property
	def valor(self):
		return self._valor

	## métodos abstratos
	def registrar(self, conta):
		if conta.depositar(self.valor):
			conta.historico.adicionar_transacao(self)


##### -------------------------------------------------------------------------
class Saque(Transacao):		## extende a transasão
	## construtor
	def __init__(self, valor):
		## atributos privados
		self._valor = valor		##    ponto flutuante

	@property
	def valor(self):
		return self._valor

	## métodos públicos da classe abstrata
	def registrar(self, conta):
		if conta.sacar(self.valor):
			conta.historico.adicionar_transacao(self)

##### /INTERFACE
##### _________________________________________________________________________



##### *************************************************************************
##### CLIENTES
class Cliente():
	## construtor
	def __init__(self, endereco):
		## atributos públicos
		self.endereco = endereco	##   endereco = logradouro, no - bairro - cidade/uf
		self.contas = []				## lista das contas, o cliente pode ter mais de uma conta

	## métodos públicos
	def adicionar_conta(self, conta):
		self.contas.append(conta)

	def realizar_transacao(self, conta, transacao):		## DEPOSITO | SAQUE
		transacao.registrar(conta)


##### -------------------------------------------------------------------------
class PessoaFisica(Cliente):	## classe filha de Cliente
	## construtor
	def __init__(self, cpf, nome, data_nascimento, endereco):
		## atributos herdados da classe mãe
		super().__init__(endereco)
		## atributos públicos
		self.cpf = cpf									##   cpf = 12345678911
		self.nome = nome								##   nome = 
		self.data_nascimento = data_nascimento	##   data_nascimento = dd/mm/aaaa

##### /CLIENTES
##### _________________________________________________________________________



##### *************************************************************************
##### EXTRATO
class Historico():
	def __init__(self):
		## atributos públicos
		self._extrato_historico = [] # extrato = ''

	@property
	def exibir(self):
		return self._extrato_historico

	## métodos públicos
	def adicionar_transacao(self, tipo):
		self._extrato_historico.append({
			'tipo': _extrato_historico.__name__.upper(),
			'valor': tipo.valor
		})
		# extrato.append(('DEPOSITO', valor_deposito))
		# saldo += valor_deposito

##### /EXTRATO
##### _________________________________________________________________________



##### *************************************************************************
##### CONTAS
## AGENCIA = '0001'
class Conta():
	## método construtor
	def __init__(self, numero, cliente):
		## atributos privados
		self._saldo = 0.00				##   ponto flutuante
		self._numero = numero			##   conta_numero  ->  sequencial 1, 2, 3
		self._agencia = '0001'			##   agencia  ->  fixo = `0001`
		self._cliente = cliente 		##   objeto Cliente
		self._historico = Historico	##   classe Historico
	
	@property
	def saldo(self):	## deve retorna um float
		return self._saldo
	
	@property
	def extrato(self):
		return self._historico

	@property
	def saldo(self):
		return self._saldo

	@property
	def numero(self):
		return self._numero

	@property
	def agencia(self):
		return self._agencia

	@property
	def cliente(self):
		return self._cliente

	@property
	def historico(self):
		return self._historico

	@classmethod
	def nova_conta(classe, cliente, numero):	## classmethod, retorna o objeto Conta
		return classe(numero, cliente)

	## metodos públicos
	def sacar(self, valor):	## deve retorna um booleano
		saldo = self.saldo
		if saldo <= 0.00:
			print(f'   A CONTA NÃO POSSUE SALDO.')
			return False
		else:
			# print(f'   SALDO DISPONÍVEL     = R$ {saldo:9.2f}')
			if valor <= 0:
				print(f'   VALOR INVÁLIDO.')
				return False
			else:
				if valor > saldo:
					print(f'   SALDO INSUFICIENTE.')
					return False
				else:
					self._saldo -= valor
					print(f'   SAQUE EFETUADO       - R$ {valor:9.2f}')
					return True


	def depositar(self, valor):	## deve retorna um booleano
		if valor <= 0:
			print(f'   VALOR INVÁLIDO.')
			return False
		else:
			self._saldo += valor
			print(f'   DEPÓSITO EFETUADO    + R$ {valor:9.2f}')
			return True


	def __str__(self):
		return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

##### _________________________________________________________________________



##### -------------------------------------------------------------------------
## SAQUES_VALOR_LIMITE_POR_TRANSACAO = 500.00
## SAQUES_QUANTIDADE_POR_DIA = 3
class ContaCorrente(Conta):	##    classe filha de Conta
	## método construtor
	def __init__(self, numero, cliente, limite=500.00, limite_saques=3):
		## atributos herdados da classe mãe
		super().__init__(numero, cliente)
		## atributos privados
		self._limite = limite
		self._limite_saques = limite_saques
		self._numero_saques = 0
	
	## metodos públicos
	def sacar(self, valor):	## deve retorna um booleano
		saldo = self.saldo
		if saldo <= 0.00:
			print(f'   A CONTA NÃO POSSUE SALDO.')
			return False
		else:
			# print(f'   SALDO DISPONÍVEL     = R$ {saldo:9.2f}')
			if valor <= 0:
				print(f'   VALOR INVÁLIDO.')
				return False
			else:
				if valor > saldo:
					print(f'   SALDO INSUFICIENTE.')
					return False
				elif valor > self._limite:
					print(f'   O VALOR MÁXIMO PARA SAQUES É R$ {self._limite}')
				elif self._numero_saques >= self._limite_saques:
					print(f'   LIMITE DE SAQUES DIÁRIO ATINGIDO.')
					return False
				else:
					saldo -= valor
					self._numero_saques += 1
					print(f'   SAQUE EFETUADO       - R$ {valor:9.2f}')

##### _________________________________________________________________________



##### *************************************************************************
##### *************************************************************************
##### *************************************************************************





##### *************************************************************************
##### *************************************************************************
##### *************************************************************************

"""

c1 = Conta.nova_conta('Saci', 1)
# c2 = Conta.nova_conta('Saci', 2)
print(c1)

# c1.extrato
# c1._saldo = 2000.00
# c1.sacar(50.0)
c1.depositar(60000.00)
c1.sacar(500.0)
c1.sacar(500.0)
c1.sacar(600.0)
c1.sacar(75.0)
c1.sacar(25.0)
c1.sacar(50.0)
c1.depositar(1000.00)
c1.sacar(750.0)
"""
