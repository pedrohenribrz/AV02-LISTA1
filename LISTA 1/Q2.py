def notas(provas):
    media = sum(provas) / len(provas)
    return media

lista = []

while True:
    try:
        nota = float(input("Digite a nota da prova (ou -1 para sair): "))
        if nota == -1:
            break
        elif 0 <= nota <= 10:
            lista.append(nota)
        else:
            print("Nota inválida! Digite uma nota entre 0 e 10.")
    except ValueError:
        print("Digite apenas números válidos!")

media = notas(lista)
print(f"A média das notas é: {media:.2f}")
