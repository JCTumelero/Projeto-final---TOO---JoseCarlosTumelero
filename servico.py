from modelo import Demanda

class DemandaServico:
    def __init__(self, repositorio):
        self.repositorio = repositorio
        self.demandas = repositorio.carregar()

    def adicionar(self, descricao, origem, prioridade, responsavel, setor, prazo=None):
        d = Demanda(descricao, origem, prioridade, responsavel, setor, prazo)
        self.demandas.append(d)
        self.repositorio.salvar(self.demandas)

    def listar(self):
        return self.demandas

    def concluir(self, id_demanda):
        for d in self.demandas:
            if d.id == id_demanda:
                d.concluir()
        self.repositorio.salvar(self.demandas)

    def filtrar_por_status(self, status):
        return [d for d in self.demandas if d.status.value == status]

    def filtrar_por_responsavel(self, nome):
        return [d for d in self.demandas if nome.lower() in d.responsavel.lower()]