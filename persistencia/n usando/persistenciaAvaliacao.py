import pandas as pd
from model import Avaliacao
from persistencia.banco import banco as banco

class PersistenciaAvaliacao():

    def insereAvaliacao(self, avaliacao):

        novaAvaliacao = (        
            avaliacao.retorna_id(),
            avaliacao.retorna_idAutor(),
            avaliacao.retorna_nota(),
            avaliacao.retorna_idLocalAtracao(),
            avaliacao.retorna_dataHora(),
            avaliacao.retorna_coment()
        )

        banco.insere_avaliacao([novaAvaliacao])
        banco.commit()

    def apagaAvaliacaoPorId(self, id):
        banco.exclui_avaliacao_id(id)


    #procura todas as avaliacoes de um dado usuario
    #retorna nome do usuario, comentario e nota
    #RESOLVER DEPOIS
    def procuraAvaliacaoUsuario(self, usuario): 
        pass
        #banco.procura_avaliacao_usuario(usuario.)

    def recuperaTodasAvaliacoesPorNome(self, nome): 
        banco.recupera_todas_avaliacoes_por_nome(nome)

