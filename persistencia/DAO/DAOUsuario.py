from DAO import DAO
from model.Usuario import Usuario
from model.Avaliacao import Avaliacao
from datetime import datetime
import sqlite3


class DAOUsuario(DAO):
    def __init__(self):
        super().__init__()

    #cria tabela caso ela nao exista
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

    #dados deve ser um usuario
    def insere_usuario(self, user: Usuario) -> bool:
        #Colocar hash nas senhas
        dados = (
            user.nome,
            user.login,
            user.senha,
            user.isAdmin)
        
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
   
    #excluir usuario
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
        
    #retorna um objeto usuario
    def recupera_usuario_id(self, id:str) -> Usuario: 
        try:
            resposta = self.cur.execute(f"""
                SELECT * 
                FROM USUARIO 
                WHERE id_usuario = {id}
            """)
            resposta = resposta.fetchall(); 
            
            return Usuario(Usuario(id=          resposta[0], 
                                            nome=        resposta[1], 
                                            login=       resposta[2], 
                                            senha=       resposta[3], 
                                            isAdmin=     resposta[4], 
                                            avals=       None))
        except:
            return False


    #procura na tabela Usuario por nome e retorna uma lista com todos os atributos 
    def recupera_usuario_login(self, login:str) -> Usuario: 
        try:
            resposta = self.cur.execute(f"""
                SELECT * 
                FROM USUARIO 
                WHERE login = '{login}';
            """)
            
            avaliacoes = None

            usuario_consultado = Usuario(id=          resposta[0], 
                                           nome=        resposta[1], 
                                           login=       resposta[2], 
                                           senha=       resposta[3], 
                                           isAdmin=     resposta[4], 
                                           avals=       avaliacoes)

            return usuario_consultado

        except Exception as e:
            print(f"ERROR ao retornar user: {e}")
            return False
        
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
        

    #retorna uma lista [user0, ... usern] com todos os usuarios,
    #onde user é um objeto Usuario
    def recupera_usuarios(self) -> list: 
        try:
            resposta = self.cur.execute(f"""
                SELECT * 
                FROM USUARIO 
            """)
            resposta = resposta.fetchall(); 
            
            objetos_usuarios = []
            avaliacoes = None

            for usuario in list(resposta):
                objetos_usuarios.append(Usuario(id=          resposta[0], 
                                           nome=        resposta[1], 
                                           login=       resposta[2], 
                                           senha=       resposta[3], 
                                           isAdmin=     resposta[4], 
                                           avals=       avaliacoes))
            
            return objetos_usuarios
        
        except Exception as e:
            print(f"ERROR no recupera_usuarios: {e}")
            return 500 #verificar esse código de return

    #transforma um usuario normal em adm e vice versa         
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
