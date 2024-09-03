import sqlite3

class DAO():    
    def __init__(self):
        self.DATABASE_PATH = 'database.db'; 
        self.bd  = sqlite3.connect(self.DATABASE_PATH)
        self.cur = self.bd.cursor()

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

    def create():
        pass

    def read():
        pass

    def update():
        pass

    def delete():
        pass

    def search():
        pass