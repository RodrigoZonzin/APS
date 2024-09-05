#import banco as b
from . import banco as b

def iniciaBd():
    banco = b.Banco()
    banco.cria_tabela_usuario()
    banco.cria_tabela_localT_atrc()
    banco.cria_tabela_Avaliacao()
    

    #banco.insere_usuario([("Rodrigo", "rodrigo@zonzin.com", "taylorswift123", 1)])
    #banco.insere_usuario([("Almada", "luis@almada.com", "rickandmorty", 1)])
    #banco.insere_usuario([("Elias", "elias@mendes.com", "geoElias", 1)])
    # banco.insere_usuario([("a", "a", "a", 1)])
    # banco.insere_usuario([("b", "b", "b", 0)])
    #
    # banco.inserir_localT_Atr(["DCOMP", "Av. do Bengo, 4125, SJDR", "Campus Tancredo Never"], 1)
    # banco.inserir_localT_Atr(["Maria Fumaça", "Av. Centro, 123, SJDR", "Venha ver a Maria Fumaça"], 1)
    #banco.inserir_local_turistico(["Igreja do Carmo", "Av. Centro, 456, SJDR", "Actiones praejudiciales in Dei"])
    #
    #print(banco.procura_usuario_login("rodrigozonzin.com"))
    #banco.fazer_login('a', 'a')

    #id_avaliacao, id_usuario, nota, id_local_turistico, data, comentario)
    # banco.insere_avaliacao([1, 5, 1, '2024-05-23', "Muito Bom memso PArabens Eh isso ai!"])
    # banco.insere_avaliacao([1, 5, 1, '2024-05-28', "Bom demaiiiiis memso PArabens Eh isso ai!"])
    # banco.insere_avaliacao([100, 1, 2, '2024-05-23', "Muito Ruim!"])

    #banco.insere_avaliacao([
    #    (1, 5, 1, '2024-05-23', "Muito Bom memso PArabens Eh isso ai!"),
    #    (2, 5, 1, '2024-05-28', "Bom demaiiiiis memso PArabens Eh isso ai!"),
    #    (2, 1, 1, '2024-05-23', "Muito Ruim!")])
    

    
    banco.commit()

#iniciaBd()