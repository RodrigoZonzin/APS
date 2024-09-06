import sqlite3
import model.rotaTuristica as rt

class DAOLocalTuristico:
    def __init__(self):
        super.__init__()

    def commit(self):
        self.bd.commit()

    def cria_tabela_rota_turistica(self) -> bool: 
        try:
            self.bd.execute("""
                CREATE TABLE ROTA_TURISTICA(
                    id_rota_turistica INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome VARCHAR(100) UNIQUE NOT NULL,
                    endereco VARCHAR(200),
                    id_localAtracao1 INTEGER,
                    id_localAtracao2 INTEGER,
                    id_localAtracao3 INTEGER,
                    id_localAtracao4 INTEGER
                )
            """)
            return True
        else: 
            print("Erro na criação da tabela rota turistica")
            return False

    def insere_rota_turistica(self, rt: rt.RotaTuristica) -> bool: 
        try: 
            dados = (rt._id,
                     rt._nome,
                     rt._descricao,
                     rt._locais_turisticosAtracoes[0].id,
                     rt._locais_turisticosAtracoes[1].id,
                     rt._locais_turisticosAtracoes[2].id,
                     rt._locais_turisticosAtracoes[3].id
                    )
        

            self.bd.execute(f"""
                INSERT INTO ROTA_TURISTICA
                    (id_rota_turistica, nome, endereco, id_localAtracao1,id_localAtracao2, id_localAtracao3, id_localAtracao4)
                VALUES
                    (NULL, ?, ?, ?, ?, ?, ?)
                """, dados)

            self.commit()
            return True
        except: 
            print("Erro inserindo RotaTuristica")
            return False

                #retorna uma lista de objetos atracao [Atracao1, ..., AtracaoN]
    
    def seleciona_todas_rotas() -> list:
        try:
            res = self.cur.execute ("SELECT * FROM ROTA_TURISTICA")
            res = res.fetchall(); 

            rotas = []
            for rota in res: 
                rotas.append(RotaTuristica(
                    _id = rota[0],
                    _nome = rota[1],
                    _descricao = rota[2],
                    _locais_turisticosAtracoes = [rota[3], rota[4]
                                                  rota[5], rota[6]])
                )
            return rotas
            
        except:
            return False
