"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

condicao = False
passou_no_if = None

if condicao :
    passou_no_if = True
    print('Faça algo')
else : 
    print('Não faça algo')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

#caso o seu if esteja em outro lugar do aplicativo
#e voce queira saber se ele passou ou não pela condição
#sem ter que procurar voce pode usar a flag que esta no if ("passou_no_if") é uma flag

if passou_no_if is None:
    print("ele não passou pelo if")
else :
    print("ele passou pelo if")
