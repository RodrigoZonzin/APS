from persistencia.banco import banco as b
from model.Avaliacao import *
# from model.Usuario import *
from model.LocalTuristico import *
from model.AtracaoTuristica import *
from control.controlUser import UsuarioController
from control.controlLocalTuristico import LocalTuristicoController
from persistencia.DAO import DAOAvaliacao as dav

dao = dav.DAOAvaliacao()
banco = b.Banco()
controlU = UsuarioController()
controlLt = LocalTuristicoController()

class AvaliacaoController:
    def adicionar_avaliacao(self, aval):
        aval = Avaliacao(None, aval[0], aval[1], aval[2], aval[3], aval[4])
        res = dao.insere_avaliacao(aval)
        return res

    def apagar_avaliacao(self, id):
        res = dao.exclui_avaliacao_id(id)
        return res
    
    def apagar_todasAvals_user(self, login):
        res = dao.exclui_todas_avaliacoes_usuario(login)
        return res

    def apagar_todasAvals_localAtr(self, localAtr):
        res = dao.exclui_todasAval_localAtr(localAtr)
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

            user = controlU.buscar_usuario(i[4])
            lt = controlLt.procuraLocalPorNome(i[5])
            # if aux != False:
            #     if aux[1] == 0:
            #         lt = LocalTuristico(aux[0], aux[2], aux[3], aux[4])
            #     else:
            #         lt = AtracaoTuristica(aux[0], aux[2], aux[3], aux[4])

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