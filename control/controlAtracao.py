from model import AtracaoTuristica as at
from persistencia.banco import banco as b
from persistencia.DAO import DAOAtracao as d

banco = b.Banco()
dao = d.DAOAtracao()

class AtracaoTuristicaController:
    def adicionarAtracaoTuristico(self, atr):
        atr = at.AtracaoTuristica(None, atr[0], atr[1], atr[2])
        response = dao.insere_atracao(atr)
        
        if response == True:
            #verificar se precisa retorar msm o local
            return True
        else:
            return False

    def deletarAtracaoTuristico(self, id_atracao):
        return dao.exclui_atracao_turistica(id_atracao)

    def procuraAtracaoPorNome(self, nome_local):
        res = dao.procura_atracao_turistica_por_nome(nome_local)
        return res

    def retornaTodasAtracoes(self):
        res = dao.seleciona_todas_atracoes()
        return res
    
    #tem q ir pro control de Avaliacao
    def retornarAvalsAtracao(self, atId):
        res = banco.recupera_todas_avaliacoes_local(atId)
        if res == False: return []

        return res