from model.UsuarioNormal import UsuarioNormal
from model.UsuarioAdm import UsuarioAdm
from persistencia.persistencia import persistencia

#O register é so para o usuario normal, pois so um adm pode tornar outro usuario em adm
#ou seja, n tem como registra-lo diretamente como adm
def registrarUser(nome, login, senha, isAdmin=False, comentario=None, avaliacao=None):
    user = UsuarioNormal(nome, login, senha, isAdmin, comentario, avaliacao)
    #gravarUsuario(user)
    print()
    return user 