#Actividad 7
numero = int(input("Inserte un número entero para saber si es primo: "))
x = 2
listaprimos = []
esprimo = True
while (x <= int(numero**0.5)+1):
    if (numero%x == 0):
        esprimo = False
        break
    else:
        esprimo == True
        listaprimos.append()
    x = x+1
print()

#Actividad 8
cap = float(input("Introduzca su capital: "))
int = float(input("Introduzca el interés en porcentaje: "))
a = float(input("Introduzca el número de años que invertirá: "))
i = 1
while i <= a:
    cap = cap + ((cap*int)/100)
    print(f'El año {i} su capital total será de {cap}€.')
    i = i + 1
print()


#Actividad 9
num = float(input("Introduzca un nombre entero: "))
div = 1
suma = 0
while div <= num/2:
    if num%div == 0:
        suma = suma + div
    div = div + 1
print(f'El resultado de la operación es {suma}.')