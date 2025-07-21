atletas = [
    ("Maria Silva", 1.75, 65),
    ("João Santos", 1.80, 72),
    ("Ana Pereira", 1.68, 58),
    ("Pedro Oliveira", 1.92, 85),
    ("Carlos Lima", 1.85, 78),
    ("Beatriz Souza", 1.70, 60),
    ("Fernanda Costa", 1.62, 55),
    ("Lucas Almeida", 1.88, 82),
    ("Rafaela Gomes", 1.74, 63),
    ("Gustavo Ferreira", 1.90, 88),
    ("Larissa Rocha", 1.66, 57),
    ("Henrique Nunes", 1.83, 76),
    ("Juliana Martins", 1.72, 90),
    ("Ricardo Carvalho", 1.86, 80),
    ("Sofia Alves", 1.64, 54),
    ("Matheus Ribeiro", 1.89, 84),
    ("Camila Duarte", 1.69, 81),
    ("Gabriel Monteiro", 1.77, 73),
    ("Eduarda Farias", 1.71, 62),
    ("Thiago Mendes", 1.84, 79),
]

#atletas_sobrepeso = []
#for atleta in atletas:
#    nome, altura, peso = atleta
#    imc = peso / (altura ** 2)  # Cálculo do IMC
#    if imc > 25:  # Considerando sobrepeso IMC > 25
#        atletas_sobrepeso.append((nome, "Sobrepeso"))
#    else:
#        atletas_sobrepeso.append((nome, "Peso normal"))

#print(f"Atletas com sobrepeso: {atletas_sobrepeso}")

# Classificação dos atletas com base no IMC
classificacao_imc = [
    (atleta[0], "Sobrepeso" if (atleta[2] / (atleta[1] ** 2)) > 25 else "Peso Normal")
    for atleta in atletas
]

# Impressão do resultado
print("Classificação dos atletas:")
print(classificacao_imc)