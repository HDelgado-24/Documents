#Actividad 1
pizzas = ["barbacoa", "margarita", "prosciutto", "romana"]
numLin1 = 0
while numLin1 <= 3:
    print(f'Me gusta la pizza {pizzas[numLin1]}.')
    numLin1 = numLin1+ 1
print("Me encantan las pizzas.")
print()


#Actividad 2
numusu = int(input("Inserte un número entero positivo: "))
n = 1
if numusu > 0:
    while n <= numusu:
        print(f'{n}')
        n = n+2
else:
    print(f'{numusu} no es un número entero positivo.')
       
print()


#Actividad 3
numero = int(input("Introduzca un número entero positivo: "))
n1 = 2
while n1 <= 2*numero:
    print(f'{n1}, {n1**3}')
    n1 = n1 + 2
print()


#Actividad 4
frase = input("Inserte una frase: ")
palabras = 1
print()


#Actividad 5
n3 = int(input("Introduzca un número entero positivo: "))
numLin2 = 1
while numLin2 <= n3:
    print(f'*'*numLin2)
    numLin2 = numLin2 +1
print()


#Actividad 6 a
palabra = input("Inserte una palabra: ")
numLin3 = 1
while numLin3 <= 10:
    print(f'{palabra}')
    numLin3 = numLin3 + 1
print()


#Actividad 6 b
palabra1 = input("Inserte una palabra: ")
numLin4 = 1
n4 = int(input("¿Cuántas veces quieres que se repita?: "))
while numLin4 <= n4:
    print(f'{palabra1}')
    numLin4 = numLin4 + 1
print()


#Actividad 7
primers0 = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
numusu1 = int(input("Introduzca un número entero positivo: "))
n5 = 1
if numusu1 < 0:
    while n5 <= numusu1:
        if primers0[n5-1] <= numusu1:
            print(f'{primers0[n5-1]}')
        else:
            break
        n5 = n5 + 1
else:
    print(f'{numusu1} no es un número entero positivo.')
       
print()


#Actividad 8
capi = int(input("Introduce su capital: "))
C = int(input("Introduzca el interés de la capital C (0 - 100): "))
M = int(input("¿Cuántos años tiene esta capital?: "))
ano = 0
while ano <= M:
    print(f'Tu capital el año {ano} fue{capi}.')
    capi = capi+ (capi * (C/100))
    ano = ano + 1
print()


#Actividad 9




#Actividad 10
palabra2 = input("Inserte una palabra")
n6 = len(palabra2)
print()


#Actividad 11
numer = int(input("Introduce un número entero positivo: "))
numLin5 = 1
while numLin5 <= 2*numer-1:
    if numLin5 <= numer:
        print(f'* '*numLin5)
    else:
        print(f'* '*(2*numer-numLin5))
    numLin5 = numLin5 + 1
print()


#Actividad 12
primers = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
cant = int(input("Introduzca un número entero positivo: "))
numLin6 = 1
while numLin6 <= cant:
    if primers[numLin6-1] <= cant:
        print(f'{primers[numLin6-1]}')
    else:
        break
    numLin6 = numLin6 + 1
print()


#Actividad 13
number = input("Introduzca un número: ")
cifras = 0
while cifras < len(number):
    cifras = cifras + 1
print(f'{number} tiene {cifras} cifras.')
print()


#Actividad 14




#Actividad 15





