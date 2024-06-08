import pandas as pd
import json


class PersistenciaUsuario():
    '''def __init__(self):
        self.nomeArquivo = 'ArquivoPersistenciaUsuarioNormal.csv'

    def criaArquivoPersistencia(self):
        self.arq_persistencia = pd.DataFrame(columns = ['id', 'nome', 'login', 'senha', 'isAdmin'])

        self.arq_persistencia.to_csv(self.nomeArquivo, index=False)'''

    def insereUsuario(self, user):
        #Define o caminho do 'banco' e cria uma lista para receber os objetos JSON
        filename = './bancoUsuario.json'
        listObj = []

        #Abre o arquivo e armazena os objetos JSON dentro da lista
        with open(filename) as fp:
            listObj = json.load(fp)

        #Define-se os novos dados
        novoUsuario = {
            "Nome": user.nome,
            "Login": user.login,
            "Senha": user.senha,
            'isAdmin': user.isAdmin
        }
        
        #Adiciona os novos dados da lista de objetos JSON
        listObj.append(novoUsuario)

        #Abre o arquivo porém agora para escrita, utiliza a função json.dump que serializa
        #o meu novo dado, permitindo que ele possa ser recolocado dentro do meu JSON
        with open(filename, 'w') as json_file:
            json.dump(
                listObj, 
                json_file,
                indent=4,
                separators=(',',': ')
            )

    def fazerLogin(self, login, senha):
        with open("./bancoUsuario.json", 'r') as arquivo:
            bancoDados = json.load(arquivo)
    
        for usuario in bancoDados:
            if usuario["Login"] == login and usuario["Senha"] == senha:
                return usuario
        
        return None

    '''def procuraUsuarioPorLogin(self, login):
        self.df_persistencia = pd.read_csv(self.nomeArquivo)

        #problema se retornar None
        #deve ser resolvido quando houver tempo
        return self.df_persistencia.iloc[self.df_persistencia['login'] == login]
    
    def procuraUsuarioPorId(self, id):
        self.df_persistencia = pd.read_csv(self.nomeArquivo)

        #problema se retornar None
        #deve ser resolvido quando houver tempo
        return self.df_persistencia.iloc[self.df_persistencia['id'] == id]'''
