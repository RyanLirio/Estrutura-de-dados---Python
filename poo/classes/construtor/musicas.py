class Musica:
    musicas = []

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def listar_musicas():
        for msc in Musica.musicas:    
            print(f"\n{msc.nome} | {msc.artista} | {msc.duracao}")

metamorfose = Musica("Metamorfose Ambulante", "Raul Seixas", 2.34)
aquarela = Musica("Aquarela", "Toquinho", 3.41)

Musica.listar_musicas()