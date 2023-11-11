
primeiro_valor = input('Digite um valor: ')
Segundo_valor = input('Digite outro valor: ')

primeiro_valorV = primeiro_valor.isdigit()
Segundo_valorV = Segundo_valor.isdigit()

if primeiro_valorV == True and Segundo_valorV == True :
    if int(primeiro_valor) > int(Segundo_valor) :
        print(f"O primeiro valor {primeiro_valor} é maior do que o segundo {Segundo_valor}")
    else : 
        print(f"O segundo valor {Segundo_valor} é maior do que o primeiro valor {primeiro_valor}")
else :
    print("Digite apenas numeros.")

print("Fim")



