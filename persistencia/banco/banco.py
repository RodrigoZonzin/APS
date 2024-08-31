import sqlite3


class Banco: 
    
    def __init__(self): 
        self.DATABASE_PATH = 'database.db'; 
        self.bd  = sqlite3.connect(self.DATABASE_PATH)
        self.cur = self.bd.cursor()


    #Métodos para criar/excluir tabelas e outros gerais
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



    def cria_tabela_local_turistico(self): 
        try: 
            self.bd.execute("""
                CREATE TABLE LOCAL_TURISTICO(
                    id_local_turistico integer primary key autoincrement,   
                    nome varchar(100) unique not null,
                    endereco varchar(200),
                    descricao varchar(500)
                );
            """)
            return True
        except: 
            return False


    def cria_tabela_Avaliacao(self): 
        try: 
            self.bd.execute("""
                CREATE TABLE AVALIACAO(
                    id_avaliacao INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_usuario INTEGER,
                    nota INTEGER, 
                    id_local_turistico INTEGER,
                    data DATE, 
                    comentario VARCHAR(300),
                    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
                    FOREIGN KEY (id_local_turistico) REFERENCES Local_Turistico(id_local_turistico)
                )                
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


    #salva as alteracoes no arquivo .db 
    def commit(self):
        self.bd.commit()


    #Métodos para a tabela Usuario

    #dados deve ser uma lista unitaria [(nome, login, senha, is_admin)]
    def insere_usuario(self, dados: list):
        #Colocar hash nas senhas

        try:
            self.bd.executemany(
                "INSERT INTO USUARIO(id_usuario, nome, login, senha, is_admin) VALUES (NULL, ?, ?, ?, ?)",
                dados);
            print(dados)
            self.commit()
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
    def recupera_usuario_login(self, login:str): 
        try:
            resposta = self.cur.execute(f"""
                SELECT * 
                FROM USUARIO 
                WHERE login = '{login}';
            """)
            #print([resposta]) 
            return list(resposta.fetchall())[0]; #[0] pois pode haver várias respostas em outros tipos de consulta

        except Exception as e:
            print(f"ERROR ao retornar user: {e}")
            return False



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


    #Métodos para a tabela Local_Turistico

    #LT deve ser uma lista unitária de tupla [(nome, endereco, descricao)]
    #retorna True se der certo e Falso se der errado (qualquer que seja o motivo)
    def inserir_local_turistico(self, LT: list) -> bool:
        try: 
            self.bd.execute("INSERT INTO LOCAL_TURISTICO(nome, endereco, descricao) VALUES (?, ?, ?)", LT) 
            self.commit()
            return True
        
        except Exception as e:
            print(F'ERROR ao adicionar local: {e}') 
            return False 

    #retorna uma tupla com as informacoes do local turistico 
    #(nome, endereco, descricao)
    def procura_local_turistico_por_id(self, id: int) -> tuple: 
        res = self.cur.execute(f"""
            SELECT * 
            FROM LOCAL_TURISTICO
            WHERE id_local_turistico = {id}
        """)
        return list(res.fetchall())[0]

    #retorna uma tupla com as informacoes do local turistico 
    #(nome, endereco, descricao)
    def procura_local_turistico_por_nome(self, nome: str) -> tuple: 
        try:
            res = self.cur.execute(f"""
                SELECT * 
                FROM LOCAL_TURISTICO 
                WHERE nome = '{nome}';
            """)
            
            return list(res.fetchall())[0]
        
        except Exception as e:
            print(f'ERROR ao procuarar local: {e}')
            return False


    def exclui_local_turistico(self, id: int) -> bool: 
        try: 
            self.bd.execute(f"""
                DELETE FROM LOCAL_TURISTICO
                WHERE id_local_turistico = {id} 
            """)
            self.commit()
            return True
        except Exception as e:
            print(f'ERROR  ao excluir local: {e}') 
            return False 


    def retornaTodosLocais(self):
        try: 
            res = self.bd.execute(f"""
                SELECT *
                FROM LOCAL_TURISTICO 
            """)

            return list(res.fetchall())
        
        except Exception as e:
            print(f'ERROR: {e}') 
            return False


    #Métodos para a tabela Avaliação

    def insere_avaliacao(self, novaAvaliacao): 
        try:
            self.bd.execute(
                f"""INSERT INTO AVALIACAO(id_usuario, nota, id_local_turistico, data, comentario)
                    VALUES ({novaAvaliacao[0]}, {novaAvaliacao[1]}, {novaAvaliacao[2]}, {novaAvaliacao[3]}, '{novaAvaliacao[4]}')""" 
                )
            print(novaAvaliacao)
            self.commit()
            return True
        except Exception as e: 
            print(f'ERROR ao inserir avaliacao: {e}')
            return False



    def exclui_avaliacao_id(self, id: int) -> bool: 
        try: 
            self.bd.execute(f"""
                DELETE FROM AVALIACAO
                WHERE id_avaliacao = {id} 
            """)
            self.commit()
            return True
        
        except Exception as e:
            print(f'ERROR ao excluir avaliacao: {e}') 
            return False 

    def procura_avaliacao_usuario(self, usuarioId): 
        try:
            resposta = self.cur.execute(f"""
                SELECT u.nome, a.comentario, a.nota
                FROM USUARIO u, 
                JOIN AVALIACAO a,
                ON a.id_autor = u.id_usuario
                WHERE u.id_usuario = {usuarioId}    
            """)
            return list(resposta.fetchall())[0]
        
        except:
            return False
        

    def retornaAvalId(self, avalId):
        try:
            res = self.cur.execute(f"""
                SELECT *
                FROM AVALIACAO
                WHERE id_avaliacao = {avalId};
            """)
            
            return list(res.fetchall())

        except Exception as e:
            print(f'ERROR ao retornar avaliacao: {e}')
            return False


    def retornarTodasAvalsUser(self, user):
        try:
            res = self.cur.execute(f"""
                SELECT *
                FROM AVALIACAO
                WHERE id_usuario = {user};
            """)

            return list(res.fetchall())

        except Exception as e:
            print(f"ERROR ao retronar Avals: {e}")   

    def recupera_todas_avaliacoes_usuario(self, login):
        try:
            resposta = self.cur.execute(f"""
                SELECT u.nome AS nome_user, a.comentario, a.nota, a.data, lt.nome AS nome_local, a.id_avaliacao
                FROM USUARIO u
                JOIN AVALIACAO a ON u.id_usuario = a.id_usuario
                JOIN LOCAL_TURISTICO lt ON a.id_local_turistico = lt.id_local_turistico
                WHERE u.login = '{login}';
            """)
            return list(resposta.fetchall())
        except Exception as e:
            print(f'ERROR ao retornar avals local: {e}')
            return False

    #retorna todas as avaliacoes de um determinado local turistico
    #[(Gabriel, "Muito Bom!", 5), (Joao Pedro, "Bom", 4), ...]
    def recupera_todas_avaliacoes_local(self, ltId):
        try:
            resposta = self.cur.execute(f"""
                SELECT u.nome AS nome_user, a.comentario, a.nota, a.data, lt.nome AS nome_local, a.id_avaliacao
                FROM USUARIO u
                JOIN AVALIACAO a ON u.id_usuario = a.id_usuario
                JOIN LOCAL_TURISTICO lt ON a.id_local_turistico = lt.id_local_turistico
                WHERE lt.id_local_turistico = '{ltId}';
            """)
            return list(resposta.fetchall())
        except Exception as e:
            print(f'ERROR ao retornar avals local: {e}')
            return False
        
    def retornaTodasAvals(self):
        try:
            resposta = self.cur.execute("""
                SELECT a.id_avaliacao, a.nota, a.data, a.comentario, u.login, lt.nome
                FROM USUARIO u
                JOIN AVALIACAO a ON u.id_usuario = a.id_usuario
                JOIN LOCAL_TURISTICO lt ON a.id_local_turistico = lt.id_local_turistico
            """)
            return list(resposta.fetchall())
        
        except Exception as e:
            print(f'ERROR ao retornar todas avals: {e}')
            return False

    def exclui_todasAval_user(self, login):
        try:
            self.bd.execute(f"""
                DELETE FROM AVALIACAO
                WHERE id_usuario IN (
                    SELECT a.id_usuario
                    FROM AVALIACAO a
                    JOIN USUARIO u ON a.id_usuario = u.id_usuario
                    WHERE u.login = '{login}'
                )
                """)
            self.bd.commit()
            print(f'Todas as avaliacoes do {login} foram apagadas')
            return True
        except Exception as e:
            print(f'ERROR ao apagar avaliacoes: {e}')
            return False