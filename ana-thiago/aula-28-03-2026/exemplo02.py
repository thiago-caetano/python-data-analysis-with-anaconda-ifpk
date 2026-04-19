nomes = ['Bianca','Adrine', 'Lucas', 'Enzo', 'Bianca', 'Gerson','Bianca']


for nome in nomes[:]:  # cópia
    if nome == 'Bianca':
        nomes.remove(nome)
        print(nomes)
