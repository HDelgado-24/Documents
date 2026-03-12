#Actividad 10
palabra = input("Inserte una palabra: ")
i = 1
palabrainv = ""
while i <= len(palabra):
    palabrainv = palabrainv + palabra[len(palabra)-i]
    i += 1
print(f'{palabrainv}')
print()


#Actividad 11
numer = int(input("Introduce un número entero positivo: "))
numLin = 1
while numLin <= 2*numer-1:
    if numLin <= numer:
        print(f'* '*numLin)
    else:
        print(f'* '*(2*numer-numLin))
    numLin = numLin + 1
print()


#Actividad 12
number = input("Introduzca un número: ")
cifras = 0
while cifras < len(number):
    cifras = cifras + 1
print(f'{number} tiene {cifras} cifras.')
print()


#Actividad 13
numero = int(input("¿Cuántos números quieres introducir?: "))
listnumero = []
i2 = 0
while i2 <= numero-1:
    listnumero.append(int(input(f'Introduzca el {i2+1}º número: ')))
    if listnumero[i2] <= listnumero[0]:
        print('Este número es menor que el primer número introducido')
    i2 +=1
print(f'{listnumero}')
print()
