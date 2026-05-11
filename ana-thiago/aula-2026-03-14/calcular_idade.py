#faça um programa que o usuario digite o ano que nasceu e a aplicação
# retorne a idade

from datetime import date

nome = input ('olá, digite o seu nome: ')
ano_nascimento = int (input (f"{nome}, em que ano que você nasceu: "))
# ano_atual = 2026
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print ('Você tem', idade, 'anos de vida')

