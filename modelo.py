#Contém as classes que representam as entidades do programa e possuem os atributos que são os 
#dados dessas entidades e os métodos construtores, 
#getters e setters e que representam atributos calculados (por exemplo, total da venda). 
#Não pode haver nenhum método para imprimir, cadastrar, inserir, apagar, etc.;

class Turismo:
    def __init__(self, nome, endereco, descricao, ID):
        self._nome = nome
        self._endereco = endereco
        self._descricao = descricao
        self._ID = ID

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_endereco(self):
        return self._endereco

    def set_endereco(self, endereco):
        self._endereco = endereco

    def get_descricao(self):
        return self._descricao

    def set_descricao(self, descricao):
        self._descricao = descricao

    def get_ID(self):
        return self._ID

    def set_ID(self, ID):
        self._ID = ID

class AtracaoTuristica:
    def __init__(self, nome, tipo, horario_funcionamento, IDAtracao):
        self._nome = nome
        self._tipo = tipo
        self._horario_funcionamento = horario_funcionamento
        self._IDAtracao = IDAtracao

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo):
        self._tipo = tipo

    def get_horario_funcionamento(self):
        return self._horario_funcionamento

    def set_horario_funcionamento(self, horario_funcionamento):
        self._horario_funcionamento = horario_funcionamento

    def get_IDAtracao(self):
        return self._IDAtracao

    def set_IDAtracao(self, IDAtracao):
        self._IDAtracao = IDAtracao

class Comentario:
    def __init__(self, autor, id_autor, conteudo, data, id_referencia):
        self._autor = autor
        self._id_autor = id_autor
        self._conteudo = conteudo
        self._data = data
        self._id_referencia = id_referencia

    def get_autor(self):
        return self._autor

    def set_autor(self, autor):
        self._autor = autor

    def get_id_autor(self):
        return self._id_autor

    def set_id_autor(self, id_autor):
        self._id_autor = id_autor

    def get_conteudo(self):
        return self._conteudo

    def set_conteudo(self, conteudo):
        self._conteudo = conteudo

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def get_id_referencia(self):
        return self._id_referencia

    def set_id_referencia(self, id_referencia):
        self._id_referencia = id_referencia

class Avaliacao:
    def __init__(self, usuario, nota, id_data, id_referencia):
        self._usuario = usuario
        self._nota = nota
        self._id_data = id_data
        self._id_referencia = id_referencia

    def get_usuario(self):
        return self._usuario

    def set_usuario(self, usuario):
        self._usuario = usuario

    def get_nota(self):
        return self._nota

    def set_nota(self, nota):
        self._nota = nota

    def get_id_data(self):
        return self._id_data

    def set_id_data(self, id_data):
        self._id_data = id_data

    
    def get_id_referencia(self):
        return self._id_referencia

    def set_id_referencia(self, id_referencia):
        self._id_referencia = id_referencia

class RotaTuristica:
    def __init__(self, nome, locais, distancia_total):
        self._nome = nome
        self._locais = locais
        self._distancia_total = distancia_total

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_locais(self):
        return self._locais

    def set_locais(self, locais):
        self._locais = locais

    def get_distancia_total(self):
        return self._distancia_total

    def set_distancia_total(self, distancia_total):
        self._distancia_total = distancia_total


class Usuario:
    def __init__(self, nome, login, senha, isAdmin=False):
        self._nome = nome
        self._login = login
        self._senha = senha
        self._isAdmin = isAdmin

    def get_nome(self):
        return self._nome

    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def get_login(self):
        return self._login

    def set_login(self, novo_login):
        self._login = novo_login

    def get_senha(self):
        return self._senha

    def set_senha(self, nova_senha):
        self._senha = nova_senha

    def get_isAdmin(self):
        return self._isAdmin

    def set_isAdmin(self, novo_valor):
        self._isAdmin = novo_valor

    




