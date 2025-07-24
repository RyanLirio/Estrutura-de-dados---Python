class Restaurante:
    nome = ""
    categoria = ""
    ativo = False

restaurante_praca = Restaurante()

restaurante_praca.categoria = "Italiana"

print(restaurante_praca.nome)

if(restaurante_praca.ativo == False):
    print(f"O restaurante está desativado")
else:
    print(f"O restaurante está ativo")

categoria = restaurante_praca.categoria
print(categoria)

restaurante_praca.nome = "Bistrô"

restaurante_pizza = Restaurante()
restaurante_pizza.nome = "Pizza Place"
restaurante_pizza.categoria = "Fast Food"

if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food.')
else:
    print('A categoria não é Fast Food.')

restaurante_pizza.ativo = True

print(f"Nome: {restaurante_praca.nome}\nCategoria: {restaurante_pizza.categoria}")