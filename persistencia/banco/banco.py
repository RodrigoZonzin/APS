import sqlite3

DATABASE_PATH = 'APS/persistencia/banco/database.db'; 

bd = sqlite3.connect(DATABASE_PATH)
cur = bd.cursor()

bd.execute("""
    CREATE TABLE USUARIO(
        id_usuario int auto_increment primary key,
        nome varchar(100) not null, 
        login varchar(30) not null,
        senha varchar(30) not null,
        is_admin int
    );
""")

bd.execute("""
    CREATE TABLE TURISMO(
        id_turismo int auto_increment primary key,   
        nome varchar(100) not null,
        endereco varchar(200),
        descricao varchar(500)
    );
""")

bd.execute("""
    CREATE TABLE LOCAL_TURISTICO(
        id_local_turistico int auto_increment primary key
    );
""")

#funcao para apagar uma tabela do banco de dados
#retorna um True caso dê certo e False caso dê errado
def drop_table(nome_tabela: str) -> bool:
    try: 
        bd.execute(f'DROP TABLE {nome_tabela}')
        return True
    
    except Exception: 
        return False    

#dados deve ser uma tupla (nome, login, senha, is_admin)
def insere_usuario(dados: tuple):
    bd.executemany(
        "INSERT INTO USUARIO(nome, login, senha, is_admin) VALUES (?, ?, ?, ?)",
        dados); 
 
#procura na tabela Usuario por nome e retorna uma lista com todos os atributos 
def recupera_usuario_nome(login:str): 
    resposta = cur.execute(f"""
        SELECT * 
        FROM USUARIO 
        WHERE login = {login}
    """)
    resposta.fetchall(); 
    return list(resposta)[0]; #[0] pois pode haver várias respostas em outros tipos de consulta

def recupera_usuario_id(id:str): 
    resposta = cur.execute(f"""
        SELECT * 
        FROM USUARIO 
        WHERE id_usuario = {id}
    """)
    resposta.fetchall(); 
    return list(resposta)[0]; #[0] pois pode haver várias respostas em outros tipos de consulta (funcao abaixo)

#retorna uma lista [user0, ... usern] com todos os usuarios,
#onde user é uma tupla (nome, ..., id_admin)
def recupera_usuarios(): 
    resposta = cur.execute(f"""
        SELECT * 
        FROM USUARIO 
    """)
    resposta.fetchall(); 
    return list(resposta)

def commit():
    bd.commit()
