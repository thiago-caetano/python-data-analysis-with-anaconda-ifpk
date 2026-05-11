from pessoas import pessoas

# for chave in pessoas:
#     print (chave)
    
# for valor in pessoas.values():
#     print (valor)
    
# for chave, valor in pessoas.items():
#     print (chave, valor)
    
# for chave, valor in pessoas.items():
#     print (valor["nome"], valor["idade"])
    
# for chave, valor in pessoas.items():
#     for campo, dado in valor.items():
#         print (chave, campo, dado)
        
for pessoa in pessoas.values():
    if pessoa["idade"] >= 30:
        print (pessoa["nome"])