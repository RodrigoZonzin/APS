# from persistencia.PersistenciaLocalTurisico import *
from model import LocalTuristico as lc

from persistencia.banco import banco as b

banco = b.Banco()

# persist = PersisnciaLocalTuristico()

class LocalTuristicoController:
    def adicionarLocalTuristico(self, lt):
        response = banco.inserir_localT_Atr(lt, 0)
        
        if response == True:
            #verificar se precisa retorar msm o local
            return True
        else:
            return False

    def deletarLocalTuristico(self, id_local):
        return banco.exclui_localT_Atr(id_local)

    def procuraLocalPorNome(self, nome_local):
        res = banco.procura_localT_Atr_nome(nome_local)
        return res

    def retornaTodosLocais(self):
        res = banco.retornaTodosLocaisOuAtr(0)
        return res
    
    def retornaTodosLocaisEAtr(self):
        res = banco.retornaTodosLocaisEAtr()
        return res

    #tem q ir pro control de Avaliacao
    def retornarAvalsLocal(self, ltId):
        res = banco.recupera_todas_avaliacoes_local(ltId)
        if res == False: return []

        return res


    '''def buscarLocalTuristicoID(id_local):
        local = showLocalTuristicoId(id_local)
        local = lc.LocalTuristico(local['ID'], local['Nome'], local['Endereco'], local['Descricao'])
       
        return local
    
    
    def alterarInfo(id_local, nome, endereco, descricao):
        alterarLocalTuristico(id_local, nome, endereco, descricao)'''