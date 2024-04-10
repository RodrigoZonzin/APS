import pandas as pd


class PersistenciaUsuario():

    def __init__(self):
        self.nomeArquivo = 'ArquivoPersistenciaUsuarioNormal.csv'

    def criaArquivoPersistencia(self):
        self.arq_persistencia = pd.DataFrame(columns = ['id', 'nome', 'login', 'senha', 'isAdmin'])

        self.arq_persistencia.to_csv(self.nomeArquivo, index=False)

    def insereUsuario(self, usuario):
        self.df_persistencia = pd.read_csv(self.nomeArquivo)

        tupla = {
            #"id": usuario.id,
            "nome": usuario.nome,
            "login": usuario.login,
            "senha": usuario.senha,
            "isAdmin": usuario.isAdmin
        }

        #add tupla (id, ... , isAdmin) à ultima linha do arquivo
        self.df_persistencia = self.df_persistencia.append(tupla, ignore_index=True)

        #salva de novo
        self.df_persistencia.to_csv(self.nomeArquivo, index=False)

    def procuraUsuarioPorLogin(self, login):
        self.df_persistencia = pd.read_csv(self.nomeArquivo)

        #problema se retornar None
        #deve ser resolvido quando houver tempo
        return self.df_persistencia.iloc[self.df_persistencia['login'] == login]
    
    def procuraUsuarioPorId(self, id):
        self.df_persistencia = pd.read_csv(self.nomeArquivo)

        #problema se retornar None
        #deve ser resolvido quando houver tempo
        return self.df_persistencia.iloc[self.df_persistencia['id'] == id]
