from . import DAO as d
import model.Avaliacao as a
import sqlite3


class DAOAvaliacao(d.DAO):
    __instance = None
    def __new__(cls):
        if DAOAvaliacao.__instance is None:
            DAOAvaliacao.__instance = super().__new__(cls)
            DAOAvaliacao.__instance._initialized = True 
        return DAOAvaliacao.__instance
    
    def __init__(self):
        super().__init__()

    # Método para criar a tabela AVALIACAO caso não exista
    def cria_tabela_Avaliacao(self): 
        try: 
            self.bd.execute("""
                CREATE TABLE AVALIACAO(
                    id_avaliacao INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_usuario INTEGER,
                    nota INTEGER, 
                    id_localAtr INTEGER,
                    data DATE, 
                    comentario VARCHAR(300),
                    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
                    FOREIGN KEY (id_localAtr) REFERENCES LOCALT_ATRAC(id)
                )                
            """)
            return True 
        except Exception as e: 
            print(f"ERROR ao criar tabela AVALIACAO: {e}")
            return False

    # Método para inserir uma nova avaliação
    def insere_avaliacao(self, novaAvaliacao: a.Avaliacao) -> bool: 
        dados = (
            novaAvaliacao.Autor,
            novaAvaliacao.nota,
            novaAvaliacao.LocalAtracao,
            novaAvaliacao.dataHora,
            novaAvaliacao.coment
        )
        try:
            self.bd.execute(
                """INSERT INTO AVALIACAO(id_usuario, nota, id_localAtr, data, comentario)
                    VALUES (?, ?, ?, ?, ?)""",
                dados)
            
            self.commit()
            return True
        except Exception as e: 
            print(f'ERROR ao inserir avaliacao: {e}')
            return False

    # Método para excluir uma avaliação pelo ID
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

    # Método para procurar uma avaliação por ID
    def procura_avaliacao_id(self, id: int) -> a.Avaliacao: 
        try:
            res = self.cur.execute(f"""
                SELECT * 
                FROM AVALIACAO
                WHERE id_avaliacao = {id}
            """)
            resultado = res.fetchone()
            if resultado:
                return a.Avaliacao(
                    id_avaliacao    =resultado[0],
                    id_usuario      =resultado[1],
                    nota            =resultado[2],
                    id_local_turistico=resultado[3],
                    data            =resultado[4],
                    comentario      =resultado[5]
                )
            return None
        except Exception as e:
            print(f'ERROR ao procurar avaliacao: {e}')
            return None

    # Método para retornar todas as avaliações de um usuário específico
    def procura_avaliacoes_usuario(self, id_usuario: int) -> list: 
        try:
            res = self.cur.execute(f"""
                SELECT * 
                FROM AVALIACAO
                WHERE id_usuario = {id_usuario}
            """)
            resultado = res.fetchall()
            avaliacoes = [] 
            
            for avaliacao_i in resultado: 
                avaliacoes.append(a.Avaliacao(
                                    id_avaliacao    =avaliacao_i[0],
                                    id_usuario      =avaliacao_i[1],
                                    nota            =avaliacao_i[2],
                                    id_local_turistico=avaliacao_i[3],
                                    data            =avaliacao_i[4],
                                    comentario      =avaliacao_i[5])
                )
            return avaliacoes
        except Exception as e:
            print(f'ERROR ao procurar avaliacoes do usuario: {e}')
            return []

    # Método para retornar todas as avaliações de um local turístico específico
    def procura_avaliacoes_local(self, id_local_turistico: int) -> list:
        try:
            res = self.cur.execute(f"""
                SELECT * 
                FROM AVALIACAO
                WHERE id_localAtr = {id_local_turistico}
            """)

            resultado = res.fetchall()
            avaliacoes = [] 

            for avaliacao_i in resultado: 
                avaliacoes.append(a.Avaliacao(
                                    id_avaliacao    =avaliacao_i[0],
                                    id_usuario      =avaliacao_i[1],
                                    nota            =avaliacao_i[2],
                                    id_local_turistico=avaliacao_i[3],
                                    data            =avaliacao_i[4],
                                    comentario      =avaliacao_i[5])
                )
            return avaliacoes

        except Exception as e:
            print(f'ERROR ao procurar avaliacoes do local: {e}')
            return []

    # Método para retornar todas as avaliações
    def retorna_todas_avaliacoes(self) -> list:
        try:
            res = self.cur.execute("""
                SELECT * 
                FROM AVALIACAO
            """)
            resultado = res.fetchall()
            avaliacoes = []

            for avaliacao_i in resultado:
                avaliacoes.append(a.Avaliacao(
                    id_avaliacao    =avaliacao_i[0],
                    id_usuario      =avaliacao_i[1],
                    nota            =avaliacao_i[2],
                    id_local_turistico=avaliacao_i[3],
                    data            =avaliacao_i[4],
                    comentario      =avaliacao_i[5])
                )    
            return avaliacoes
        
        except Exception as e:
            print(f'ERROR ao retornar todas as avaliacoes: {e}')
            return []

    # Método para excluir todas as avaliações de um usuário específico
    def exclui_todas_avaliacoes_usuario(self, login) -> bool:
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
            self.commit()
            print(f'Todas as avaliacoes do {login} foram apagadas')
            return True
        
        except Exception as e:
            print(f'ERROR ao excluir avaliacoes do usuario: {e}')
            return False

    def recupera_todas_avaliacoes_usuario(self, login):
        try:
            resposta = self.cur.execute(f"""
                SELECT u.nome AS nome_user, a.comentario, a.nota, a.data, lt.nome AS nome_local, a.id_avaliacao
                FROM USUARIO u
                JOIN AVALIACAO a ON u.id_usuario = a.id_usuario
                JOIN LOCALT_ATRAC lt ON a.id_localAtr = lt.id
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
                JOIN LOCALT_ATRAC lt ON a.id_localAtr = lt.id
                WHERE lt.id = '{ltId}';
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
                JOIN LOCALT_ATRAC lt ON a.id_localAtr = lt.id
            """)
            return list(resposta.fetchall())
        
        except Exception as e:
            print(f'ERROR ao retornar todas avals: {e}')
            return False