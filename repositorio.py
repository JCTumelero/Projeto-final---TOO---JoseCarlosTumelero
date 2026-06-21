import json
from modelo import Demanda

class DemandaRepositorio:
    def __init__(self, path="demandas.json"):
        self.path = path

    def salvar(self, demandas):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump([d.to_dict() for d in demandas], f, indent=4, ensure_ascii=False)

    def carregar(self):
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                dados = json.load(f)
                return [Demanda.from_dict(d) for d in dados]
        except FileNotFoundError:
            return []