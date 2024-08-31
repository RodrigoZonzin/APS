class Avaliacao:
    def __init__(self, id, Autor, nota, LocalAtracao, dataHora, coment):
        self.id = id
        self.Autor = Autor
        self.nota = nota
        self.LocalAtracao = LocalAtracao
        self.dataHora = dataHora
        self.coment = coment

    # Métodos retorna
    def retornaid(self):
        return self.id

    def retornaidAutor(self):
        return self.loginAutor

    def retornanota(self):
        return self.nota

    def retornaidLocalAtracao(self):
        return self.idLocalAtracao

    def retornadataHora(self):
        return self.dataHora

    def retornacoment(self):
        return self.coment

    # Métodos altera
    def alteraid(self, value):
        self.id = value

    def alteraloginAutor(self, value):
        self.loginAutor = value

    def alteranota(self, value):
        self.nota = value

    def alteraidLocalAtracao(self, value):
        self.idLocalAtracao = value

    def alteradataHora(self, value):
        self.dataHora = value

    def alteracoment(self, value):
        self.coment = value
