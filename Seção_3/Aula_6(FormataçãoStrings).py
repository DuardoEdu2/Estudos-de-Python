nome = 'Edu'
altura = 1.80
peso = 86

linha_1 = 'nome tem altura de altura'

print(linha_1)

#f-strings
linha_1formatada = f'{nome} tem {altura:.2f} de altura'
linha_2formatada = f'pesa {peso} quilos'
print(linha_1formatada)
print(linha_2formatada)

print("-------------------------------------------------------------")
#Formatação com o metodo format

a = 'AAA'
b = 'BBB'
c = 8.1
string =  'a={nome1} a={nome1} a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(
    nome1 = a, nome2 = b, nome3 = c
)

print(formato)