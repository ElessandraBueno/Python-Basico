A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

if (A>B):
    aux = A;
    A = B;
    B = aux;
print("O valor de A agora é: ", A);
print("O valor de B agora é: ", B);