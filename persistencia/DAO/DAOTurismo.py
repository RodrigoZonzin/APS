from DAO import DAO
import banco.banco as b
import model.LocalTuristico as lt

class DAOLocalTuristico(DAO):
    def __init__(self):
        super().__init__()
        self.banco = b.Banco()

    #retorna bool. True caso a conexão com o banco dê certo, False em caso contrário
    def create(self):
        try:
            return True if self.banco.cria_tabela_local_turistico() else False
        except: 
            return False

    #retorna um objeto Turismo ou Falso
    def read(self, id_local):
        try:
            tupla = self.banco.procura_local_turistico_por_id(id_local)
            
            lt_turismo = lt.LocalTuristico(  id          = tupla[0],
                                            nome        = tupla[1],
                                            endereco    = tupla[2],
                                            descricao   = tupla[3])
            return lt_turismo
        except: 
            return False
 
    def update():
        pass
    
    #deleta local turistico
    def delete(self, id_local):
        try: 
            return True if self.banco.exclui_local_turistico(id_local) else False
        except:
            return False

    def search():
        pass