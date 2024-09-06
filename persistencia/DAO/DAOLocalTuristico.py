from . import DAO as d
import sqlite3
import model.LocalTuristico as lt

class DAOLocalTuristico(d.DAO):
    __instance = None
    def __new__(cls):
        if DAOLocalTuristico.__instance is None:
            DAOLocalTuristico.__instance = super().__new__(cls)
            DAOLocalTuristico.__instance._initialized = True 
        return DAOLocalTuristico.__instance
    
    def __init__(self):
        super().__init__()

    def commit(self):
        self.bd.commit()

    # Cria a tabela LOCAL_TURISTICO, se não existir
    def cria_tabela_local_turistico(self): 
        try: 
            self.bd.execute("""
                CREATE TABLE LOCALT_ATRAC(
                    id integer primary key autoincrement,   
                    isLT_Atr integer not null,
                    nome varchar(100) unique not null,
                    endereco varchar(200),
                    descricao varchar(500)
                );
            """)
            return True
        except Exception as e: 
            print(f'ERROR ao criar tabela: {e}')
            return False

    # Insere um local turístico na tabela
    def inserir_local_turistico(self, local: lt.LocalTuristico) -> bool:
        try:
            dados = (
                0,
                local.nome,
                local.endereco,
                local.descricao
            )
            print('lt:', dados)
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

    # Retorna um objeto LocalTuristico a partir do id
    def procura_local_turistico_por_id(self, id: int) -> lt.LocalTuristico:
        try:
            res = self.cur.execute(f"""
                SELECT * 
                FROM LOCALT_ATRAC
                WHERE id = {id}
            """)
            resposta = res.fetchone()
            if resposta:
                return lt.LocalTuristico(id=resposta[0], nome=resposta[2], endereco=resposta[3], descricao=resposta[4])
            else:
                return False
        except Exception as e:
            print(f'ERROR ao procurar local por ID: {e}')
            return False

    # Retorna um objeto LocalTuristico a partir do nome
    def procura_local_turistico_por_nome(self, nome: str) -> lt.LocalTuristico:
        try:
            res = self.cur.execute(f"""
                SELECT * 
                FROM LOCALT_ATRAC 
                WHERE nome = '{nome}';
            """)
            resposta = res.fetchone()
            if resposta:
                return lt.LocalTuristico(id=resposta[0], nome=resposta[2], endereco=resposta[3], descricao=resposta[4])
            else:
                return False
        except Exception as e:
            print(f'ERROR ao procurar local por nome: {e}')
            return False

    # Exclui um local turístico pelo ID
    def exclui_local_turistico(self, id: int) -> bool: 
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

    # Retorna uma lista de objetos LocalTuristico com todos os locais turísticos
    def retornaTodosLocais(self) -> list:
        try:
            res = self.cur.execute("""
                SELECT * 
                FROM LOCALT_ATRAC
                WHERE isLT_Atr = 0;
            """)
            resposta = res.fetchall()
            locais = []
            for local in resposta:
                locais.append(lt.LocalTuristico(id=local[0], nome=local[2], endereco=local[3], descricao=local[4]))
            
            return locais
        except Exception as e:
            print(f'ERROR ao retornar todos os locais: {e}')
            return []
