##### *************************************************************************
##### INTERFACE
from abc import ABC, abstractproperty, abstractclassmethod

class Transacao(ABC):	
	@property
	@abstractproperty
	def valor(self):
		pass

	@abstractclassmethod
	def registrar(self, conta):	
		pass


##### -------------------------------------------------------------------------
class Deposito(Transacao):	
	def __init__(self, valor):
		self._valor = valor	

	@property
	def valor(self):
		return self._valor

	def registrar(self, conta):
		if conta.depositar(self.valor):
			conta.historico.adicionar_transacao(self)


##### -------------------------------------------------------------------------
class Saque(Transacao):		

	def __init__(self, valor):
		self._valor = valor	

	@property
	def valor(self):
		return self._valor

	def registrar(self, conta):
		if conta.sacar(self.valor):
			conta.historico.adicionar_transacao(self)

##### /INTERFACE
##### _________________________________________________________________________



##### *************************************************************************
##### CLIENTES
class Cliente():
	def __init__(self, endereco):
		self.endereco = endereco	
		self.contas = []		

	def adicionar_conta(self, conta):
		self.contas.append(conta)

	def realizar_transacao(self, conta, transacao):		
		transacao.registrar(conta)


##### -------------------------------------------------------------------------
class PessoaFisica(Cliente):	
	def __init__(self, cpf, nome, data_nascimento, endereco):
		super().__init__(endereco)
		self.cpf = cpf				
		self.nome = nome			
		self.data_nascimento = data_nascimento	

##### /CLIENTES
##### _________________________________________________________________________



##### *************************************************************************
##### EXTRATO
class Historico():
	def __init__(self):
		self._extrato_historico = [] 

	@property
	def exibir(self):
		return self._extrato_historico

	def adicionar_transacao(self, tipo):
		self._extrato_historico.append({
			'tipo': _extrato_historico.__name__.upper(),
			'valor': tipo.valor
		})

##### /EXTRATO
##### _________________________________________________________________________



##### *************************************************************************
##### CONTAS
## AGENCIA = '0001'
class Conta():
	def __init__(self, numero, cliente):
		self._saldo = 0.00	
		self._numero = numero		
		self._agencia = '0001'	
		self._cliente = cliente 	
		self._historico = Historico	
	
	@property
	def saldo(self):	
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
	def nova_conta(classe, cliente, numero):	
		return classe(numero, cliente)

	def sacar(self, valor):	
		saldo = self.saldo
		if saldo <= 0.00:
			print(f'   A CONTA NÃO POSSUE SALDO.')
			return False
		else:
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


	def depositar(self, valor):	
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
class ContaCorrente(Conta):	
	def __init__(self, numero, cliente, limite=500.00, limite_saques=3):
		super().__init__(numero, cliente)
		self._limite = limite
		self._limite_saques = limite_saques
		self._numero_saques = 0
	
	def sacar(self, valor):	
		saldo = self.saldo
		if saldo <= 0.00:
			print(f'   A CONTA NÃO POSSUE SALDO.')
			return False
		else:
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


