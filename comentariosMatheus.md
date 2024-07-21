Não pode ter cadastre-se no diagrama de casos de uso 

Colocar uma seta direta para o login pois, para o login, não é preciso haver o cadastro uma vez que o usuário já está cadastrado 

Não é preciso ter o alterar

No diagrama de casos de uso, add comentário sobre a avaliação turística

Avaliação pode ser uma classe com atributos Nota e Comentário 

Usuário seria uma seta direta para o local mais bem avaliado 


Nenhum dos métodos na classe Usuário deveria estar aí (apagar, buscar) e etc. Devem estar nas camadas de modelo, visão ou etc. 

Não tem nome do atributo nas seringas da relações no diagrama de classes 

Matheus recomenda q a Avaliação tenha o atributo Usuário. (Comentário deve ser apagado pois Avaliação conterá o comentário). 

Rota não é relação todo-parte. Inverter a seta. A Rota que tem a Atração. 

No diagrama maior. Persistência deve conversar com Controle e Visão. Controle com Modelo. 

O estado 'está logado' não faz diferença no código atual. A Tela não tem funcionalidade nova depois do Login. 

Cada janela tem que ser uma classe separada. 

Os métodos das classes JanelaPrincipal (e outras) não estão no diagrama. 

Persistência, Modelo e Visão têm que ter arquivos separados!!!
