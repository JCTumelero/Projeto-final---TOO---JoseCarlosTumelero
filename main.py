from repositorio import DemandaRepositorio
from servico import DemandaServico

repo = DemandaRepositorio()
servico = DemandaServico(repo)

def menu():
    while True:
        print("\n--- SISTEMA DE DEMANDAS ---")
        print("1 - Adicionar demanda")
        print("2 - Listar demandas")
        print("3 - Concluir demanda")
        print("4 - Sair")

        op = input("Escolha: ")

        if op == "1":
            desc = input("Descrição: ")
            origem = input("Origem: ")
            prioridade = input("Prioridade (alta/media/baixa): ")
            resp = input("Responsável: ")
            setor = input("Setor: ")

            servico.adicionar(desc, origem, prioridade, resp, setor)

        elif op == "2":
            for d in servico.listar():
                print(d)

        elif op == "3":
            id_d = input("ID da demanda: ")
            servico.concluir(id_d)

        elif op == "4":
            break


if __name__ == "__main__":
    menu()