"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
horas = input("Que horas brasileiras são: ")


if horas.isdigit() :
    horasV = float(horas)
    if horasV >= 0 and horasV <= 11.59 :
        print("Bom Dia e Compania, ganhar playstation")
    elif horasV >= 12 and horasV <= 17.59 :
        print('Boa Tarde Negada, tirar cochilo')
    elif horasV >= 18 and horasV <= 23.59 :
        print("Boa Noite Galera, bó Madrugar")
else :
    print("digite apenas numeros")
"""

horas = input("Que horas brasileiras são: ")



try:
    horasV = int(horas)
    if horasV >= 0 and horasV <= 11 :
        print("Bom Dia e Compania, ganhar playstation")
    elif horasV >= 12 and horasV <= 17 :
        print('Boa Tarde Negada, tirar cochilo')
    elif horasV >= 18 and horasV <= 23 :
        print("Boa Noite Galera, bó Madrugar")
    else :
        print("digite apenas numeros entre 0 e 23")
except:
    print("voce não digitou um numero inteiro")
