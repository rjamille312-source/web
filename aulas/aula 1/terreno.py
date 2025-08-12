largura = float(input("Informe o valor da largura: "))
comprimento = float (input("Informe o valor da comprimento: "))
preco_metro = float (input("informe o preço do metro quadrado"))

area = largura * comprimento
preco_total = area * preco_metro

print(f"area: {area}")
print(f"preco_total: {preco_total}")
