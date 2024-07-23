import banco as b

banco = b.Banco()
banco.cria_tabela_usuario()
banco.cria_tabela_turismo()

#banco.insere_usuario([("Rodrigo", "rodrigo@zonzin.com", "taylorswift123", 1)])
#banco.insere_usuario([("Almada", "luis@almada.com", "rickandmorty", 1)])
#banco.insere_usuario([("Elias", "elias@mendes.com", "geoElias", 1)])

#banco.inserir_local_turistico(["DCOMP", "Av. do Bengo, 4125, SJDR", "Campus Tancredo Never"])
#banco.inserir_local_turistico(["Maria Fumaça", "Av. Centro, 123, SJDR", "Venha ver a Maria Fumaça"])
#banco.inserir_local_turistico(["Igreja do Carmo", "Av. Centro, 456, SJDR", "Actiones praejudiciales in Dei"])

print(banco.procura_usuario_login("rodrigozonzin.com"))

banco.commit()

