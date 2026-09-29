def aprovados(notas):
    aprovados = []
    for nota in notas:
        if nota >= 7:
            aprovados.append(nota)
    return aprovados

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

resultado = aprovados(lista)
if resultado:
    print("Nota dos aprovados:")
    for nota in resultado:
        print(nota, end=" ")