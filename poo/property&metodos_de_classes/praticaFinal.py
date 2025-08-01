#Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
#Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta.
#Crie duas instâncias da classe e imprima essas instâncias.
#Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. 
#Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
#Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
#Crie uma instância da classe e imprima o valor da propriedade titular.

class ContaBancaria:
    contas = []

    
    def __init__(self, titular='', saldo=0.0, ativo=False):
        self._titular = titular
        self._saldo = saldo
        self._ativo = ativo
        ContaBancaria.contas.append(self)

    def __str__(self):
        return f"{self._titular.ljust(25)} | {self._saldo}"
    
    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

    @classmethod
    def ativar_conta(cls, titular):
        for conta in cls.contas:
            if conta._titular == titular:
                conta._ativo = True
                return conta._ativo
        return False
    
conta1 = ContaBancaria("Lucas", 10.00, True)
conta2 = ContaBancaria("Gabriel", 100000.0)



for cont in ContaBancaria.contas:
    print(cont)


print(conta2._ativo)
ContaBancaria.ativar_conta("Gabriel")
print(conta2._ativo)

print(conta1._titular)


##Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. 
#Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
#Crie um método de classe para a conta ClienteBanco.

class ClienteBanco:
    clientes = []


    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancaria(titular, saldo_inicial)
        return conta

cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Backend")
cliente2 = ClienteBanco("Luiza", 25, "Rua B", "987.654.321-01", "Estudante")
cliente3 = ClienteBanco("Vinny Neves", 40, "Rua C", "111.222.333-44", "Frontend")


    
# Exemplo de uso do método de classe
conta_cliente1 = ClienteBanco.criar_conta("Ana", 2000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")
    

        