def banco (saldo, valor, operacao):
    if operacao == "sacar":
        if valor <= saldo:
            saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente para realizar o saque.")
    elif operacao == "depositar":
        saldo += valor
        print("Depósito realizado com sucesso!")
    else:
        print("Operação inválida. Use 'sacar' ou 'depositar'.")
    return saldo

saldo_inicial = float(input("Digite o saldo inicial da conta: "))
operacao = input("Digite a operação (sacar/depositar): ").lower()

if operacao in ["sacar", "depositar"]:
    valor = float(input(f"Digite o valor a {operacao}: "))
    saldo_final = banco(saldo_inicial, valor, operacao)

print(f"Saldo final da conta: R${saldo_final:.2f}")
