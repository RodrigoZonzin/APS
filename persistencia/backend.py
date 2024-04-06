from pandas import *

# alterar o path para o seu prorpio
pathU = r'C:\Users\luizf\Documents\faculdade\7º período\APS\code\persistencia\usuarios.csv'
pathLT =  r'C:\Users\luizf\Documents\faculdade\7º período\APS\code\persistencia\localTuristico.csv'

def retornaUsers():
    users = read_csv(pathU)
    
    return users


def retonraLocalT():
    locaT = read_csv(pathLT)
    
    return locaT


def insereUsuario(df, nome, login, senha, isAdmin=False, comentarios=None, avaliacoes=None):
    if login in df['login'].values: 
        print('Usuário ja registrado')
        return
    
    user = {'nome': nome, 
            'login': login,
            'senha': senha,
            'isAdmin': isAdmin,
            'comentarios': comentarios,
            'avaliacoes': avaliacoes}
    
    df = df.append(user, ignore_index=True)
    df.to_csv(pathU, index=False)


def insereLocalT(df, id, nome, endereco, comentarios=None, avaliacoes=None):
    if id in df['id'].values: 
        print('Local turistico ja inserido')
        return
    
    user = {'id': id,
            'nome': nome, 
            'endereco': endereco,
            'comentarios': comentarios,
            'avaliacoes': avaliacoes}
    
    df = df.append(user, ignore_index=True)
    df.to_csv(pathLT, index=False)
