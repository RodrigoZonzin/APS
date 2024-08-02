from persistencia.banco import banco as b

banco = b.Banco()

class AvaliacaoController:
    def adicionar_avaliacao(self, aval):
        res = banco.insere_avaliacao(aval)
        return res

    def apagar_avaliacao(self, id):
        res = banco.exclui_avaliacao_id(id)
        return res
    
    def retornaTodasAvals(self):
        res = banco.retornaTodasAvals()
        
        if res == False: res = []

        return res