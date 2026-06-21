from datetime import datetime
from enum import Enum
import uuid

class Prioridade(Enum):
    ALTA = "alta"
    MEDIA = "media"
    BAIXA = "baixa"


class Status(Enum):
    ABERTA = "aberta"
    EM_ANDAMENTO = "em andamento"
    CONCLUIDA = "concluida"


class Demanda:
    def __init__(self, descricao, origem, prioridade, responsavel, setor, prazo=None):
        self.id = str(uuid.uuid4())
        self.descricao = descricao
        self.origem = origem
        self.prioridade = Prioridade(prioridade)
        self.responsavel = responsavel
        self.setor = setor
        self.data_criacao = datetime.now()
        self.prazo = prazo
        self.status = Status.ABERTA

    def concluir(self):
        self.status = Status.CONCLUIDA

    def to_dict(self):
        return {
            "id": self.id,
            "descricao": self.descricao,
            "origem": self.origem,
            "prioridade": self.prioridade.value,
            "responsavel": self.responsavel,
            "setor": self.setor,
            "data_criacao": self.data_criacao.isoformat(),
            "prazo": self.prazo,
            "status": self.status.value
        }

    @staticmethod
    def from_dict(d):
        obj = Demanda(
            d["descricao"],
            d["origem"],
            d["prioridade"],
            d["responsavel"],
            d["setor"],
            d.get("prazo")
        )
        obj.id = d["id"]
        obj.data_criacao = datetime.fromisoformat(d["data_criacao"])
        obj.status = Status(d["status"])
        return obj

    def __str__(self):
        return f"[{self.status.value.upper()}] {self.descricao} ({self.prioridade.value}) - {self.responsavel}"