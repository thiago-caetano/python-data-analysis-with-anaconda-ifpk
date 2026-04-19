from funcoes import *
# from funcoes import calcular_media_lista

print('oi pessoal !!!!!!!')
numero1 = 86745
numero2 = 567
numeros = [950, 2110, 1500, 940000000000000000, 2021, 0.15, 69, 1046]
print (f"{calcular_media(numero1, numero2):.4f}")
media_lista = calcular_media_lista(numeros)

print(f" A média é : {media_lista:,.3f}")