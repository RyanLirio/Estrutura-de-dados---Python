class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria): #usado pra definir entradas obrigatórias
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):#usado pra não ser necessário usar vars() pra mostrar o objeto
        return f"{self.nome} | {self.categoria}"
    
    def mostrar_rest():
        for rest in Restaurante.restaurantes:
            if(rest.ativo):
                status = "Ativo"
            else:
                status = "Desativado"
            print(f"{rest.nome} | {rest.categoria} | {status}")


restaurante_chines = Restaurante("Xaina_imbocs", "Xing-Ling")
restaurante_chines.ativo = True
restaurante_japones = Restaurante("Japax", "Japon")

Restaurante.mostrar_rest()