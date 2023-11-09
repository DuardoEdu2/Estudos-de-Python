# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool são tipos primitivos

"""
por causa de que o python é uma liguagem do tipo forte
ele não consegue fazer a conversão de tipos de dados diferentes ex int e string na fase de procesamento
por isso que nos temos que converter de ante-mão.
"""

#EXEMPLOS:

# print('1' + 1) #ERROR
print(1 + 1) #=2
print('a' + 'b') #='ab'

#o sinal de mais + passa por um processo de polimorfismo
#significa que ele age diferente dependendo do data type
#somando os int's e cocatenando strings.

#CONVERSÕES:

print(int('1') + 1) #=2
print(str(1) + '1') #'11'
print(float(1) + 0.1) #1.1 type class float

print(type(int('1') + 1)) 
print(type(str(1) + '1'))
print(type(float(1) + 0.1))

