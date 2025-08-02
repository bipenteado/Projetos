menu = """

Informe o que deseja realizar:

[s] Sacar
[d] Depositar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saqueS = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor que deseja depositar:"))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print ("Operação falhou, o valor desejado é inválido.")

    elif opcao == "s":
        valor = float (input("Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo
    
        excedeu_limite = valor > limite

        excedeu_saques = numero_saqueS >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo Insuficiente!")

        elif excedeu_limite:
            print ("Saque desejado excede o limite!")

        elif excedeu_saques:
            print("Número máximo de saque atingido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numero_saqueS += 1

        else:    
            print("Operação Inválida!")

    elif opcao =="e":
        print("============ Extrato ============")
        print("Não foram realizadas movimentações!" if not extrato else extrato)
        print(f"Saldo: R$ {saldo: .2f}")
        print("=================================")
    
    elif opcao =="q":
        break

    else:
        print ("Operação inválida, tente novamente!")





              





