#Actividad 1
seguir = input('Si desea seguir con el programa, escriba exactamente "sí": ')
while seguir == "sí":
    seguir = input('Si desea seguir con el programa, escriba exactamente "sí": ')
print()


#Actividad 2
seguir = input('¿Desea seguir con el programa?: ')
while (seguir == "sí") or (seguir == "si") or (seguir == "Sí") or (seguir == "Si") or (seguir == "sÍ") or (seguir == "sI") or (seguir == "SÍ") or (seguir == "SI"):
    seguir = input('¿Desea seguir con el programa?: ')
print()


#Actividad 3
num1 = int(input('Introduzca un número: '))
num2 = int(input('Introduzca otro número: '))
menu = '''Elige una de las siguientes opciones (teclee un número del 1 al 3):
1 - Sumar los números
2 - Restar los números
3 - Multiplicar los números'''
opcion = input(menu)
while True:
    match opcion:
        case '1':
            print(f'La suma entre {num1} y {num2} resulta en {num1+num2}')
            break
        case '2':
            print(f'La resta entre {num1} y {num2} resulta en {num1-num2}')
            break
        case '3':
            print(f'La multiplicación entre {num1} y {num2} resulta en {num1*num2}')
            break
        case _:
            print('Escoge una opción válida.')
    print()
    opcion = input(menu)
print()


#Actividad 4
numeroimpar = int(input('Introduzca un número entero impar: '))
while numeroimpar%2 == 0:
    numeroimpar= int(input(f'{numeroimpar} no es un número impar, pruebe otra vez: '))
print(f'{numeroimpar} es un número impar.')
print()


#Actividad 5
numini = 2
total = 0
while numini <= 100:
    total += numini
    numini +=2
print(f'La suma de todos los números pares del 0 al 100 resulta en {total}')
print()


#Actividad 6
listaveri = [1, 3, 6, 9]
numusu = int(input('Introduzca un número entero del 0 al 9: '))
cont = 0
while cont <= len(listaveri)-1:
    if numusu == listaveri[cont]:
        print('Acertaste uno de los números.')
        break
    elif cont == len(listaveri)-1:
        cont= 0
        numusu= int(input('Pruebe otra vez: '))
    cont += 1
print()


#Actividad 7
lista1 = [1, 1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9, 1, 11, 12, 13, 14, 15, 16, 15, 1, 2]
lista2 = [1, 2, 2, 3, 3, 4, 5, 6, 7, 7, 8, 8, 9, 9]
listarepe = []
comp1 = 0
comp2 = 0
comprepe = 0
while comp1 <= len(lista1)-1:
    while comp2 <= len(lista2)-1:
        if lista1[comp1] == lista2[comp2]:
            while (comprepe <= len(listarepe)-1) or (listarepe == []):
                if (comprepe == len(listarepe)-1) or (listarepe == []):
                    listarepe.append(lista1[comp1])
                comprepe += 1
        comprepe = 0
        comp2 +=1
    comp2 = 0
    comp1 +=1
print(f'La lista con los elementos repetidos en las listas {lista1} y {lista2} resulta en: {listarepe}.')