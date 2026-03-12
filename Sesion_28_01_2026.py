#Actividad 15
num = int(input(f'Introduzca cuántos números desea almacenar: '))
listapar = []
listasenar = []
i = 1
while i <= num:
    numero = int(input(f'Introduce el {i}º número: '))
    if numero%2==0:
        listapar.append(numero)
    else:
        listasenar.append(numero)
    i += 1
print(f'La lista de números pares es: {listapar}, con un total de {len(listapar)} pares. La lista de números senares es: {listasenar}, con un total de {len(listasenar)} senares.')
print()

#Ejercicio 16
num1 = int(input('Introduce el primer número: '))
num2 = int(input('Introduce el segundo número: '))
suma = 0
i2 = num1
while i2 <= num2:
    suma += i2
    i2 +=1
print(f'El resultado de la suma es: {suma}.')
print()


#Ejercicio 17
num10 = int(input('Escriba el primer número: '))
num20 = int(input('Escriba el segundo número, mayor que el primero: '))
suma2 = 0
sumaesc =""
i3 = num10
while i3 <= num20:
    suma2 += i3
    if i3 == num20:
        sumaesc += f'{i3} '
    else:
        sumaesc += f"{i3} + "
    i3 +=1
print(f'{sumaesc}= {suma}')
print()


#Ejercicio 18
num3 = int(input(f'Introduzca el número a comparar: '))
numcan = int(input('¿Cuántos números desea introducir?: '))
listanum = []
cont = 0
i4 = 1
while i4 <= numcan:
    num4 = int(input(f'Introduzca el {i4}º número: '))
    if num3 == num4:
        cont += 1
    listanum.append(num4)
    i4 += 1
print(f'En la lista {listanum}, el número {num3} se ha repetido {cont} veces.')
print()


#Ejercicio 19
frase = input('Introduzca una frase: ')
vocal = 0
i5 = 0
while i5 < len(frase):
    match frase[i5]:
        case "a":
            vocal += 1
        case "e":
            vocal += 1
        case "i":
            vocal += 1
        case "o":
            vocal += 1
        case "u":
            vocal += 1
        case "A":
            vocal += 1
        case "E":
            vocal += 1
        case "I":
            vocal += 1
        case "O":
            vocal += 1
        case "U":
            vocal += 1
    i5 += 1
print(f'La frase: "{frase}" contiene {vocal} vocales.')
