
numero = 1
calculo = 0
quant = 0
Maior = 0
Menor = 0
while numero != 0:
  numero = float (input("Digite o numero:"))
  calculo = (calculo + numero)
  if quant == 1:
      Maior = Menor = numero
  else:  
    if numero > Maior:
       Maior = numero 
    if numero < Menor:
       Menor = numero
    if Menor == 0:
       Menor = numero  
print("calculo:", calculo)
print(" Maior numero: {}  \n Menor numero:{}".format(Maior, Menor))
print("Fim do programa :(")
