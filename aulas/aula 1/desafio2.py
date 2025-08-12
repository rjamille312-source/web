nota1 = float (input("digite a nota 1"))
nota2 = float (input("digite a nota 2"))
nota3 = float (input("digite a nota 3"))

media =(nota1 + nota2 + nota3)/3

if media >=7:
 print("aprovado")
elif media <6:
 print("reprovado")
else:
 print("recuperação")
 
 print (f"a media do aluno foi de {media:.2f}")
 

