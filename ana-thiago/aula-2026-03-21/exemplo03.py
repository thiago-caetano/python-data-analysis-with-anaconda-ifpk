inicio = int (input ('Digite o valor inicial: '))
termino = int (input ('Digite o valor final: '))
passo = int (input ('Digite o passo (incremento): '))

if passo == 0:
    print ('Valor do passo inválido')
else:
    if termino == inicio:
        print ('Valores iguais, não há loop')
    else:
        if (termino < inicio and passo > 0) or (termino > inicio and passo < 0):
            print('valor do passo inválido')
        else:
            for i in range (inicio, termino, passo):
                print (i)