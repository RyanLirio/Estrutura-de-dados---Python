atletas = [
    ["Maria Silva", 1.75, 65],
    ["João Santos", 1.80, 72],
    ["Ana Pereira", 1.68, 58],
    ["Pedro Oliveira", 1.92, 85],
    ["Carlos Lima", 1.85, 78],
    ["Beatriz Souza", 1.70, 60],
    ["Fernanda Costa", 1.62, 55],
    ["Lucas Almeida", 1.88, 82],
    ["Rafaela Gomes", 1.74, 63],
    ["Gustavo Ferreira", 1.90, 88],
    ["Larissa Rocha", 1.66, 57],
    ["Henrique Nunes", 1.83, 76],
    ["Juliana Martins", 1.72, 59],
    ["Ricardo Carvalho", 1.86, 80],
    ["Sofia Alves", 1.64, 54],
    ["Matheus Ribeiro", 1.89, 84],
    ["Camila Duarte", 1.69, 61],
    ["Gabriel Monteiro", 1.77, 73],
    ["Eduarda Farias", 1.71, 62],
    ["Thiago Mendes", 1.84, 79],
]
 
tupla_atletas = []
#tupla_atletas = tuple(atletas)
for atleta in atletas:
    nome = atleta[0]
    altura = atleta[1]
    peso = atleta[2]
    tupla_atleta = (nome, altura, peso)
    tupla_atletas.append(tupla_atleta)

print(tupla_atletas)