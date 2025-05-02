nome = 'Xander Ricardo'
altura = 1.80
peso = 60
imc = peso / altura ** 2


#f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso:.2f} quilos e seu imc é {imc:.2f}'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)

print(nome, 'tem', altura, 'de altura',)
print('pesa', peso, 'quilos e seu imc é',)
print(imc)