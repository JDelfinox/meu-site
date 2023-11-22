print("D1")
n = int(input("Digite um número inteiro: "))
soma = 0
for i in range(2, n+1, 2):
    soma += i
print(soma, "\n")



print("D2")
n = int(input("Digite um número: "))

from time import sleep
for contagem in range(n,0,-1):
   print(contagem)
   sleep(1)
print("Acabou seu Tempo!!!")



print('D3')
quantidade = int(input("Insira a quantidade de notas: "))
abuabu = []
for x in range(quantidade):
    c = int(input("Digite a nota: "))
    abuabu.append(c)
soma_das_notas = sum(abuabu)
print(soma_das_notas/quantidade)



print("D4")
l = {5}
n = int(input("Acerte o número de 1 a 10: "))
if n in l:
   print("Acertou!", "\n")

else:
   print("Errou!", "\n") 



print("D5")
tabuada=int(input("Tabuada do numero: "))

for count in range(10):
   print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)))