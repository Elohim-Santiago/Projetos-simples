
calculo = 0 
media = 0
media_M = 0
media_F = 0
qtd_m = 0
qtd_f = 0
idade_m = 0
idade_f = 0
for P in range(1,11):
  print("{}ªpessoa".format(P))
  idade = int (input("Idade:"))
  sexo = str (input("sexo[M/F]:"))
  calculo = calculo + idade
  if (sexo == 'M' or sexo == 'm'):
      qtd_m = qtd_m + 1
      idade_m = idade_m + idade
  elif (sexo == 'F' or sexo == 'f'):
      qtd_f = qtd_f + 1
      idade_f = idade_f + idade
media_m = idade_m/qtd_m
media_f = idade_f/qtd_f
media = calculo/10
print("Média geral: {}".format(media))
print("Média homem: {}".format(media_m))
print("Média mulher: {}".format(media_f))
