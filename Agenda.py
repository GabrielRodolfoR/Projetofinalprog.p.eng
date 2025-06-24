from datetime import datetime

tarefas = []

def mostrar_tarefas():
    print("\n" + "="*140)
    print("\n Lista de Tarefas:")
    for i, tarefa in enumerate(tarefas):
        print(f"\nTarefa {i+1}:")
        print(f"  Nome: {tarefa['nome']}")
        print(f"  Prioridade: {tarefa['prioridade']}")
        print(f"  Prazo: {tarefa['dia']}/{tarefa['mes']}/{tarefa['ano']}")
        print(f"  Descrição: {tarefa['descricao']}")
    print("\n" + "="*140)

while True:
    print(f"\nBem-vindo à agenda exclusiva para alunos SATC!")
    print(f"1 - Agendar novas tarefas")
    print(f"2 - Visualizar tarefas")
    print(f"3 - Alterar tarefas")
    print(f"4 - Excluir tarefas")
    print(f"5 - Sair")

    try:
        opcao = int(input(f"Digite a opção desejada: "))
    except ValueError:
        print("Entrada inválida! Digite um número de 1 a 5.")
        continue

    if not (1 <= opcao <= 5):
        print(f"Número escolhido não é válido, tente novamente.")
        continue

    elif opcao == 1:
        print(f"\nDigite as informações para o cadastro de sua tarefa!")
        nome = input("Digite o nome da tarefa: ").strip()
        prioridade = input("Digite a sigla da prioridade (A para Alta, M para Média ou B para Baixa): ").strip().upper()

        while prioridade not in ["A", "M", "B"]:
            print("Prioridade inválida, digite novamente!")
            prioridade = input("Digite a sigla da prioridade (A, M ou B): ").strip().upper()

        try:
            dia = int(input("Digite o dia do prazo a ser entregue: "))
            mes = int(input("Digite o mês do prazo a ser entregue: "))
            ano = int(input("Digite o ano do prazo a ser entregue: "))
            datetime(year=ano, month=mes, day=dia)  # valida a data
        except ValueError:
            print("Data inválida.")
            continue

        descricao = input("Digite a descrição da tarefa: ").strip()

        nova_tarefa = {
            "nome": nome.upper(),
            "prioridade": prioridade,
            "dia": dia,
            "mes": mes,
            "ano": ano,
            "descricao": descricao.upper()
        }

        tarefas.append(nova_tarefa)
        print("\nTarefa adicionada com sucesso!")
        print("\n" + "="*140)

    elif opcao == 2:
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
            continue

        print("\nComo deseja visualizar as tarefas?")
        print("1 - Listar todas")
        print("2 - Filtrar por prioridade")
        print("3 - Filtrar por data de entrega")

        try:
            sub_opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida.")
            continue

        if sub_opcao == 1:
            mostrar_tarefas()

        elif sub_opcao == 2:
            prioridade_filtro = input("\nDigite a prioridade para filtrar (A, M ou B): ").strip().upper()
            while prioridade_filtro not in ["A", "M", "B"]:
                prioridade_filtro = input("\nPrioridade inválida. Digite A, M ou B: ").strip().upper()

            tarefas_filtradas = [t for t in tarefas if t["prioridade"] == prioridade_filtro]
            if not tarefas_filtradas:
                print(f"Nenhuma tarefa com prioridade {prioridade_filtro}.")
            else:
                print("\n" + "="*140)
                print(f"\nTarefas com prioridade {prioridade_filtro}:")
                for i, tarefa in enumerate(tarefas_filtradas):
                    print(f"\nTarefa {i+1}:")
                    print(f"  Nome: {tarefa['nome']}")
                    print(f"  Prioridade: {tarefa['prioridade']}")
                    print(f"  Prazo: {tarefa['dia']}/{tarefa['mes']}/{tarefa['ano']}")
                    print(f"  Descrição: {tarefa['descricao']}")
                print("\n" + "="*140)

        elif sub_opcao == 3:
            try:
                dia = int(input("Digite o dia: "))
                mes = int(input("Digite o mês: "))
                ano = int(input("Digite o ano: "))
                datetime(year=ano, month=mes, day=dia)
            except ValueError:
                print("Data inválida.")
                continue

            tarefas_filtradas = [
                t for t in tarefas if t["dia"] == dia and t["mes"] == mes and t["ano"] == ano
            ]
            if not tarefas_filtradas:
                print("Nenhuma tarefa com essa data de entrega.")
            else:
                print("\n" + "="*140)
                print(f"\nTarefas com entrega para {dia}/{mes}/{ano}:")
                for i, tarefa in enumerate(tarefas_filtradas):
                    print(f"\nTarefa {i+1}:")
                    print(f"  Nome: {tarefa['nome']}")
                    print(f"  Prioridade: {tarefa['prioridade']}")
                    print(f"  Prazo: {tarefa['dia']}/{tarefa['mes']}/{tarefa['ano']}")
                    print(f"  Descrição: {tarefa['descricao']}")
                print("\n" + "="*140)
        else:
            print("Opção inválida.")


    elif opcao == 3:
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
            continue

        mostrar_tarefas()

        try:
            op_alterar_tarefa = int(input("\nDigite o número da tarefa que você deseja alterar: "))
            if not (1 <= op_alterar_tarefa <= len(tarefas)):
                print("Número de tarefa inválido.")
                continue
        except ValueError:
            print("Entrada inválida! Digite um número.")
            continue

        print("Digite o que deseja alterar:")
        print("1 - Data")
        print("2 - Nome")
        print("3 - Descrição")
        print("4 - Prioridade")

        while True:
            try:
                op = int(input("\nDigite aqui o número da opção desejada: "))
                if 1 <= op <= 4:
                    break
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Entrada inválida! Digite um número.")

        index = op_alterar_tarefa - 1

        if op == 1:
            print("Escolha o que deseja alterar:")
            print("1 - Dia, mês e ano")
            print("2 - Dia e mês")
            print("3 - Mês e ano")
            print("4 - Dia")
            print("5 - Mês")
            print("6 - Ano")

            while True:
                try:
                    opcao_data = int(input("Digite a opção desejada: "))
                    if 1 <= opcao_data <= 6:
                        break
                    else:
                        print("Opção inválida!")
                except ValueError:
                    print("Entrada inválida!")

            try:
                if opcao_data == 1:
                    dia = int(input("Novo dia: "))
                    mes = int(input("Novo mês: "))
                    ano = int(input("Novo ano: "))
                elif opcao_data == 2:
                    dia = int(input("Novo dia: "))
                    mes = int(input("Novo mês: "))
                    ano = tarefas[index]["ano"]
                elif opcao_data == 3:
                    mes = int(input("Novo mês: "))
                    ano = int(input("Novo ano: "))
                    dia = tarefas[index]["dia"]
                elif opcao_data == 4:
                    dia = int(input("Novo dia: "))
                    mes = tarefas[index]["mes"]
                    ano = tarefas[index]["ano"]
                elif opcao_data == 5:
                    mes = int(input("Novo mês: "))
                    dia = tarefas[index]["dia"]
                    ano = tarefas[index]["ano"]
                elif opcao_data == 6:
                    ano = int(input("Novo ano: "))
                    dia = tarefas[index]["dia"]
                    mes = tarefas[index]["mes"]

                datetime(year=ano, month=mes, day=dia)  # valida data
                tarefas[index]["dia"] = dia
                tarefas[index]["mes"] = mes
                tarefas[index]["ano"] = ano
                print("Data alterada com sucesso!")
                print("\n" + "="*140)

            except ValueError:
                print("Data inválida. Alteração cancelada.")

        elif op == 2:
            novo_nome = input("Digite o novo nome da tarefa: ").strip().upper()
            tarefas[index]["nome"] = novo_nome
            print("\nNome alterado com sucesso!")
            print("\n" + "="*140)

        elif op == 3:
            nova_descricao = input("Digite a nova descrição: ").strip().upper()
            tarefas[index]["descricao"] = nova_descricao
            print("\nDescrição alterada com sucesso!")
            print("\n" + "="*140)

        elif op == 4:
            nova_prioridade = input("Digite a nova prioridade (A, M ou B): ").strip().upper()
            while nova_prioridade not in ["A", "M", "B"]:
                nova_prioridade = input("Prioridade inválida. Digite A, M ou B: ").strip().upper()
            tarefas[index]["prioridade"] = nova_prioridade
            print("Prioridade alterada com sucesso!")
            print("\n" + "="*140)

    elif opcao == 4:
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
            continue

        mostrar_tarefas()

        try:
            op_excluir = int(input("\nDigite o número da tarefa que deseja excluir: "))
            if not (1 <= op_excluir <= len(tarefas)):
                print("Número de tarefa inválido.")
                continue
        except ValueError:
            print("Entrada inválida! Digite um número.")
            continue

        op_certeza = input(f"\nTem certeza que deseja excluir a tarefa {op_excluir}? (S/N): ").strip().upper()
        while op_certeza not in ["S", "N"]:
            op_certeza = input("Digite S para sim ou N para não: ").strip().upper()

        if op_certeza == "S":
            tarefas.pop(op_excluir - 1)
            print("\nTarefa excluída com sucesso!")
            print("\n" + "="*140)
        else:
            print("Certo, nenhuma tarefa será excluída.")

    elif opcao == 5:
        print("Encerrando a agenda. Até mais!")
        break
