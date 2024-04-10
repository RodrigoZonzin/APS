#contém as classes que recebem as solicitações feitas pelos usuários na visão e executam os casos de uso do software, 
#seja processar cálculos, combinar dados para estatísticas, 
#ou solicitar que a persistência recupere ou grave dados.
from antigos.modelo import *
from persistencia.persistencia import *
from persistencia.PersistenciaUsuarioNormal import PersistenciaUsuario as pu

from model import UsuarioNormal as un
#from model import UsuarioAdm as ua
from model import LocalTuristico as lc

class LocalTuristicoController:
    def __init__(self):
        pass

    def adicionarLocalTuristico(id, nome, endereco, descricao):
        localT = lc.LocalTuristico(id, nome, endereco, descricao)
        gravarLocalTuristico(localT)
        
        return localT

    def buscarLocalTuristicoID(id_local):
        local = showLocalTuristicoId(id_local)
        local = lc.LocalTuristico(local['ID'], local['Nome'], local['Endereco'], local['Descricao'])
       
        return local
    
    def buscarLocalTuristicoNome(nome_local):
        local = showLocalTuristicoNome(nome_local)
        if local != None:
            local = lc.LocalTuristico(local['ID'], local['Nome'], local['Endereco'], local['Descricao'])
       
        return local
    
    def apagarLocalTuristico(id_local):
        return deletarLocalTuristico(id_local)
    
    def alterarInfo(id_local, nome, endereco, descricao):
        alterarLocalTuristico(id_local, nome, endereco, descricao)


class UsuarioController:
    def __init__(self):
        pass

    #Cadastrar
    def adicionar_usuario(nome, login, senha):
        user = un.UsuarioNormal(nome, login, senha, False)
        insereUsuario(user) #N estou usando a persistenciaUsuario, pois estava dando erro por algum motivo
        
        return user

    def buscar_usuario(login):
        return showUsuario(login)

    def apagar_usuario(login):
        deletarUsuario(login)

    def fazer_login(Login,Senha):
        user = login(Login,Senha)
        #Verifica se o usuario existe
        if user != None:
            user = un.UsuarioNormal(user['Nome'], user['Login'], user['Senha'], user['isAdmin'])
        
        return user


"""class AtracaoTuristicaController:
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
        pass"""