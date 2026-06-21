from modelo import Demanda
from repositorio import DemandaRepositorio
from servico import DemandaServico


def test_criar_demanda():
    d = Demanda("Teste", "Email", "alta", "João", "Financeiro")
    assert d.descricao == "Teste"
    assert d.status.value == "aberta"


def teste_to_dict():
    d = Demanda("Teste", "Email", "alta", "João", "Financeiro")
    data = d.to_dict()
    assert data["descricao"] == "Teste"


def teste_repositorio(tmp_path):
    repo = DemandaRepositorio(tmp_path / "teste.json")

    demandas = [Demanda("Teste", "Email", "alta", "João", "Financeiro")]
    repo.salvar(demandas)

    carregadas = repo.carregar()
    assert len(carregadas) == 1


def test_service():
    repo = DemandaRepositorio("teste.json")
    service = DemandaServico(repo)

    service.adicionar("Teste", "Email", "alta", "João", "Financeiro")
    assert len(service.listar()) >= 1
