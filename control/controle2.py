from model import UsuarioNormal as un
#from model import UsuarioAdm as ua
#from persistencia import persistencia as pers

#O register é so para o usuario normal, pois so um adm pode tornar outro usuario em adm
#ou seja, n tem como registra-lo diretamente como adm
def registrarUser(nome, login, senha, isAdmin=False, comentario=None, avaliacao=None):
    user = un.UsuarioNormal(nome, login, senha, isAdmin, comentario, avaliacao)
    #gravarUsuario(user)
    return user 