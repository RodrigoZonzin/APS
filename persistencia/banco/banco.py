import sqlite3


class Banco: 
    
    def __init__(self): 
        self.DATABASE_PATH = 'database.db'; 
        self.bd  = sqlite3.connect(self.DATABASE_PATH)
        self.cur = self.bd.cursor()


    def cria_tabela_usuario(self): 
        try: 
            self.bd.execute("""
                CREATE TABLE USUARIO(
                    id_usuario integer primary key autoincrement,
                    nome varchar(100) not null, 
                    login varchar(30) unique not null,
                    senha varchar(30) not null,
                    is_admin int
                );
            """)
            return True 
        
        except: 
            return False



    def cria_tabela_turismo(self): 
        try: 
            self.bd.execute("""
                CREATE TABLE TURISMO(
                    id_turismo integer primary key autoincrement,   
                    nome varchar(100) not null,
                    endereco varchar(200),
                    descricao varchar(500)
                );
            """)
            return True
        except: 
            return False



    def cria_tabela_localTuristico(self): 
        try: 
            self.bd.execute("""
                CREATE TABLE LOCAL_TURISTICO(
                    id_local_turistico integer autoincrement primary key
                );
            """)
            return True
        except: 
            return False



    #funcao para apagar uma tabela do banco de dados
    #retorna um True caso dê certo e False caso dê errado
    def drop_table(self, nome_tabela: str) -> bool:
        try: 
            self.bd.execute(f'DROP TABLE {nome_tabela}')
            return True
        
        except Exception: 
            return False    



    #dados deve ser uma lista unitaria [(nome, login, senha, is_admin)]
    def insere_usuario(self, dados: list):
        #Colocar hash nas senhas

        try:
            self.bd.executemany(
                "INSERT INTO USUARIO(id_usuario, nome, login, senha, is_admin) VALUES (NULL, ?, ?, ?, ?)",
                dados);
            print(dados)
        
        except sqlite3.IntegrityError as e:
            print("ERRO de integridade chave primaria ou unique")

        except Exception as e:
            print(e) 
    

    def excluir_usuario(self, login):
        try:
            self.bd.execute(f"""
                DELETE 
                FROM USUARIO
                WHERE login = '{login}';                
            """)
            print(f"Usuario {login} deletado")
            self.bd.commit()

            return 200

        except Exception as e:
            print(f"ERROR ao deletar user: {e}")
            return 400


    #procura na tabela Usuario por nome e retorna uma lista com todos os atributos 
    def procura_usuario_login(self, login:str): 
        resposta = self.cur.execute(f"""
            SELECT * 
            FROM USUARIO 
            WHERE login = {login}
        """)
        resposta.fetchall();
        print([resposta]) 
        return list(resposta)[0]; #[0] pois pode haver várias respostas em outros tipos de consulta



    #retorna uma tupla com as informacoes do usuario (nome, ... , )
    def recupera_usuario_id(self, id:str) -> tuple: 
        resposta = self.cur.execute(f"""
            SELECT * 
            FROM USUARIO 
            WHERE id_usuario = {id}
        """)
        resposta = resposta.fetchall(); 
        return list(resposta)[0]; #[0] pois pode haver várias respostas em outros tipos de consulta (funcao abaixo)



    #retorna uma lista [user0, ... usern] com todos os usuarios,
    #onde user é uma tupla (nome, ..., id_admin)
    def recupera_usuarios(self): 
        try:
            resposta = self.cur.execute(f"""
                SELECT * 
                FROM USUARIO 
            """)
            resposta = resposta.fetchall(); 
            return list(resposta)
        
        except Exception as e:
            print(f"ERROR no recupera_usuarios: {e}")
            return 500 #verificar esse código de return


    #consulta login e senha para permitir o login
    def fazer_login(self, login, senha): 
        try:
            resposta = self.cur.execute(f"""
                SELECT * 
                FROM USUARIO                       
                WHERE login = '{login}'
            """)

            resposta = resposta.fetchall()

            if senha == resposta[0][3]:
                print('login feito')
                return resposta[0]
            else:
                print('login recusado')
                return 400 #verificar esses codigos de erros

        except Exception as e:
            print(f'ERROR login banco: {e}')
            return 500 #verificar esses codigos de erros


    def mudarAdm(self, login, isAdm):
        if isAdm == 0:
            isAdm = 1
        else:
            isAdm = 0
        
        try:
            self.bd.execute(f"""
                UPDATE USUARIO
                SET is_admin = {isAdm}
                WHERE login = '{login}';
            """)
            print("isAdm atualizado")
            self.bd.commit()

            return 200

        except Exception as e:
            print(f"ERROR: {e}")
            return 400


    #LT deve ser uma lista unitária de tupla [(nome, endereco, descricao)]
    #retorna True se der certo e Falso se der errado (qualquer que seja o motivo)
    def inserir_local_turistico(self, LT: list) -> bool:
        try: 
            self.bd.execute("INSERT INTO TURISMO(nome, endereco, descricao) VALUES (?, ?, ?)", LT) 
            return True
        
        except Exception: 
            return False 

    #retorna uma tupla com as informacoes do local turistico 
    #(nome, endereco, descricao)
    def procura_local_turistico_por_id(self, id: int) -> tuple: 
        res = self.cur.execute(f"""
            SELECT * 
            FROM TURISMO
            WHERE id_turismo = {id}
        """)
        return list(res.fetchall())[0]

    #retorna uma tupla com as informacoes do local turistico 
    #(nome, endereco, descricao)
    def procura_local_turistico_por_nome(self, nome: str) -> tuple: 
        res = self.cur.execute(f"""
            SELECT * 
            FROM TURISMO 
            WHERE nome = {nome}
        """)
        
        return list(res.fetchall())[0]


    def exclui_local_turistico(self, id: int) -> bool: 
        try: 
            self.bd.execute(f"""
                DELETE FROM TURISMO
                WHERE id_turismo = id 
            """)
            return True
        except Exception: 
            return False 

    #salva as alteracoes no arquivo .db 
    def commit(self):
        self.bd.commit()

