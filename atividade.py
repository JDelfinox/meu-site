# def soma(a,b):
#     return a+b
    


# primeiro_numero = int(input("Primeiro numero: "))
# segundo_numero = int(input("Segundo numero: "))
# terceiro_numero = int(input("Terceiro numero: "))
# quarto_numero = int(input("Quarto numero: "))
# quinto_numero  = int(input("Quinto numero: "))
# sexto_numero   = int(input("Sexto numero: "))
# setimo_numero  = int(input("Setimo numero: "))
# oitavo_numero  = int(input("Oitavo numero: "))
# resultado = soma(primeiro_numero, segundo_numero,)
# resultado1 = soma(terceiro_numero, quarto_numero)
# resultado2 = soma(quinto_numero, sexto_numero)
# resultado3 = soma(setimo_numero, oitavo_numero)
# print( resultado, "\n", resultado1, "\n", resultado2,"\n", resultado3)

# def exercicio_1(n):
#     for i in range(n):
#         i += 1
#         print(str(i) * i)


# n = int(input('Digite um número: '))
# exercicio_1(n)

# def tres(a,b,c):
#     return a+b+c
# primeiro_numero = int(input("Primeiro numero: "))
# segundo_numero = int(input("Segundo numero: "))
# terceiro_numero = int(input("Terceiro numero: "))

# resultado = tres(primeiro_numero, segundo_numero, terceiro_numero)
# print(resultado)

# def sinal(n):
#     if n>0:
#         return 'P'
#     else:
#         return "N"
# primeiro_numero = int(input("Primeiro numero: "))
# resultado = sinal(primeiro_numero)
# print(resultado)

def somaimposto(a,b):
    return round(a * (1 + ( b/100)))

custo = float(input("Quanto custa seu produto?: "))
taxa = float(input("Qual a taxa? (em porcentagem): "))

resultado = somaimposto(custo, taxa)
print(resultado)




    
    


