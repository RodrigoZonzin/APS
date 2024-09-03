from DAO import DAO
import model.Avaliacao as a
import sqlite3


class DAOAvaliacao(DAO):
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
                    id_local_turistico INTEGER,
                    data DATE, 
                    comentario VARCHAR(300),
                    FOREIGN KEY (id_usuario) REFERENCES USUARIO(id_usuario),
                    FOREIGN KEY (id_local_turistico) REFERENCES LOCAL_TURISTICO(id_local_turistico)
                );
            """)
            return True 
        except Exception as e: 
            print(f"ERROR ao criar tabela AVALIACAO: {e}")
            return False

    # Método para inserir uma nova avaliação
    def insere_avaliacao(self, novaAvaliacao: a.Avaliacao) -> bool: 
        dados = (
            novaAvaliacao.id_usuario,
            novaAvaliacao.nota,
            novaAvaliacao.id_local_turistico,
            novaAvaliacao.data,
            novaAvaliacao.comentario
        )
        try:
            self.bd.execute(
                """INSERT INTO AVALIACAO(id_usuario, nota, id_local_turistico, data, comentario)
                    VALUES (?, ?, ?, ?, ?')""",
                novaAvaliacao)
            
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
                WHERE id_local_turistico = {id_local_turistico}
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
    def exclui_todas_avaliacoes_usuario(self, id_usuario: int) -> bool:
        try:
            self.bd.execute(f"""
                DELETE FROM AVALIACAO
                WHERE id_usuario = {id_usuario}
            """)
            self.commit()
            return True
        
        except Exception as e:
            print(f'ERROR ao excluir avaliacoes do usuario: {e}')
            return False
