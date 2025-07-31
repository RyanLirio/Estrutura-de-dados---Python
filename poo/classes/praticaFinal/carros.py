#Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. 
# Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    
    carros = []

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)

    def __str__(self):
        return f"{self.modelo} | {self.cor} | {self.ano}"#exibe somente isso no print da variavel

uno = Carro("Uno Mille", "prata", 1997)

print(uno)


