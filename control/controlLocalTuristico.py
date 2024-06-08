from persistencia.PersistenciaLocalTurisico import *
from model import LocalTuristico as lc

persist = PersisnciaLocalTuristico()

class LocalTuristicoController:
    def adicionarLocalTuristico(self, id, nome, endereco, descricao):
        localT = lc.LocalTuristico(id, nome, endereco, descricao)
        response = persist.inserirLocal(localT)
        
        if response == True:
            #verificar se precisa retorar msm o local
            return localT
        else:
            return None

    def deletarLocalTuristico(self, id_local):
        return persist.deletarLocalTuristico(id_local)

    def procuraLocalPorNome(self, nome_local):
        local = persist.procuraLocalPorNome(nome_local)
        if local != False:
            #local é uma lista, ent preciso fazer esse if num for
            local = lc.LocalTuristico(local[0]['ID'], local[0]['Nome'], local[0]['Endereco'], local[0]['Descricao'])
       
        return local


    '''def buscarLocalTuristicoID(id_local):
        local = showLocalTuristicoId(id_local)
        local = lc.LocalTuristico(local['ID'], local['Nome'], local['Endereco'], local['Descricao'])
       
        return local
    
    
    def alterarInfo(id_local, nome, endereco, descricao):
        alterarLocalTuristico(id_local, nome, endereco, descricao)'''