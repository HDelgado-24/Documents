'''
-INSTRUCCIONS:
1 - Respon totes les preguntes en un arxiu amb el format “Nom_llinatge1_llinatge2_Final1erTrimestrel.py”
2 - Copia l’enunciat de cada exercici en aquest document i posa’l com a comentari.
''' 
'''
Exercicis de teoria:
1 - Explica els diferents tipus de contenidors de dades i les seves característiques i, per tant, les seves diferències. 1 punt
'''
# Variable: Contenedor de datos que permite guardar un valor bajo un nombre comprensible para el usuario. Se le otorga valor mediante "variable = valor".
# Lista/Iterable: Contenedor de datos que permite almacenar más de un elemento o valor. Se crea mediante "lista = ['elemento1', 'elemento2']".
'''
2 - Digues quin tipus de dades natius de Python hem vist a classe i explica’ls. 0.75 punts.
'''
# STR: Cadena de carácteres. Permite todas las letras del abecedario, números y símbolos.
# INT: Números enteros. Permite todos los carácteres alfanuméricos, ya sea positivo, negativo o 0, que no contengan valor decimal.
# FLOAT: Números reales. Permite todos los carácteres alfanuméricos, incluyendo su valor decimal.
# BOOL: Valor booleano. Tiene dos valores: TRUE/VERDADERO/1 y FALSE/FALSO/0.
# BIN: Número binario. Permite los carácteres 0 y 1. Se utiliza para almacenar números binarios.
# OCT: Número octal. Permite carácteres del 0 al 7. Se utiliza para almacenar números octales.
# HEX: Número hexadecimal. Permite carácteres del 0 al 9 y del "a" al "f". Se utiliza para almacenar números hexadecimales.
'''
Exercicis de condicionals:
3 - Crea un petit programa que demani que l’usuari introdueixi per teclat una  opció de l’1 al 5 (pot ser processat com a enter o com a caràcter) 
i que imprimeixi per pantalla “Has introduït l'opció -nombre introduït-” o, en el cas de no introduir una opció correcte imprimeixi “No has introduït una opció vàlida”. 1’75 punts
'''
numusuario = int(input("Introduzca un número del 1 al 5: "))
match numusuario:
    case 1:
        print(f'Has introducido la opción {numusuario}.')
    case 2:
        print(f'Has introducido la opción {numusuario}.')
    case 3:
        print(f'Has introducido la opción {numusuario}.')
    case 4:
        print(f'Has introducido la opción {numusuario}.')
    case 5:
        print(f'Has introducido la opción {numusuario}.')
    case _:
        print("No has introducido una opción válida.")
print()
'''
4 - (Exercici amb condicionals). Escriu un programa que llegeixi una lletra per teclat i digui si es tracta d’una vocal. Haureu de tenir en compte 
les majúscules també, no serà necessari tenir en compte les vocals amb accent o altres. Una altra cosa que haurà de fer el programa serà la d’imprimir 
un missatge d’error “Has introduït més d’una lletra” si l’usuari introdueix 2 o més lletres com a missatge d’entrada. 1’75 punt
'''
letra = input("Introduzca una letra: ")
if len(letra) > 1:
    print("Has introducido más de una letra.")
else:
    match letra:
        case "a":
            print(f'{letra} es una vocal.')
        case "e":
            print(f'{letra} es una vocal.')
        case "i":
            print(f'{letra} es una vocal.')
        case "o":
            print(f'{letra} es una vocal.')
        case "u":
            print(f'{letra} es una vocal.')
        case "A":
            print(f'{letra} es una vocal.')
        case "E":
            print(f'{letra} es una vocal.')
        case "I":
            print(f'{letra} es una vocal.')
        case "O":
            print(f'{letra} es una vocal.')
        case "U":
            print(f'{letra} es una vocal.')
        case _:
            print(f'{letra} no es una vocal.')
print()
        
'''
5 - (Exercici amb condicionals). Crea una calculadora per donar-te un impost d’IRPF total a pagar en funció d’un salari introduït per l’usuari. 
Una vegada que l’usuari introdueixi el seu salari (haurà de ser transformat en ‘float’) la calculadora fará el següent:
Si el salari és inferior o igual a 15000€ anuals, l’usuari no haurà de pagarà res.
Si el salari és troba entre els 15000€ i els 30000€ (aquest darrer inclòs) l’usuari haurà de pagar el 17% d’aquest en IRPF (multiplica el salari per 0.17 i ja tens la quantitat).
Si el salari es troba entre els 30000€ i els 45000€ (aquest darrer inclòs) l’usuari haurà de pagar el 23% d’aquest en IRPF (multiplica el salari per 0.23 i ja tens la quantitat).
Si el salari és superior a 45000€ l’usuari haurà de pagar el 37% d’aquest salari en IRPF (multiplica el salari per 0.37 i ja tens la quantitat). 2 punts
'''
salario = float(input("Introduzca su salario: "))
if salario < 0:
    print("Usted debe dinero.")
elif salario <= 15000:
    print(f'Usted no debe pagar nada.')
elif salario <= 30000:
    print(f'Usted debe pagar {salario * 0.17}€.')
elif salario <= 45000:
    print(f'Usted debe pagar {salario * 0.23}€.')
elif salario > 45000:
    print(f'Usted debe pagar {salario * 0.37}€.')
else:
    print("Introduzca una cantidad válida")
print()
'''
Exercicis de bucles:
6 - Crea un menú ‘infinit’ del qual només es pugui sortir quan l’usuari introdueix per teclat el número 3. Aquest menú haurà de tenir 3 opcions: 1.5 punts.
1a opció: ‘Introdueix el número 1 per saludar-te’, i si l’usuari introueix aquest número el programa haurà de contestar: ‘Hola que tal Pascual’.
2a opció: ‘Introdueix el número 2 per fer una suma’, llavors, demanará dos números per teclat i imprimirà per pantalla: “La suma del ‘num1’+ ‘num2’ és: ‘resultat de la suma’”.
3a opció: ‘Introdueix el número 3 per sortir d’aquest menú’, si el usuari introdueix el número 3, haurà d’imprimir ‘Adeu Mateu.’ i haurà de finalitzar.
'''
menu = '''Seleccione la opción que desee:
1 - Pulsa 1 para recibir un saludo.
2 - Pulsa 2 para realizar una suma.
3 - Pulsa 3 para cerrar este menú.
'''

while True:
    opcion = input(menu)
    match opcion:
        case "1":
            print("Hola que tal Pascual.")
        case "2":
            num1 = float(input("Introduzca el primer número: "))
            num2 = float(input("Introduzca el segundo número: "))
            print(f'La suma de {num1} y {num2} es: {num1 + num2}.')
        case "3":
            print("Adeu Mateu.")
            break
        case _:
            print("Introdujiste una opción inválida.")
    print()
print()
'''
7 - Realitza un programa que demani a l’usuari un nombre i un caràcter d’entrada i a partir d’aquests realitzi el següent patró (exemple per a nombre = 4 y per a caràcter = #) :
“””
1#
2##2##
3###3###3###
4####4####4####4####

1.25 punts.
'''
numero = int(input("Introduzca un número positivo entero: "))
carac = input("Introduzca un carácter: ")
numLin = 1
while numLin <= numero:
    print((f'{numLin}' + f'{carac * numLin}')*numLin)
    numLin = numLin + 1
print()