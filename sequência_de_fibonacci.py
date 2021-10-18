
N = int (input("Digite o numero:"))
print("_________________________________________________________________________")

T = 1
T2 = 1
cont = 0

sequencia = [0,1,1]
for x in range(2, N):
  cont = T + T2
  T = cont
  T2 = (cont - T2)
  sequencia.append(cont)

print("sequencia:", sequencia)
print("_________________________________________________________________________")
print("Fim do programa :)")
