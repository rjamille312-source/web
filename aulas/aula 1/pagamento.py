saldo_disponivel = 1000.00

valor_saque = float (input("qual valor deseja sacar"))

if valor_saque < saldo_disponivel:
    saldo_disponivel = saldo_disponivel - valor_saque
    print(f"saque")
    