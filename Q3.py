def verificar_horas(horas):
    if horas >= 40:
        return "Carga completa"
    else:
        return "Carga incompleta"
horas_trabalhadas = float(input("Digite as horas trabalhadas: "))
print(verificar_horas(horas_trabalhadas))
