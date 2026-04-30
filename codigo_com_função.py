def processar_leituras():
    
    print("Ola! Bem vindo ao sistema da refinaria Delta-9.\nPara começar, insira os seus dados: ")
    
    nome_funcionario = input("Digite o seu nome: ").title()
    senha_funcionario = input("Digite a sua senha: ")
    
    print(f"Seja bem vindo {nome_funcionario}! Como está o seu trabalho?\nVamos para a atividade de seu turno ->")
    
    total_leituras = int(input("Digite o número de leituras: "))

    zonas_verdes = 0
    zonas_amarelas = 0
    zonas_vermelhas = 0

    soma = 0
    menor_valor = 0
    leituras_realizadas = 0

    zona_vermelha_anterior = 0
    travamento = 0 

    i = 0
    while i < total_leituras and travamento == 0:

        leitura = float(input(f"Leitura {i+1}: "))

        if leitura > 150:
            valor_ajustado = leitura + (leitura * 0.08)
            print(f"Aumento de 8%: {valor_ajustado:.2f}, houve uma expansão térmica.")
        else:
            valor_ajustado = leitura - (leitura * 0.04)
            print(f"Redução de 4%: {valor_ajustado:.2f}, houve uma contração térmica.")

        soma += valor_ajustado
        leituras_realizadas += 1

        if leituras_realizadas == 1 or valor_ajustado < menor_valor:
            menor_valor = valor_ajustado

        if 120 <= valor_ajustado <= 180:
            print("ZONA VERDE (Estável), continue nesse nível para manter a estabilidade.")
            zonas_verdes += 1
            zona_vermelha_anterior = 0

        elif valor_ajustado < 250:
            print("ZONA AMARELA (Oscilação), fique atento e tente voltar para a zona verde.")
            zonas_amarelas += 1
            zona_vermelha_anterior = 0

        else:
            print("ZONA VERMELHA (Crítica), retome imediatamente o controle!")
            zonas_vermelhas += 1

            if zona_vermelha_anterior == 1:
                print("TRAVAMENTO IMEDIATO!")
                travamento = 1 

            zona_vermelha_anterior = 1

        i += 1

    print("\n=== Resumo realizado no seu turno ===")
    print("Verdes:", zonas_verdes)
    print("Amarelas:", zonas_amarelas)
    print("Vermelhas:", zonas_vermelhas)

    if leituras_realizadas > 0:
        media = soma / leituras_realizadas
        porcentagem_verde = (zonas_verdes / leituras_realizadas) * 100

        print(f"\nMédia das pressões ajustadas: {media:.2f} UPC")
        print(f"Menor pressão registrada: {menor_valor:.2f} UPC")
        print(f"Porcentagem na zona verde: {porcentagem_verde:.2f}%")

    if travamento == 1:
        print("O sistema foi interrompido por medidas de segurança.")
        porcentagem_execucao = (leituras_realizadas / total_leituras) * 100
        print(f"Execução interrompida em {porcentagem_execucao:.2f}% das leituras")

    return nome_funcionario


def instrucoes_trabalho():
    print("\n=== Guia rápido do sistema ===")
    print("1. Insira valores corretamente.")
    print("2. O sistema ajusta automaticamente os valores.")
    print("3. Duas zonas vermelhas seguidas causam travamento.")
    print("4. Mantenha sempre na zona verde para estabilidade.")
    print("5. Zonas:")
    print("   - Verde: Estável.")
    print("   - Amarela: Atenção")
    print("   - Vermelha: Crítica\n")


def menu():
    opcao = ""
    nome_funcionario = ""
    
    while opcao != "3":
        print("\n====== MENU PRINCIPAL ======")
        print("1 - Iniciar leituras")
        print("2 - Ver instruções de trabalho")
        print("3 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_funcionario = processar_leituras()
        elif opcao == "2":
            instrucoes_trabalho()
        elif opcao == "3":
            if nome_funcionario:
                print(f"Encerrando sistema... Até mais {nome_funcionario}!")
            else:
                print("Encerrando sistema...")
        else:
            print("Opção inválida! Digite uma das opções válidas")

menu()