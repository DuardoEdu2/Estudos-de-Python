"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

####Operadores de atribuição
####+=, -=, *=, /=, //=, **=, %=

#Dica de eduardo: quando voce quiser repetir palavras com um cont = 0 usa so o operador de menor <
#se voce for printar numeros usa o operador de menor igual <=.

condicao = True
cont = 0
while cont <= 100:
    cont += 1

    if cont == 6 :
        print('"6"')
        continue
    
    if cont >= 10 and cont <= 27 :
        print(f"não vou mostra o {cont}")
        continue
    
    print(cont)
    
    if cont == 90 :
        break

print("Eai")

"""
while condicao :
    nome = input("Qual seu nome: ")
    print(f"Seu nome é {nome}")

    if nome == 'sair' :
        break

print("eaei")
"""




