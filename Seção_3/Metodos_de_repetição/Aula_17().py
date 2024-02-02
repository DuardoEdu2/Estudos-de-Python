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


qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas :
        print(f"{linha=}, {coluna=}")
        coluna += 1
    linha += 1
print("Acabou")