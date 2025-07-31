# Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, 
# instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:

    clientes = []

    def __init__(self, nome, idade, sexo, prato_mais_pedido):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.prato_mais_pedido = prato_mais_pedido
        Cliente.clientes.append(self)
    
    def __str__(self):
        return f"{self.nome} | {self.idade} | {self.sexo} | {self.prato_mais_pedido}"
    
cliente_1 = Cliente("João", 32, "M", "Carbonara")
cliente_2 = Cliente("Maria", 22, "F", "Arroz com peixe branco")
cliente_3 = Cliente("Deyverson", 29, "M", "Bife a cavalo")
cliente_4 = Cliente("Lindamir", 32, "F", "Risoto de Funghi")

for cliente in Cliente.clientes:
    print(cliente)
