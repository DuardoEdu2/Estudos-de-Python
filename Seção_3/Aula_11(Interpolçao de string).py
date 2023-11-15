
"""
forma de formatação de string com data types diferentes
funciona que nem em C criando um espaco de data type usando a porcentagem e as letrinhas
e depois preenche com os valores.
"""

nome = "Edu"
preco = 1000.95897643
variavel = "%s o Preço é R$%.2f" % (nome, preco)
print(variavel)


#-------------------------------------------------------------------------------------------------------------
"""
formatação básica de strings
conceitos extras do metodo de formatação f strings
> - Esquerda
< - Direita
^ - Centro
Conversion flags - !r !s !a
"""

variavel = "ABC"
print(f"{variavel}")
print(f"{variavel:3^10}.")
print(f"{1000.1001923:0<+10,.3f}")
print(f"O hexadecimal de 1500 é {1500:08X}")

#-------------------------------------------------------------------------------------------------------------

#Fatiamento de strings]
#Fatiamento [i:f:p] [::] 
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
# idexes positivos = 0,1,2,3,4,5,6,7,8,9
# idexes negativos = -9,-8,-7,-6,-5,-4,-3,-2,-1

variavel = "HelloWorld"
#Fatiamento    \/
print(variavel[5:8])
print(variavel[0:8:2])
print(variavel[5:8])
print(len(variavel[1:5]))
print(variavel[0:len(variavel):1])
#inverte
print(variavel[::-1])












