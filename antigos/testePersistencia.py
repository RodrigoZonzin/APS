from model import UsuarioAdm as ua
from persistencia import PersistenciaUsuarioAdm as pers

usrRodrigo = ua.UsuarioAdm(00, "Rodrigo", "zonz", "rod123", False)
usrAlmada = ua.UsuarioAdm(1, "Almada", "almada", "almada123", False)

persAdm = pers.PersistenciaUsuario()

persAdm.criaArquivoPersistencia()
persAdm.insereUsuario(usrRodrigo)
persAdm.insereUsuario(usrAlmada)






