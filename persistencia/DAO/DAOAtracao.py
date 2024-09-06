from . import DAO as d
import sqlite3
from model.AtracaoTuristica import AtracaoTuristica 

class DAOAtracao(d.DAO):
    __instance = None
    def __new__(cls):
        if DAOAtracao.__instance is None:
            DAOAtracao.__instance = super().__new__(cls)
            DAOAtracao.__instance._initialized = True 
        return DAOAtracao.__instance
    
    def __init__(self):
        super().__init__()

    def commit(self):
        self.bd.commit()

    def cria_tabela_atracao(self) -> bool:
        try:
            self.bd.execute("""
                CREATE TABLE ATRACAO(
                    id_atracao INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome VARCHAR(100) UNIQUE NOT NULL,
                    descricao TEXT NOT NULL,
                    endereco VARCHAR(200) NOT NULL
                )
            """)
            self.commit()
            return True
        except Exception as e:
            print(f"Erro na criação da tabela atracao: {e}")
            return False

    def insere_atracao(self, atracao: AtracaoTuristica) -> bool:
        try:
            dados = (
                1,
                atracao.nome,
                atracao.endereco,
                atracao.descricao
            )
            print('atr:', dados)
            self.bd.execute(
                "INSERT INTO LOCALT_ATRAC(isLT_Atr, nome, endereco, descricao) VALUES (?, ?, ?, ?)",
                dados
            )
            self.commit()
            return True
        except sqlite3.IntegrityError as e:
            print(f"ERROR de integridade: {e}")
            return False
        except Exception as e:
            print(f"ERROR ao inserir local: {e}")
            return False

        except Exception as e:
            print(f"Erro inserindo Atracao Turistica: {e}")
            return False

    def procura_atracao_turistica_por_id(self, id: int):
        try:
            res = self.cur.execute(f"""
                SELECT * 
                FROM LOCALT_ATRAC
                WHERE id = {id}
            """)
            resposta = res.fetchone()
            if resposta:
                return AtracaoTuristica(id=resposta[0], nome=resposta[2], endereco=resposta[3], descricao=resposta[4])
            else:
                return False
        except Exception as e:
            print(f'ERROR ao procurar local por ID: {e}')
            return False

    # Retorna um objeto LocalTuristico a partir do nome
    def procura_atracao_turistica_por_nome(self, nome: str):
        try:
            res = self.cur.execute(f"""
                SELECT * 
                FROM LOCALT_ATRAC 
                WHERE nome = '{nome}';
            """)
            resposta = res.fetchone()
            if resposta:
                return AtracaoTuristica(id=resposta[0], nome=resposta[2], endereco=resposta[3], descricao=resposta[4])
            else:
                return False
        except Exception as e:
            print(f'ERROR ao procurar local por nome: {e}')
            return False

    def exclui_atracao_turistica(self, id: int) -> bool: 
        try:
            self.bd.execute(f"""
                DELETE FROM LOCALT_ATRAC
                WHERE id = {id}
            """)
            self.commit()
            return True
        except Exception as e:
            print(f'ERROR ao excluir local: {e}')
            return False

    #retorna uma lista de objetos atracao [Atracao1, ..., AtracaoN]
    def seleciona_todas_atracoes(self) -> list:
        try:
            res = self.cur.execute("""
                SELECT * 
                FROM LOCALT_ATRAC
                WHERE isLT_Atr = 1;
            """)
            resposta = res.fetchall()
            locais = []
            for local in resposta:
                locais.append(AtracaoTuristica(id=local[0], nome=local[2], endereco=local[3], descricao=local[4]))
            
            return locais
        except Exception as e:
            print(f'ERROR ao retornar todos os locais: {e}')
            return []
