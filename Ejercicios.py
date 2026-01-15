#Actividad 1
numero = int(input("Introduce un número:"))
if numero > 0:
    print(f"¡Tú número es positivo!")
else:
    if numero == 0 :
        print(f"¡Tú número es 0!")
    else:
        print(f"¡Tú número es negativo!")


#Actividad 2
citrica = ["limon", "lima", "naranja"]
dulce = ["fresa", "sandia", "caqui"]
seco = ["nuez", "cacahuete", "pipa"]
fruta = input("Introduzca una fruta:")
if fruta in citrica:
    print(f"{fruta} es una fruta cítrica.")
else:
    if fruta in dulce:
        print(f"{fruta} es una fruta dulce.")
    else:
        if fruta in seco:
            print(f"{fruta} es un fruto seco.")
        else:
            print(f"{fruta} es otro tipo de fruta.")


#Actividad 3
edad = int(input("Introduzca tu edad:"))
if edad >= 0 and edad < 18:
    print(f"Eres menor.")
else:
    if edad >= 18 and edad <= 30 :
        print(f"Eres un adulto joven.")
    else:
        if edad >= 31 and edad <= 65:
            print(f"Eres un adulto.")
        else:
            if edad > 65:
                print(f"Eres adulto senior.")
            else:
                print(f"¿Has nacido acaso?")


#Actividad 4
dia = int(input("Introduzca el día de la semana (del 1 al 7):"))
if dia == 1:
    print(f"Hoy es lunes.")
elif dia == 2:
    print(f"Hoy es martes.")
elif dia == 3:
    print(f"Hoy es miércoles.")
elif dia == 4:
    print(f"Hoy es jueves.")
elif dia == 5:
    print(f"Hoy es viernes.")
elif dia == 6:
    print(f"Hoy es sábado.")
elif dia == 7:
    print(f"Hoy es domingo.")
else:
    print(f"Ese día no existe.")


#Actividad 5
mamifero = ["leon", "tigre", "perro"]
ave = ["pingüino", "cigüeña", "flamenco"]
reptil = ["lagarto", "cocodrilo", "serpiente"]
animal = input("Introduzca un animal:")
if animal in mamifero:
    print(f"{animal} es un animal mamífero.")
else:
    if animal in ave:
        print(f"{animal} es una ave.")
    else:
        if animal in reptil:
            print(f"{animal} es un reptil.")
        else:
            print(f"{animal} es otro tipo de animal.")

#Actividad 6
distancia = int(input("Introduzca la distancia que ha de recorrer el paquete (km):"))
if distancia > 0 and distancia < 10:
    print(f"Tu coste de envío será de 5€.")
elif distancia >= 10 and distancia < 50:
    print(f"Tu coste de envío será de 10€.")
elif distancia >= 50:
    print(f"Tu coste de envío será de 15€.")
else:
    print(f"No ha indicado una distancia permitida.")


#Actividad 7
nota = int(input("Introduzca la nota adquirida en su examen:"))
if nota >= 0 and nota < 3:
    print(f"Has sacado un F.")
elif nota >= 3 and nota < 5:
    print(f"Has sacado un D.")
elif nota >= 5 and nota < 7:
    print(f"Has sacado un C.")
elif nota >= 7 and nota < 9:
    print(f"Has sacado un B.")
elif nota >= 9 and nota <= 10:
    print(f"Has sacado un A.")
else:
    print(f"Introduzca una nota válida.")


#Actividad 8
diasem = input("¿Qué día de la semana es hoy?:")
if diasem == "lunes" or diasem == "Lunes":
    print(f"Hoy es día laborable.")
elif diasem == "martes" or diasem == "Martes":
    print(f"Hoy es día laborable.")
elif diasem == "miércoles" or diasem == "Miércoles" or diasem == "miercoles" or diasem == "Miercoles":
    print(f"Hoy es día laborable.")
elif diasem == "jueves" or diasem == "Jueves":
    print(f"Hoy es día laborable.")
elif diasem == "viernes" or diasem == "Viernes":
    print(f"Hoy es día laborable.")
elif diasem == "sábado" or diasem == "Sábado" or diasem == "sabado" or diasem == "Sabado":
    print(f"Hoy es día fin de semana.")
elif diasem == "domingo" or diasem == "Domingo":
    print(f"Hoy es fin de semana.")
else:
    print(f"Introduzca un día válido.")


#Actividad 9
contrasena = input("Introduzca una contraseña:")
comprocon = input("Repita su contraseña:")
if contrasena.upper == comprocon.upper:
    print(f"Su contraseña es correcta.")
else:
    print(f"Ha introducido incorrectamente su contraseña.")


#Actividad 10
num1 = int(input("Introduzca el dividendo:"))
num2 = int(input("Introduzca el divisor:"))
if num2 != 0:
    print(f"El resultado de su división es {num1/num2}.")
else:
    print(f"Ha ocurrido un error (No puede insertar 0 como divisor).")


#Actividad 11
edad1 = int(input("Inserte su edad:"))
ingresos = float(input("Introduzca sus ingresos mensuales (€):"))
if edad1 > 16 and ingresos >= 1000:
    print(f"Usted debe tributar.")
else:
    print(f"Usted no debe tributar.")


#Actividad 12
abc = ["A", "B", "N", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
genero = input("Introduca su género:")
nombre = input("Introduzca su nombre:")
if (genero == "MUJER" or genero == "CHICA") and (nombre[0] == abc[0] or nombre[0] == abc[1] or nombre[0] == abc[2] or nombre[0].upper == abc[3] or nombre[0] == abc[4] or nombre[0] == abc[5] or nombre[0] == abc[6] or nombre[0] == abc[7] or nombre[0] == abc[8] or nombre[0] == abc[9] or nombre[0] == abc[10] or nombre[0] == abc[11]):
    print(f"Perteneces al grupo A.")
elif (genero == "HOMBRE" or genero == "CHICO") and (nombre[0] == abc[14] or nombre[0] == abc[15] or nombre[0] == abc[16] or nombre[0] == abc[17] or nombre[0] == abc[18] or nombre[0] == abc[19] or nombre[0] == abc[20] or nombre[0] == abc[21] or nombre[0] == abc[22] or nombre[0] == abc[23] or nombre[0] == abc[24] or nombre[0] == abc[25] or nombre[0] == abc[26]):
    print(f"Perteneces al grupo A.")
else:
    print(f"Perteneces al grupo B")


#Actividad 13
renta = int(input("Introduzca tu renta anual (€):"))
if renta > 0 and renta < 10000:
    print(f"Te corresponde el 5% de impositivo.")
elif renta >= 10000 and renta < 20000:
    print(f"Te corresponde el 15% de impositivo.")
elif renta >= 20000 and renta < 35000:
    print(f"Te corresponde el 20% de impositivo.")
elif renta >= 35000 and renta < 60000:
    print(f"Te corresponde el 30% de impositivo.")
elif renta >= 60000:
    print(f"Te corresponde el 45% de impositivo.")
else:
    print(f"No te corresponde el impositivo.")


#Actividades Match Case


#Actividad 1
fruta1 = input("Introduzca una fruta:")
match fruta1:
    case 'manzana':
        print(f"Es una manzana.")
    case 'platano':
        print(f"Es un plátano.")
    case 'plátano':
        print(f"Es un plátano.")
    case _:
        print(f"Es otra fruta.")


#Actividad 2
diasema = int(input("Introduzca un día de la semána con un número del 1-7:"))
match diasema:
    case 1:
        print(f"Hoy es lunes.")
    case 2:
        print(f"Hoy es martes.")
    case 3:
        print(f"Hoy es miércoles.")
    case 4:
        print(f"Hoy es jueves.")
    case 5:
        print(f"Hoy es viernes.")
    case 6:
        print(f"Hoy es sábado.")
    case 7:
        print(f"Hoy es domingo.")
    case _:
        print(f"Introduzca un número válido.")


#Actividad 3
codi = int(input("Introduzca un código:"))
match codi:
    case 200:
        print(f"Todo ok.")
    case 301:
        print(f"Movimiento permanente de la página.")
    case 302:
        print(f"Movimiento temporal de la página.")
    case 404:
        print(f"Página no encontrada.")
    case 500:
        print(f"Error interno del servidor.")
    case 503:
        print(f"Servidor no disponible.")
    case _:
        print(f"Mensaje desconocido.")