#contém as classes que implementam a interface gráfica com o usuário. 
#Essas classes só podem apresentar e obter dados de e para os usuários, 
#mas não são elas que executam os casos de uso do software;
from control.controle import *
from modelo import *

controladorLocalTuristico = LocalTuristicoController()
controladorUsuario = UsuarioController()

def main():
    menuGeral()

def menuGeral():
    op = int(input("\n1 - Adm\n2 - Usuario\nOpcao: "))
    menu(op)

def menu(Logica):

    #Administrador
    if(Logica == 1):
        print("\n\n__MENU ADMINISTRADOR__")
        op = -1
        while(op != 0):
            op = int(input("\n1 - Gerenciar Local Turistico\n2 - Gerenciar Usuarios\n0 - Sair\nOpcao: "))
            if(op == 1):
                AdmLocalTuristico()
            elif(op == 2):
                AdmUsuarios()



    #Usuario
    elif(Logica == 2):
        print("\n\n__MENU USUARIO__")
        op = -1
        while(op != 0):
            op = int(input("\n1 - Cadastrar-se\n2 - Buscar Local Turistico\n3 - Efetuar Login\n0 - Voltar\nOpcao: "))
            
            #Cadastrar Usuario
            if(op == 1):
                controladorUsuario.adicionar_usuario(catchInfoUsuario())
                print('Usuario cadastrado com sucesso !!!\n\n')
            
            #Buscar LocalTuristico
            elif(op == 2):
                IDBusca = input("\nDigite o ID: ")
                k = controladorLocalTuristico.buscarLocalTuristicoID(IDBusca)
                imprimeLocalTuristico(k)
                print("\n\n")

            #Fazer login
            elif(op == 3):
                login = input("Login: ")
                senha = input("Senha: ")
                condicao = controladorUsuario.fazer_login(login,senha)
                if(condicao == None):
                    print("Usuario nao cadastrado !!! \n\n")
                else:
                    print("Login Efetuado com Sucesso !!!\n\n")
                    menuUsuarioCadastrado(login)


def menuUsuarioCadastrado(login):
    opcao = int(input("\n1 - Acessar Perfil\n2 - Gerenciar Avaliacoes\n3 - Gerenciar Comentarios\nOpcao: "))

    if(opcao == 1):
        AcessarPerfil(login)
    elif(opcao == 2):
        gerenciarAvaliacao()
    elif(opcao == 3):
        gerenciaComentario()

def AdmUsuarios():
    opcao = int(input("\n1 - Buscar Usuario\n2 - Apagar Usuario\n0 - Voltar\nOpcao: "))
    if(opcao == 1):
        login = input("\nDigite o Login do usuario: ")
        u = controladorUsuario.buscar_usuario(login)
        imprimeUsuario(u)
        print("\n\n")
    elif(opcao == 2):
        login = input("\nDigite o Login do usuario: ")
        controladorUsuario.apagar_usuario(login)
        print('Usuario removido com sucesso !!!\n\n')

def AdmLocalTuristico():
    print("\n\n__MENU LOCAL TURISTICO__")
    opcao = int(input("1 - Adicionar Local Turistico\n2 - Buscar Local Turistico\n3 - Apagar Local Turistico\n4 - Alterar Local Turistico\n0 - Sair\nOpcao: "))
    if(opcao == 1):
        controladorLocalTuristico.adicionarLocalTuristico(catchInfoLocalTuristico());
        print('Local Turistico adicionado com sucesso !!!\n\n')
    elif(opcao == 2):
        opcaoBusca = int(input("\n1 - Buscar Local Turistico\n2 - Buscar Local Turistico por ID\nOpcao: "))
        if(opcaoBusca == 1):
            controladorLocalTuristico.buscarLocalTuristico(catchInfoLocalTuristico)
        elif(opcaoBusca == 2):
            IDBusca = input("\nDigite o ID: ")
            k = controladorLocalTuristico.buscarLocalTuristicoID(IDBusca)
            imprimeLocalTuristico(k)
            print("\n\n")
            
    elif(opcao == 3):
        IDBusca = input("\nDigite o ID: ")
        controladorLocalTuristico.apagarLocalTuristico(IDBusca);
        print('Local Turistico removido com sucesso !!!\n\n')

    #Para alteração do local turistico primeiro a gente apaga e depois adiciona novamente
    elif(opcao == 4):
        IDBusca = input("\nDigite o ID do Local a ser Alterado: ")
        k = controladorLocalTuristico.buscarLocalTuristicoID(IDBusca)
        op = int(input("\n1 - Novo ID\n2 - Novo Nome\n3 - Novo Endereco\n4 - Nova Descricao\nOpcao: "))
        if(op == 1):
            novoId = input("Digite o novo ID: ")
            localTuristicoAlterado = Turismo(k.get("Nome"),k.get("Endereco"),k.get("Descricao"),novoId)
            controladorLocalTuristico.apagarLocalTuristico(IDBusca)
            controladorLocalTuristico.adicionarLocalTuristico(localTuristicoAlterado)
            print("ID Alterado com Sucesso !!! \n\n")
        elif(op == 2):
            novoNome = input("Digite o novo Nome: ")
            localTuristicoAlterado = Turismo(novoNome,k.get("Endereco"),k.get("Descricao"),k.get("ID"))
            controladorLocalTuristico.apagarLocalTuristico(IDBusca)
            controladorLocalTuristico.adicionarLocalTuristico(localTuristicoAlterado)
            print("Nome alterado com Sucesso !!! \n\n")
        elif(op == 3):
            novoEndereco = input("Digite o novo endereco: ")
            localTuristicoAlterado = Turismo(k.get("Nome"),novoEndereco,k.get("Descricao"),k.get("ID"))
            controladorLocalTuristico.apagarLocalTuristico(IDBusca)
            controladorLocalTuristico.adicionarLocalTuristico(localTuristicoAlterado)
            print("Endereco alterado com sucesso !!! \n\n")
        elif(op == 4):
            novaDescricao = input("Digite a nova descricao: ")
            localTuristicoAlterado = Turismo(k.get("Nome"),k.get("Endereco"),novaDescricao,k.get("ID"))
            controladorLocalTuristico.apagarLocalTuristico(IDBusca)
            controladorLocalTuristico.adicionarLocalTuristico(localTuristicoAlterado)
            print("Descricao alterada com sucesso !!! \n\n")



def imprimeLocalTuristico(Objeto):
    print("\n\nLOCAL TURISTICO:")
    print(f'\nNome: {Objeto.get("Nome")}\nEndereco: {Objeto.get("Endereco")}\nDescricao: {Objeto.get("Descricao")}')

def imprimeUsuario(Objeto):
    print("\n\nUsuario: ")
    print(f'\nNome: {Objeto.get("Nome")}\nLogin: {Objeto.get("Login")}\nSenha: {Objeto.get("Senha")}\nisAdmin: {Objeto.get("isAdmin")}')

def catchInfoLocalTuristico():
    nome = input("Nome do Local Turistico: ")
    localizacao = input("Localizacao do Local Turistico: ")
    descricao = input("Pequena descrição do local Turistico: ")
    IDLocal = input("Defina o ID do Local: ")
    NovoLocalTuristico = Turismo(nome, localizacao, descricao, IDLocal)
    return NovoLocalTuristico

def catchInfoUsuario():
    nome = input("Nome do Usuario: ")
    login = input("Login do Usuario: ")
    senha = input("Senha do Usuario: ")
    NovoUsuario = Usuario(nome,login,senha)
    return NovoUsuario

def AcessarPerfil(login):
    u = controladorUsuario.buscar_usuario(login)
    op = int(input("\n1 - Alterar Nome\n2 - Alterar Login\n3 - Alterar Senha\nOpcao: "))
    if(op == 1):
        novoNome = input("Digite o Novo Nome: ")
        NovoUsuario = Usuario(novoNome, u.get("Login"), u.get("Senha"))
        controladorUsuario.apagar_usuario(login)
        controladorUsuario.adicionar_usuario(NovoUsuario)
        print("Nome alterado com Sucesso !!!\n\n")
    elif(op == 2):
        novoLogin = input("Digite o novo Login: ")
        NovoUsuario = Usuario(u.get("Nome"),novoLogin,u.get("Senha"))
        controladorUsuario.apagar_usuario(login)
        controladorUsuario.adicionar_usuario(NovoUsuario)
        print("Login alterado com sucesso !!!\n\n")
    elif(op == 3):
        novaSenha = input("Digite a nova senha: ")
        NovoUsuario = Usuario(u.get("Nome"),u.get("Login"),novaSenha)
        controladorUsuario.apagar_usuario(login)
        controladorUsuario.adicionar_usuario(NovoUsuario)
        print("Senha alterada com sucesso !!!\n\n")
        

def gerenciarAvaliacao():
    op = int(input("\n1 - Fazer Avaliacao\n2 - Alterar Avaliacao\n3 - Apagar Avaliacao\nOpcao: "))

def gerenciaComentario():
    op = int(input("\n1 - Fazer Comentario\n2 - Alterar Comentario\n3 - Apagar Comentario\nOpcao: "))
