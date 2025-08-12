nome = input ("nome do funcionario(a): ")
valor = float(input("valor que recebe por hora: "))
horas_trabalhada = float(input("horas trabalhadas: "))
total = valor * horas_trabalhada
desconto = horas_trabalhada * 0.075
print(f"pagamento final : {total-desconto}")





