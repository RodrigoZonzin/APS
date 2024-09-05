import DAOUsuario as daou
import model.Usuario as u


uRod = u.Usuario(0, 'Rodrigo', 'zonzin@rodrigo', 'odeiosoftware', 0, None)
uAlm = u.Usuario(1, 'Almada', 'almada@almada', 'emticonfio', 1, None)

udao = daou.DAOUsuario()
udao.cria_tabela_usuario()
udao.insere_usuario(uRod)
udao.insere_usuario(uAlm)
udao.commit()