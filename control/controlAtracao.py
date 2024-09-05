from model import AtracaoTuristica as at
from persistencia.banco import banco as b

banco = b.Banco()

class AtracaoTuristicaController:
    def adicionarAtracaoTuristico(self, at):
        response = banco.inserir_localT_Atr(at, 1)
        
        if response == True:
            #verificar se precisa retorar msm o local
            return True
        else:
            return False

    def deletarAtracaoTuristico(self, id_atracao):
        return banco.exclui_localT_Atr(id_atracao)

    def procuraAtracaoPorNome(self, nome_local):
        res = banco.procura_localT_Atr_nome(nome_local)
        return res

    def retornaTodasAtracoes(self):
        res = banco.retornaTodosLocaisOuAtr(1)
        return res
    
    #tem q ir pro control de Avaliacao
    def retornarAvalsAtracao(self, atId):
        res = banco.recupera_todas_avaliacoes_local(atId)
        if res == False: return []

        return res