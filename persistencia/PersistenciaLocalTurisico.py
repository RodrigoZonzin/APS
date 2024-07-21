import model.LocalTuristico
import json
from banco.banco import *

class PersisnciaLocalTuristico():

    '''def __init__(self, usuario):
        self.nomeArquivo = 'ArquivoPersistenciaLocalTuristico.csv'

    def criaArquivoPersistencia(self):
        self.arq_persistencia = pd.DataFrame(columns = ['id', 'nome', 'endereco', 'descricao'])

        self.arq_persistencia.to_csv(self.nomeArquivo, index=False)'''

    def inserirLocal(self, LT: model.LocalTuristico): 
        LT_tuple = (LT.nome, LT.endereco, LT.descricao)
        return inserir_local_turistico([LT_tuple]); 

    """
    def inserirLocal(self, LT):
        try:
            res = self.procuraLocalPorId(LT.id)
            if res != False:
                print('Local ja esta no banco de dados')
                return 400 #arrumar esses returns
            else:
                #Define o caminho do 'banco' e cria uma lista para receber os objetos JSON
                filename = './banco.json'
                listObj = []

                #Abre o arquivo e armazena os objetos JSON dentro da lista
                with open(filename) as fp:
                    listObj = json.load(fp)

                #Define-se os novos dados
                novoLocalTuristico = {
                    "ID": LT.id,
                    "Nome": LT.nome,
                    "Endereco": LT.endereco,
                    "Descricao": LT.descricao
                }
                
                #Adiciona os novos dados da lista de objetos JSON
                listObj.append(novoLocalTuristico)

                #Abre o arquivo porém agora para escrita, utiliza a função json.dump que serializa
                #o meu novo dado, permitindo que ele possa ser recolocado dentro do meu JSON
                with open(filename, 'w') as json_file:
                    json.dump(
                        listObj, 
                        json_file,
                        indent=4,
                        separators=(',',': ')
                    )
                    
                return True

        except:
            print('Erro ao inserir local turistico')
            return False
    """

    def procuraLocalPorId(self, id): 
        resposta_banco = procura_local_turistico_por_id(); 
        if resposta_banco  

    def procuraLocalPorId(self, id):
        filename = './banco.json'
        listObj = []

        with open(filename) as fp:
            listObj = json.load(fp)
        
        #Percorre todo o banco e verifica se um local com o id informado ja existe
        for i in listObj:
            if str(i['ID']) == str(id):
                return i
        
        #Retorna False se o local não esta no banco
        return False

    def deletarLocalTuristico(self, id):
        res = self.procuraLocalPorId(id)
        if res != False:
            #O elemento buscado existe no banco
            filename = './banco.json'
            listObj = []

            with open(filename) as fp:
                listObj = json.load(fp)

            #O res aqui contém as infos do local que se deseja apagar
            listObj.remove(res)

            #Reescrevendo o arquivo, já sem o que foi apagado
            with open(filename, 'w') as json_file:
                json.dump(
                    listObj, 
                    json_file,
                    indent=4,
                    separators=(',',': ')
                )

            return True
        
        else:
            print('Local n existe no banco')
            return False

            
    def procuraLocalPorNome(self, nome):
        filename = './banco.json'
        listObj = []
        listaLocais = []

        with open(filename) as fp:
            listObj = json.load(fp)
        
        for i in listObj:
            if str(i['Nome']) == str(nome):
                listaLocais.append(i)
        
        if len(listaLocais) > 0:
            return listaLocais
        else:
            return False