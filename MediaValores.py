qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while (valor > 0.0):
    soma = soma + valor
    qtd = qtd + 1
    #entrada de valores
    valor = float(input("Digite um valor: "))

#caso digite um valor negativo o laço encerra
media = soma / qtd
print("\nTotal da soma: ", soma)
print("\nQuantidade de valores: ", qtd)
print("\nMédia dos valores: ", media)
