# Crie um programa que receba o preço de um produto e um desconto percentual, e exiba o preço final com o desconto aplicado.

preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o percentual de desconto: "))

preco_final = preco - (preco * (desconto / 100))

print("Preço final com desconto:", preco_final)

