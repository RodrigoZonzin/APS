from persistencia.banco import banco as b
from model.Avaliacao import *
# from model.Usuario import *
from model.LocalTuristico import *
from control.controlUser import UsuarioController
from control.controlLocalTuristico import LocalTuristicoController

banco = b.Banco()
controlU = UsuarioController()
controlLt = LocalTuristicoController()

class AvaliacaoController:
    def adicionar_avaliacao(self, aval):
        res = banco.insere_avaliacao(aval)
        return res

    def apagar_avaliacao(self, id):
        res = banco.exclui_avaliacao_id(id)
        return res
    
    def retornaTodasAvals(self):
        res = banco.retornaTodasAvals()
        
        if res == False:
            print('vazio') 
            return []

        vet = []
        for i in res:
            user = None
            lt = None

            aux = controlU.buscar_usuario(i[4])
            user = controlU.criaUser(aux, 0)
            # if aux[4] == 0:
            #     user = UsuarioNormal(aux[0], aux[1], aux[2], aux[3], aux[4])
            # else:
            #     user = UsuarioAdm(aux[0], aux[1], aux[2], aux[3], aux[4])
            
            aux = controlLt.procuraLocalPorNome(i[5])
            if aux != False:
                lt = LocalTuristico(aux[0], aux[1], aux[2], aux[3])
            #Fazer controle de erros nessa parte
            vet.append(Avaliacao(
                i[0], 
                user, 
                i[1],
                lt, 
                i[2],
                i[3]
            ))


        return vet