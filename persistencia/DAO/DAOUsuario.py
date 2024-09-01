from DAO import DAO
import banco.banco as b
import model.Usuario as u

class DAOUsuario(DAO):
    def __init__(self):
        super().__init__()
        self.banco = b.Banco()

    #(id_usuario, nome, login, senha, is_admin)
    def create(self, novo_u):
        try:
            dados = [(novo_u.id,
                      novo_u.nome,
                      novo_u.login,
                      novo_u.senha,
                      novo_u.isAdmin)]

            
            self.banco.insere_usuario(dados)

            return True
        except: 
            return False

    def read(self, id):
        try:
            tupla = self.banco.recupera_usuario_id(id)
            tupla_avaliacoes = self.banco.procura_avaliacao_usuario(id)
            usuario_consultado = u.Usuario(id   =   tupla[0],
                                           nome =   tupla[1],
                                           login=   tupla[2],
                                           senha=   tupla[4],
                                           is_admin=tupla[5],
                                           avals=   None)           #CONSULTAR ISSO AQUI COM O ALMADA
        
            return usuario_consultado
        except:
            return False

    def update():
        pass

    def delete(self, id):
        try:
            self.banco
        except: 
        

    def search():
        pass