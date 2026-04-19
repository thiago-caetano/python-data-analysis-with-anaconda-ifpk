# leiam uma palavra e verifiquem se ela contem as vogais
letra_a = 0
letra_e = 0
palavra = 'arare'
# input ("Digite uma palavra: ")

for letra in palavra:
    if letra == 'a' :
        letra_a += 1 
    elif letra == 'e':
        letra_e += 1
        
print (letra_a, letra_e)