# from persistencia.PersistenciaLocalTurisico import *
from model import LocalTuristico as lc

from persistencia.banco import banco as b
from persistencia.DAO import DAOLocalTuristico as d

banco = b.Banco()
dao = d.DAOLocalTuristico()

# persist = PersisnciaLocalTuristico()

class LocalTuristicoController:
    def adicionarLocalTuristico(self, lt):
        lt1 = lc.LocalTuristico(None, lt[0], lt[1], lt[2])
        response = dao.inserir_local_turistico(lt1)
        
        if response == True:
            #verificar se precisa retorar msm o local
            return True
        else:
            return False

    def deletarLocalTuristico(self, id_local):
        return dao.exclui_local_turistico(id_local)

    def procuraLocalPorNome(self, nome_local):
        print(nome_local)
        
        res = dao.procura_local_turistico_por_nome(nome_local)
        return res

    def retornaTodosLocais(self):
        res = dao.retornaTodosLocais()
        return res
    
    def retornaTodosLocaisEAtr(self):
        res = banco.retornaTodosLocaisEAtr()
        return res

    def retornarAvalsLocal(self, ltId):
        res = banco.recupera_todas_avaliacoes_local(ltId)
        if res == False: return []

        return res