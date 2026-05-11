# ler o valor de um pagamento e aplicar juros de 
# 10% se o valor for menor que R$ 457,67
# 20% se for maior

pagamento = float (input ("Digite o valor do pagamento: "))

valor_com_juros = pagamento * 1.2 if pagamento >= 457.67 else pagamento * 1.1

print (f"O prejuizo foi de R$ {valor_com_juros}")
print (f"O prejuizo foi de R$ {pagamento * 1.2 if pagamento >= 457.67 
                                                  else pagamento * 1.1}")
