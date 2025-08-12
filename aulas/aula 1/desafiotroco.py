preco_unitario= float (input("informe o preco unitario do produto: "))
unidade = float (input ("informe a quantidade comprada: "))
valor_cliente = float (input("informe o valor pago: "))

valor_total= preco_unitario * unidade
troco = valor_cliente - valor_total

print(f"troco a ser devolvido ao cliente: {troco}")

