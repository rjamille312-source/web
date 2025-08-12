nome = input("informe seu nome completo: ")
idade = float (input("informe sua idade"))
endereco = input("informe seu endereco:")           
estado_civil = input("informe seu estado civil:")
escolaridade = input("informe sua escolaridade:")
salario1 = float (input("informe o salario"))
salario2 = float (input("informe o salario"))
salario3 = float (input("informe o salario"))

salario_media= (salario1 + salario2 + salario3 )/ 3
diferenca_salario= (salario1 - salario2)

print (f"A Media salarial do usuario é: {salario_media}")
print (f"A diferenca entre a media salarial do usuario é: {diferenca_salario}")
