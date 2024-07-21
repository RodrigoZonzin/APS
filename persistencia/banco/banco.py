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

#retorna uma tupla com as informacoes do usuario (nome, ... , )
def recupera_usuario_id(id:str) -> tuple: 
    resposta = cur.execute(f"""
        SELECT * 
        FROM USUARIO 
        WHERE id_usuario = {id}
    """)
    resposta = resposta.fetchall(); 
    return list(resposta)[0]; #[0] pois pode haver várias respostas em outros tipos de consulta (funcao abaixo)

#retorna uma lista [user0, ... usern] com todos os usuarios,
#onde user é uma tupla (nome, ..., id_admin)
def recupera_usuarios(): 
    resposta = cur.execute(f"""
        SELECT * 
        FROM USUARIO 
    """)
    resposta = resposta.fetchall(); 
    return list(resposta)

#consulta login e senha para permitir o login
def fazer_login(login, senha): 
    resposta = cur.execute(f"""
        SELECT * 
        FROM USUARIO                       
        WHERE login = {login} AND senha = {senha}
    """)
    return list(resposta.fetchall()) 

#LT deve ser uma lista unitária de tupla [(nome, endereco, descricao)]
#retorna True se der certo e Falso se der errado (qualquer que seja o motivo)
def inserir_local_turistico(LT: list) -> bool:
    try: 
        bd.execute("INSERT INTO TURISMO(nome, endereco, descricao) VALUES (?, ?, ?)", LT) 
        return True
    
    except Exception: 
        return False 

#retorna uma tupla com as informacoes do local turistico 
#(nome, endereco, descricao)
def procura_local_turistico_por_id(id: int) -> tuple: 
    cur.execute(f"""
        SELECT * 
        FROM TURISMO
        WHERE id_turismo = {id}
    """)
    return list(cur.fetchall())[0]

#salva as alteracoes no arquivo .db 
def commit():
    bd.commit()

