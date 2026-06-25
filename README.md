1.  Introdução
Descrição

Este projeto consiste em um sistema desenvolvido em Python para gerenciamento de demandas de uma seção, permitindo o controle de solicitações com informações como:

- Descrição da demanda
- Origem
- Prioridade
- Responsável
- Setor
- Status
- Data de criação
- Prazo

O sistema foi desenvolvido utilizando os princípios de **Programação Orientada a Objetos (POO)**, com foco em organização, manutenção e escalabilidade.

2. Objetivo


Facilitar o controle de demandas administrativas ou operacionais, substituindo métodos manuais (como papel ou planilhas) e proporcionando:

- Rastreabilidade
- Organização
- Controle de responsabilidades
- Acompanhamento de status

3. Arquitetura do Projeto
    O projeto foi estruturado em camadas, seguindo boas práticas de desenvolvimento:

   projeto_demandas/
├── models.py        # Modelos (classes)
├── repository.py    # Persistência (JSON)
├── service.py       # Regras de negócio
├── main.py          # Interface CLI
└── tests.py         # Testes automatizados

5.  Funcionalidades:
   a)Cadastro de demandas  
   b)Listagem de demandas  
   c)Conclusão de demandas  
   d)Persistência em arquivo JSON  
   e) Filtro por status e responsável  
   f)Identificação única (UUID)  
   g) Controle de prioridade e status

6. Tecnologias utilizadas
- Python 3.x
- JSON (armazenamento)
- Programação Orientada a Objetos
- Enum (para controle de estados)
- UUID (identificação única)

  7.Como executar o projeto:
  
1 -> Clone o repositório:
  git clone https://github.com/seu-usuario/seu-repositorio.gitcd projeto_demandas
2 -> Execute o sistema: 
  python main.py

Autor: José Carlos Tumelero

Diagrama:



<img width="646" height="490" alt="Desenho 1" src="https://github.com/user-attachments/assets/ec68e5e1-17c2-46c3-a60f-9c04c7e11ba8" />


   
