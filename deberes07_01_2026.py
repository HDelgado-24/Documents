#Actividad 1
pizzas = ["barbacoa", "margarita", "prosciutto", "romana"]
numLin1 = 0
for pizza in pizzas:
    print(f'Me gusta la pizza {pizza}.')
    numLin1 = numLin1+ 1
print("Me encantan las pizzas.")
print()


#Actividad 2
numusu = int(input("Inserte un número entero positivo: "))
resu = ""
n = 1
if numusu > 0:
    while n <= numusu:
        resu +=str(n)+", "
        n = n+2
    print(resu)
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
fraselist = list(frase)
i = 1
palabras = 1
for letra in fraselist:
    if letra == " ":
        palabras = palabras + 1
        i = i + 1
    else:
        i = i + 1
print(f'"{frase}" contiene {palabras} palabras.')
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




#Actividad sesión
palabrilla = input("Introduzca una palabra: ")
palabrillalist = list(palabrilla)
nuevapalabrilla=[]
u = 1
for letrilla in palabrillalist:
    if (u%2==0):
        nuevapalabrilla.append(letrilla.lower())
    else:
        nuevapalabrilla.append(letrilla.upper())
    u = u + 1
palabrita=""
for letra in nuevapalabrilla:
    palabrita = palabrita+letra
print(f"{palabrita}")
print()
print()






cadena = input("Introduzca una cadena: ")
cadenalter = ""
ismayus = True
ind = 0
while ind <= len(cadena)-1:
    if ismayus:
        cadenalter += cadena[ind].upper()
    else:
        cadenalter += cadena[ind].lower()
    ismayus = not ismayus
    ind += 1
print(cadenalter)
