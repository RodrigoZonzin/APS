import sqlite3
import model.LocalTuristico as lt

class DAOLocalTuristico:
    def __init__(self):
        super.__init__()

    def commit(self):
        self.bd.commit()

    # Cria a tabela LOCAL_TURISTICO, se não existir
    def cria_tabela_local_turistico(self): 
        try: 
            self.bd.execute("""
                CREATE TABLE LOCAL_TURISTICO(
                    id_local_turistico INTEGER PRIMARY KEY AUTOINCREMENT,   
                    nome VARCHAR(100) UNIQUE NOT NULL,
                    endereco VARCHAR(200),
                    descricao VARCHAR(500)
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
                local.nome,
                local.endereco,
                local.descricao
            )
            self.bd.execute(
                "INSERT INTO LOCAL_TURISTICO(nome, endereco, descricao) VALUES (?, ?, ?)",
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
                FROM LOCAL_TURISTICO
                WHERE id_local_turistico = {id}
            """)
            resposta = res.fetchone()
            if resposta:
                return lt.LocalTuristico(id=resposta[0], nome=resposta[1], endereco=resposta[2], descricao=resposta[3])
            else:
                return None
        except Exception as e:
            print(f'ERROR ao procurar local por ID: {e}')
            return None

    # Retorna um objeto LocalTuristico a partir do nome
    def procura_local_turistico_por_nome(self, nome: str) -> lt.LocalTuristico:
        try:
            res = self.cur.execute(f"""
                SELECT * 
                FROM LOCAL_TURISTICO 
                WHERE nome = '{nome}';
            """)
            resposta = res.fetchone()
            if resposta:
                return lt.LocalTuristico(id=resposta[0], nome=resposta[1], endereco=resposta[2], descricao=resposta[3])
            else:
                return None
        except Exception as e:
            print(f'ERROR ao procurar local por nome: {e}')
            return None

    # Exclui um local turístico pelo ID
    def exclui_local_turistico(self, id: int) -> bool: 
        try:
            self.bd.execute(f"""
                DELETE FROM LOCAL_TURISTICO
                WHERE id_local_turistico = {id}
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
                FROM LOCAL_TURISTICO
            """)
            resposta = res.fetchall()
            locais = []
            for local in resposta:
                locais.append(lt.LocalTuristico(id=local[0], nome=local[1], endereco=local[2], descricao=local[3]))
            
            return locais
        except Exception as e:
            print(f'ERROR ao retornar todos os locais: {e}')
            return []
