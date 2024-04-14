menu = """

[a] Depositar
[b] Sacar
[c] Extrato
[d] Sair

=> """

from datetime import date

data_de_hoje = date.today()
saldo = 0
limite = 500
extrato = ""
lis = 1000
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "a":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "b":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo + lis

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "c":
        print(f"\n**********     {data_de_hoje.strftime('%d/%m/%Y')}     **********")
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.1f}")
        print(f"\nCheque Especial disponível: R${lis:.2f}")
        
        print("==========================================")

    elif opcao == "d":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    elif opcao == "d":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
