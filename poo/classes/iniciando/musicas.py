class Musica:
    nome = ""
    artista = ""
    duracao = 0.0

metamorfose = Musica()
metamorfose.nome = "Metamorfose Ambulante"
metamorfose.artista = "Raul Seixas"
metamorfose.duracao = 2.34

evidencias = Musica()
evidencias.nome = "Evidências"
evidencias.artista = "Chitãozinho e Xororó"
evidencias.duracao = 4.39

aquarela = Musica()
aquarela.nome = "Aquarela"
aquarela.artista = "Toquinho"
aquarela.duracao = 3.41

musicas = [metamorfose, evidencias, aquarela]


for musica in musicas:
    print(f"Músicas: {vars(musica)}")
