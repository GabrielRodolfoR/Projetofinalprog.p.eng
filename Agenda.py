tarefas = []

while True:
    print(f"Bem-vindo a agenda excluiva para alunos SATC!")
    print(f"Vou te dar algumas opções, assim que decidir o que quer fazer é só digitar o número no campo de escolha!")
    print(f"1 - Agendar novas tarefas")
    print(f"2 - Visualizar suas tarefas")
    print(f"3 - Alterar tarefas  ")
    print(f"4 - Excluir tarefas ")
    print(f"5 - Sair")
    opcao = int(input(f"Digite a opção desejada: "))

    if (opcao == 0) or (opcao > 5):
        print(f"Número escolhido não é válido, tente novamente.")

    elif (opcao == 5):
        break;

    elif (opcao == 1):
        print(f"Digite as informações para o cadastro de sua tarefa: ")
        nome = input("Digite o nome da tarefa: ")
        prioridade = input("Digite a prioridade (A para Alta, M para Média ou B para Baixa): ")
        prazo = int(input("Digite a data a ser entregue sem as barras (ex: 25062025): "))
        descricao = input("Digite a descrição da tarefa: ")

        nome_up = nome.upper
        prioridade_up = prioridade.upper
        descricao_up = descricao.upper

        nova_tarefa = {
            "nome": nome_up,
            "prioridade": prioridade_up,
            "prazo": prazo,
            "descricao": descricao_up
        }

        tarefas.append(nova_tarefa)
        print("Tarefa adicionada com sucesso!")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\n Lista de Tarefas:")
            for i, tarefa in enumerate(tarefas):
                print(f"\nTarefa {i+1}:")
                print(f"  Nome: {tarefa['nome']}")
                print(f"  Prioridade: {tarefa['prioridade']}")
                print(f"  Prazo: {tarefa['prazo']}")
                print(f"  Descrição: {tarefa['descricao']}")
