import pandas as pd
import model.LocalTuristico


class PersisnciaLocalTuristico():

    def __init__(self, usuario):
        self.nomeArquivo = 'ArquivoPersistenciaLocalTuristico.csv'

    def criaArquivoPersistencia(self):
        self.arq_persistencia = pd.DataFrame(columns = ['id', 'nome', 'endereco', 'descricao'])

        self.arq_persistencia.to_csv(self.nomeArquivo, index=False)

    def insereLocal(self, localTuristico):
        self.df_persistencia = pd.read_csv(self.nomeArquivo)

        tupla = {
            "id": localTuristico.id,
            "nome": localTuristico.nome,
            "login": localTuristico.endereco,
            "senha": localTuristico.senha,
            "descricao": localTuristico.descricao
        }

        #add tupla (id, ... , descricao) à ultima linha do arquivo
        self.df_persistencia = self.df_persistencia.append(tupla, ignore_index=True)

        #salva de novo
        self.df_persistencia.to_csv(self.nomeArquivo, index=False)

    def procuraLocalPorNome(self, nome):
        self.df_persistencia = pd.read_csv(self.nomeArquivo)

        #problema se retornar None
        #deve ser resolvido quando houver tempo
        return self.df_persistencia.iloc[self.df_persistencia['nome'] == nome]
    
    def procuraLocalPorId(self, nome):
        self.df_persistencia = pd.read_csv(self.nomeArquivo)

        #problema se retornar None
        #deve ser resolvido quando houver tempo
        return self.df_persistencia.iloc[self.df_persistencia['nome'] == nome]