nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

#calcular media
mediaFinal = (nota1 + nota2) / 2

#verificação
if(mediaFinal > 7.0):
    print("A média %.1f - Aprovado"%mediaFinal)
else:
    print("A média: %.1f - Reprovado"%mediaFinal)