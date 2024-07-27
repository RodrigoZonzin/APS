from persistencia.PersistenciaUsuarioNormal import *
from model import UsuarioNormal as un
from model import Avaliacao as av
from persistencia.banco import banco as banco

persist = PersistenciaUsuario()

class UsuarioController:
    def __init__(self):
        pass

    #Cadastrar
    def adicionar_usuario(self, nome, login, senha):
        user = un.UsuarioNormal(nome, login, senha, False)
        persist.insereUsuario(user)

        dados = (nome, login, senha, 0)   
        #banco.insere_usuario(dados)

        return user

    def fazer_login(self, login, senha):
        user = persist.fazerLogin(login, senha)
        #user = banco.fazer_login(login, senha)
        print("usuario: ", user)

        #Verifica se o usuario existe
        if user != None:
            return un.UsuarioNormal(user['Nome'], user['Login'], user['Senha'], user['isAdmin'])
        
        return None

    #aval = (id, loginAutor, nota, idLocalAtracao, dataHora, coment)
    def fazerAvaliacao(self, user, aval: tuple): #user é um objeto da classe Usuario
        avaliacao = av.Avaliacao(*aval)

        #salvar no bd do usuario
        
        #atualizando o model do usuario
        user.fazerAval(avaliacao)

        
        return user

    def apagarAvaliacao(self, user, aval):
        #apagar no bd do usuario

        #atualizando o model do usuario
        user.apagarAval(aval)

        return user

    def buscar_usuario(login):
        #return showUsuario(login)
        pass

    def apagar_usuario(login):
        #deletarUsuario(login)
        pass