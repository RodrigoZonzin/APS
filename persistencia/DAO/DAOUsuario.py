from DAO import DAO
import banco.banco as b
import model.Usuario as u

class DAOUsuario(DAO):
    def __init__(self):
        super().__init__()
        self.banco = b.Banco()

    
    def create(self):
        try:
            return True if self.banco.cria_tabela_usuario() else False
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

    def update(self, user_alterar):
        user_alterar

    def delete(self, id):
        try:
            login_usuario = self.banco.recupera_usuario_id(id)[2]       #[2] corresponde ao login na tupla
            self.banco.excluir_usuario(login= login_usuario)

            return True
        except: 
            return False

    def search_id(self, usuario_id):
        try:
            return True if self.banco.recupera_usuario_id(usuario_id) else False
        except: 
            return False
        