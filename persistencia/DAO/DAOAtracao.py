import sqlite3
import model.AtracaoTuristica import AtracaoTuristica *

class DAOAtracao:
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
            dados = (atracao.get_nome(),
                     atracao.get_descricao(),
                     atracao.get_endereco())

            self.bd.execute("""
                INSERT INTO ATRACAO (nome, descricao, endereco)
                VALUES (?, ?, ?)
            """, dados)

            self.commit()
            return True

        except Exception as e:
            print(f"Erro inserindo Atracao Turistica: {e}")
            return False

    #retorna uma lista de objetos atracao [Atracao1, ..., AtracaoN]
    def seleciona_todas_atracoes() -> list:
        try:
            res = self.cur.execute ("SELECT * FROM ATRACAO")
            res = res.fetchall(); 

            atracoes = []
            for atracao in res: 
                atracoes.append(AtracaoTuristica(
                    id = atracao[0],
                    nome = atracao[1],
                    endereco = atracao[2],
                    descricao = atracao[3]
                ))
            
            return atracoes
        except:
            return False
