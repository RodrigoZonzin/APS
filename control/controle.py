#contém as classes que recebem as solicitações feitas pelos usuários na visão e executam os casos de uso do software, 
#seja processar cálculos, combinar dados para estatísticas, 
#ou solicitar que a persistência recupere ou grave dados.
from modelo import *
from persistencia.persistencia import *

class LocalTuristicoController:
    def __init__(self):
        pass

    def adicionarLocalTuristico(self, LocalTuristicoX):
        gravarLocalTuristico(LocalTuristicoX)

    def buscarLocalTuristicoID(self, id_local):
        return showLocalTuristico(id_local)
    
    def buscarLocalTuristicoNome(self, nome):
        pass
    
    def apagarLocalTuristico(self, id_local):
        deletarLocalTuristico(id_local)
    
    def alterarInfo(self,id_local, op):
        pass


class AtracaoTuristicaController:
    def __init__(self):
        pass

    def adicionar_atracao(self, nome, tipo, horario_funcionamento, id_atracao):
        pass

    def buscar_atracao(self, id_atracao):
        pass

    def apagar_atracao(self, id_atracao):
        pass


class ComentarioController:
    def __init__(self):
        pass

    def adicionar_comentario(self, autor, id_autor, conteudo, data, id_local):
        pass

    def buscar_comentario(self, id_local):
        pass

    def apagar_comentario(self, id_comentario):
        pass

class AvaliacaoController:
    def __init__(self):
        pass

    def adicionar_avaliacao(self, usuario, nota, id_local):
        pass

    def buscar_avaliacao(self, id_local):
        pass

    def apagar_avaliacao(self, id_avaliacao):
        pass

class RotaTuristicaController:
    def __init__(self):
        pass

    def adicionar_rota(self, nome, locais, distancia_total):
        pass

    def buscar_rota(self, id_rota):
        pass

    def apagar_rota(self, id_rota):
        pass

class UsuarioController:
    def __init__(self):
        pass

    #Cadastrar
    def adicionar_usuario(self, Usuario):
        gravarUsuario(Usuario)
        pass

    def buscar_usuario(self, login):
        return showUsuario(login)

    def apagar_usuario(self, login):
        deletarUsuario(login)

    def fazer_login(self,Login,Senha):
        return buscaUsuario(Login,Senha)