
#iterando strings com while

nome = "Eduardo"
cont = 0
tamanho_nome = len(nome)

print(nome)
print(tamanho_nome)
print(nome[3])

while cont < tamanho_nome :
    print(f"*{nome[cont]}", end="")
    cont += 1

