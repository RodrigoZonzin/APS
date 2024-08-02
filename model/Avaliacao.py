class Avaliacao:
    def __init__(self, idAutor, nota, idLocalAtracao, dataHora, coment, id=-1):
        self._id = id
        self._idAutor = idAutor
        self._nota = nota
        self._idLocalAtracao = idLocalAtracao
        self._dataHora = dataHora
        self._coment = coment

    # Métodos retorna
    def retorna_id(self):
        return self._id

    def retorna_idAutor(self):
        return self._loginAutor

    def retorna_nota(self):
        return self._nota

    def retorna_idLocalAtracao(self):
        return self._idLocalAtracao

    def retorna_dataHora(self):
        return self._dataHora

    def retorna_coment(self):
        return self._coment

    # Métodos altera
    def altera_id(self, value):
        self._id = value

    def altera_loginAutor(self, value):
        self._loginAutor = value

    def altera_nota(self, value):
        self._nota = value

    def altera_idLocalAtracao(self, value):
        self._idLocalAtracao = value

    def altera_dataHora(self, value):
        self._dataHora = value

    def altera_coment(self, value):
        self._coment = value
