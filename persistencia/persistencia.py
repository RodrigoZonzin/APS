#contém as classes que são responsáveis por gravar e recuperar os dados dos 
#objetos das classes da camada de modelo em arquivos ou BD;

from os import path
import json
from antigos.modelo import *

def gravarLocalTuristico(LT : Turismo):

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
        json.dump(listObj, json_file,
                            indent=4,
                            separators=(',',': '))

def showLocalTuristicoId(id_local):
    # Carregar os dados do arquivo JSON
    with open("./banco.json", "r") as arquivo:
        locais_turisticos = json.load(arquivo)

    # Buscar o local turístico pelo ID
    for local in locais_turisticos:
        if str(local["ID"]) == str(id_local):
            return local
    
    # Se o ID não for encontrado, retorna None
    return None

def showLocalTuristicoNome(nome_local):
     # Carregar os dados do arquivo JSON
    with open("./banco.json", "r") as arquivo:
        locais_turisticos = json.load(arquivo)

    # Buscar o local turístico pelo ID
    for local in locais_turisticos:
        if str(local["Nome"]) == str(nome_local):
            return local
    
    # Se o nome não for encontrado, retorna None
    return None

def deletarLocalTuristico(id_local):
    control = 0
    
    # Carregar os dados do arquivo JSON
    with open("./banco.json", "r") as arquivo:
        locais_turisticos = json.load(arquivo)

    # Iterar sobre os locais turísticos e remover o local com o ID correspondente
    for local in locais_turisticos:
        if str(local["ID"]) == str(id_local):
            locais_turisticos.remove(local)
            control = 1
            break

    # A variavel control = 1 garante que o usuario foi encontrado. Se for 0, ent ele n foi encontrado
    if control == 1:
        # Escrever os dados atualizados no arquivo JSON
        with open("./banco.json", "w") as arquivo:
            json.dump(locais_turisticos, arquivo, indent=4)

        return True
    
    #Nesse caso, retorna False, ao n econtrar o usuario para deletar
    else:
        return False


def alterarLocalTuristico(id, nome, endereco, descricao):
    # Carregar os dados do arquivo JSON
    with open("./banco.json", "r") as arquivo:
        locais_turisticos = json.load(arquivo)

    # Iterar sobre os locais turísticos e remover o local com o ID correspondente
    for local in locais_turisticos:
        if str(local['ID']) == str(id):
            if nome != '':
                local['Nome'] = nome
            if endereco != '':
                local['endereco'] = endereco
            if descricao != '':
                local['descricao'] = descricao
            
            break

    # Escrever os dados atualizados no arquivo JSON
    with open("./banco.json", "w") as arquivo:
        json.dump(locais_turisticos, arquivo, indent=4)


def insereUsuario(user : Usuario):
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
        json.dump(listObj, json_file,
                            indent=4,
                            separators=(',',': '))


def login(login, senha):
    with open("./bancoUsuario.json", 'r') as arquivo:
        jsonObject = json.load(arquivo)
    
    for usuario in jsonObject:
        if usuario["Login"] == login and usuario["Senha"] == senha:
            return usuario
    
    return None


def showUsuario(login):
    # Carregar os dados do arquivo JSON
    with open("src/bancoUsuario.json", "r") as arquivo:
        usuarios = json.load(arquivo)

    # Buscar o usuario pelo login
    for usuario in usuarios:
        if str(usuario["Login"]) == str(login):
            return usuario
    
    # Se o login não for encontrado, retorna None
    return None


def deletarUsuario(login):
    # Carregar os dados do arquivo JSON
    with open("src/bancoUsuario.json", "r") as arquivo:
        usuarios = json.load(arquivo)

    # Iterar sobre os locais turísticos e remover o local com o ID correspondente
    for usuario in usuarios:
        if str(usuario["Login"]) == str(login):
            usuarios.remove(usuario)
            break

    # Escrever os dados atualizados no arquivo JSON
    with open("src/bancoUsuario.json", "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)