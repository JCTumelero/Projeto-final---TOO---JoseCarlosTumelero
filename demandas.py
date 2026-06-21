from datetime import datetime
import json


class Demanda:
    def __init__(self, descricao, origem, prioridade, responsavel, setor):
        self.descricao = descricao
        self.origem = origem
        self.prioridade = prioridade
        self.responsavel = responsavel
        self.setor = setor
        self.data_criacao = datetime.now()
        self.status = "Aberta"

    def concluir(self):
        self.status = "Concluída"

    def to_dict(self):
        return {
            "descricao": self.descricao,
            "origem": self.origem,
            "prioridade": self.prioridade,
            "responsavel": self.responsavel,
            "setor": self.setor,
            "data_criacao": self.data_criacao.strftime("%Y-%m-%d %H:%M:%S"),
            "status": self.status
        }

    @staticmethod
    def from_dict(dados):
        d = Demanda(
            dados["descricao"],
            dados["origem"],
            dados["prioridade"],
            dados["responsavel"],
            dados["setor"]
        )
        d.data_criacao = datetime.strptime(dados["data_criacao"], "%Y-%m-%d %H:%M:%S")
        d.status = dados["status"]
        return d

    def __str__(self):
        return f"[{self.status}] {self.descricao} | {self.prioridade} | Resp: {self.responsavel}"


def salvar_em_arquivo(demandas_list=None, path="demandas.json"):
    if demandas_list is None:
        demandas_list = []
    with open(path, "w", encoding="utf-8") as f:
        json.dump([d.to_dict() for d in demandas_list], f, indent=4, ensure_ascii=False)

def carregar_do_arquivo():
    try:
        with open("demandas.json", "r", encoding="utf-8") as f:
            dados = json.load(f)
            return [Demanda.from_dict(d) for d in dados]
    except FileNotFoundError:
        return []


# Exemplo de uso
demandas = [
    Demanda("Teste", "Origem A", "Alta", "Responsável A", "Setor A"),
    Demanda("Teste 2", "Origem B", "Baixa", "Responsável B", "Setor B")
]

salvar_em_arquivo(demandas)
demandas = carregar_do_arquivo()

print(demandas)

def adicionar_demanda():
    descricao = input("Descrição: ")
    origem = input("Origem (email/presencial): ")
    prioridade = input("Prioridade (alta/media/baixa): ")
    responsavel = input("Responsável: ")
    setor = input("Setor: ")

    demanda = Demanda(descricao, origem, prioridade, responsavel, setor)
    demandas.append(demanda)

    salvar_em_arquivo()
    print("✅ Demanda salva!\n")
