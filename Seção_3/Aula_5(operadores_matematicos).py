adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)

divisao = 10 / 3  # float
print('Divisão', divisao)

divisao_inteira = 10 // 3
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 59 % 5  # resto da divisão
print('Módulo', modulo)

print(10 % 8 == 0)
print(16 % 8 == 0)
print(10 % 2 == 0)
print(15 % 2 == 0)
print(16 % 2 == 0)

print('----------------------------------')
#propriedades dos sinais com strings

concatenacao = 'Edu' + 'Goiaba' + '81'
print(concatenacao)

a_dez_vezes = 'A' * 10
tres_vezes_edu = 3 * 'Edu'
print(a_dez_vezes)
print(tres_vezes_edu)

print('----------------------------------')
#precedencias dos operadores

conta_1 = 1 + 1 ** 5 + 5 # 7
conta_1correta = (1 + 1) ** (5 +5) #1024
conta_2 = (5 * int(0.3 + 2.7)) ** (1 + 1)
print(conta_1)
print(conta_1correta)
print(conta_2)

print('----------------------------------')
#IMC
#EXERCICIO:

nome = 'Edu'
altura = 1.80
peso = 86
imc = peso / (altura ** 2)

print(nome, "possui", altura, "metros de altura e pesa", peso, "quilos")
print("seu IMC é: ", imc)

#print('Na tabela voce esta localizado em: ')

'''
match imc:
    case list(range(0, 18,5, 0.1)):
         print("Abaixo do peso")
    case list(range(18.6, 24.9, 0.1)):
         print("Peso ideal")
    case list(range(25.0,29.9,0.1)):
         print("levemente acima do peso")
    case list(range(30.0, 34.9, 0.1)):
         print("obasidade level I")
    case list(range(35.0, 39.9, 0.1)):
         print("obasidade level II")
    case list(range(40.0, 100.9, 0.1)):
         print("obasidade level III")
    case _:
        print("Insira seus dados corretamente")
'''

