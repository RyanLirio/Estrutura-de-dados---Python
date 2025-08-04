#Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo,
#autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

class Livro:
    livros = []
    def __init__(self, titulo="", autor="", ano_publicacao=0000, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel
        Livro.livros.append(self)

    #Na classe Livro, adicione um método especial str
    #que retorna uma mensagem formatada com o título,

    def  __str__(self):
        return f"Titulo: {self.titulo.ljust(20)} | Autor: {self.autor.ljust(20)} | Ano: {self.ano_publicacao}"
    
    #Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False.
    #Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
            return "O livro estava disponível. Boa Leitura!"
        else:
            return "O livro não está dísponivel. Tente voltar outro dia!"
        
#autor e ano de publicação do livro. Crie duas instâncias
#da classe Livro e imprima essas instâncias.
livro1 = Livro("Dom kichute", "sancho pança", 2025, False)
livro2 = Livro("Dom casmurro", "Bob esponja", 2022, True)

print(livro2.emprestar())

for livro in Livro.livros:
    print(livro)

print(livro2.emprestar())