fatorial = 0
fat = 0
numero = int(input("Digite o número: "))
if numero == 0: 
    print("Fatorial de 0 é = 1")
if numero < 0:
    print("Não existe fatorial negativo")
else:
    fatorial = numero
    while numero >1:
        numero-=1
        fatorial*= numero

    print("Fatorial: ", fatorial)
