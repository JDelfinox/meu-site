print("Desafio 1")
Mensagem = "Alô mundo"
print(Mensagem)
print()

print("Desafio 2")
primeiro_numero = int(input("Informe um número: "))
print(primeiro_numero)
print()

print("Desafio 3")
def somar(a,b):
    return a+b

primeiro_numero = int(input("Primeiro numero: "))
segundo_numero = int(input("Segundo numero: "))
resultado = somar(primeiro_numero, segundo_numero)
print(resultado)
print()

print("Desafio 4")
def media(a,b,c,d):
    return (a+b+c+d)/4

primeiro_numero = int(input("Primeiro numero: "))
segundo_numero = int(input("Segundo numero: "))
terceiro_numero = int(input("Terceiro numero:"))
quarto_numero = int(input("Quarto numero:"))
resultado = media(primeiro_numero, segundo_numero, terceiro_numero, quarto_numero)
print(resultado)
print()

print("Desafio 5")
def conversao(a):
    return a * 100

primeiro_numero = int(input("Informe seu numero: "))
resultado = conversao(primeiro_numero)
print(resultado)
print()

print("Desafio 6")
def area(a):
    return a*a*3.14

primeiro_numero = int(input("Informe seu Raio:"))
resultado = area(primeiro_numero)
print(resultado)
print()

print("Desafio 7")
def areaq(a):
    return (a*a) * 2

primeiro_numero = int(input("Quanto vale o lado do Quadrado:"))
resultado = areaq(primeiro_numero)
print(resultado)
print()

print("Desafio 8")
def trabalho(a,b):
    return a*b

primeiro_numero = float(input("Quanto você ganha por hora?"))
segundo_numero = int(input("Quantas horas por mês você trabalha?"))
resultado = trabalho(primeiro_numero, segundo_numero)
print(resultado)
print()

print("Desafio 9")
print()

def celsius(a):
    return 5 * ((a - 32) / 9)

primeiro_numero = float(input("Temperatura em Fahrenheit:"))
resultado = celsius(primeiro_numero)
print(resultado)
print()


print("Desafio 10")
print()

def fahreinheit(a):
    return (a * 1.8) + 32
primeiro_numero = float(input("Temperatura em Celsius:"))
resultado = fahreinheit(primeiro_numero)
print(resultado)
print()

print("Desafio 11")
print()

def calculos(a,b,c):
    return (2*a) * (b/2), (3*a) + c, c*c*c
primeiro_numero = int(input("Qual o valor:"))
segundo_numero = int(input("Qual o valor:"))
terceiro_numero = float(input("Qual o valor:"))
resultado = calculos(primeiro_numero,segundo_numero,terceiro_numero)
print(resultado)
print()

print("Desafio 12")
print()

def peso(a):
    return (72.7 * a ) - 58
primeiro_numero = float(input("Qual sua Altura?"))
resultado = peso(primeiro_numero)
print(resultado)

print("Desafio 13")
print()
def peso(a):
    return (72.7 * a ) - 58, (62.1 * a) - 44.7
primeiro_numero = float(input("Qual sua Altura?"))
resultado = peso(primeiro_numero)
print(resultado)




 