import sqlite3

class DAO():    
    __instance = None
    def __new__(cls):
        if DAO.__instance is None:
            DAO.__instance = super().__new__(cls)
        return DAO.__instance
    
    def __init__(self):
        self.DATABASE_PATH = 'database.db'; 
        self.bd  = sqlite3.connect(self.DATABASE_PATH)
        self.cur = self.bd.cursor()

    def drop_table(self, nome_tabela: str) -> bool:
        pass
        
    def commit(self):
        pass

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