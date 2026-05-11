# entre com 3 notas e calcule a média. 

# nota1 = float(input('Digite 1 a nota: '))
# nota2 = float(input('Digite 2 a nota: '))
# nota3 = float(input('Digite 3 a nota: '))

# media = (nota1 + nota2 + nota3) /3

# print (f"A sua média é : {media}")

media = 11

if media == 10:
    print('Aprovado com louvor')
elif media >=7 and media <10:
    print ('Aprovado')
elif media >= 5 and media <7:
    print ('Recuperação')
elif media >=0 and media <5:
    print ('Reprovado')
else:
    print ('média incorreta')