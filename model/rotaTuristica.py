class RotaTuristica:
    def __init__(self,id,  nome, descricao):
        self._id = id
        self._nome = nome
        self._descricao = descricao
        self._locais_turisticos = []
        self._atracoes_turisticas = []

    # Getters e Setters para os atributos da rota
    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_descricao(self):
        return self._descricao

    def set_descricao(self, descricao):
        self._descricao = descricao

    # Getters e Setters para os conjuntos de locais turísticos
    def get_locais_turisticos(self):
        return self._locais_turisticos

    def set_locais_turisticos(self, locais_turisticos):
        self._locais_turisticos = locais_turisticos

    # Getters e Setters para os conjuntos de atrações turísticas
    def get_atracoes_turisticas(self):
        return self._atracoes_turisticas

    def set_atracoes_turisticas(self, atracoes_turisticas):
        self._atracoes_turisticas = atracoes_turisticas

    # Métodos para adicionar locais e atrações
    def add_local_turistico(self, local_turistico):
        self._locais_turisticos.append(local_turistico)

    def add_atracao_turistica(self, atracao_turistica):
        self._atracoes_turisticas.append(atracao_turistica)

    # Método calculado: número total de locais turísticos na rota
    def get_total_locais(self):
        return len(self._locais_turisticos)

    # Método calculado: número total de atrações turísticas na rota
    def get_total_atracoes(self):
        return len(self._atracoes_turisticas)

    # Método calculado: total de atrações e locais na rota
    def get_total_pontos_turisticos(self):
        return self.get_total_locais() + self.get_total_atracoes()
