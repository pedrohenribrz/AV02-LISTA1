def divisao():
    try:
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite outro número: "))
    except ValueError:
        print("Digite apenas números inteiros!")
        return
    try:
        resultado = num1 / num2
        print(resultado)
    except ZeroDivisionError:
        print("Não é possível dividir por zero!")
divisao()
