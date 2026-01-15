numero = int(input("Inserte un número entero para saber si es primo: "))
x = 1
while (x <= numero/2):
    if (numero%x == 0) and (x < numero) and (x != 1):
        print(f'{numero} no es un número primo.')
        break
    elif x == numero:
        print(f'{numero} es un número primo.')
        break
    else:
        x = x+1
