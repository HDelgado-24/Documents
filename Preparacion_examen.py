# Correcció d'exercicis de patrons:


'''
# 2 - Segundo ejercicio:
Imagina que te han dado la frase = 'Hola como vas amigo mío.'
El patrón a dibujar en función de esta frase será:


Hola
Hola como
Hola como vas
Hola como vas amigo
Hola como vas amigo mío.
mío. amigo vas como
mío. amigo vas
mío. amigo
mío.


"Tened en cuenta que las oraciones introducidas siempre tendrán un solo
espacio entre palabras. Los puntos, comas y otros separadores pertenecen
a la palabra a la que están pegados.
'''


frase = input('Escriu una frase d\'entrada: ')


listafrase = frase.split(' ')
contplabr = 0


while contplabr < len(listafrase):
    print(' '.join(listafrase[0:contplabr]))
    contplabr += 1
print(' '.join(listafrase))


contplabr -= 1
listafraseinv = listafrase[::-1]


while contplabr >= 0:
    print(' '.join(listafraseinv[0:contplabr]))
    contplabr -= 1








# 3 - Tercer ejercicio:
# número introducido n = 4
'''
1 -
* * * *
2 - 22 -
* * *
3 - 33 - 333 -
* *
4 - 44 - 444 - 4444 -
* *
3 - 33 - 333 -
* * *
2 - 22 -
* * * *
1 -
'''


num = int(input('Introdueix un nombre enter positiu: '))
# Hacemos el patrón de asteriscos y lo guardamos en una lista de listas.
contast = num
patronast = []
while contast >= 2:
    patronast.append(contast*'* ')
    contast -= 1
patronast.extend(patronast[::-1])


# Creamos el patrón numérico.
patronNum = []
contNum = 1


while contNum <= num:
    contInt = 1
    linea = ''
    while contInt <= contNum:
        linea += contInt*str(contNum) + ' - '
        contInt += 1
    patronNum.append(linea)
    contNum += 1
patronNum.extend(patronNum[0:num-1][::-1])


contPrint = 0
while contPrint < len(patronast):
    print(patronNum[contPrint])
    print(patronast[contPrint])
    contPrint += 1
print(patronNum[0])
print()




#Act 4
numintr = int(input('Introduzca un número: '))
numimpr = numintr
numlin = 1
while numlin <= numintr * 2:
    if numlin < numintr:
        if numlin%2 == 1:
            ast = numimpr
            textlinea = ''
            while ast > 0:
                ast -= 1
                textlinea += str(numimpr)+' '+'* '*ast
            print(textlinea)
        else:
            porc = numimpr
            textlinea = ''
            while porc > 0:
                porc -= 1
                textlinea += str(numimpr) +' '+'% '*porc
            print(textlinea)
        numimpr -= 1
    elif numlin > numintr:
        if numlin%2 == 1:
            ast = numimpr
            textlinea = ''
            while ast > 0:
                ast -= 1
                textlinea += str(numimpr) +' '+'* '*ast
            print(textlinea)
        else:
            porc = numimpr
            textlinea = ''
            while porc > 0:
                porc -= 1
                textlinea += str(numimpr) +' '+'% '*porc
            print(textlinea)
        numimpr += 1


    numlin += 1
print()


#Act 5
nintr = int(input('Introduzca un número: '))
nummostr = 1
lin = 1
while lin <= 2*nintr-1:
    numesp = nintr - nummostr
    if lin < nintr:
        if lin%2 == 1:
            print(' '*numesp+f'{nummostr}-'*(nummostr-1)+f'{nummostr}')
        else:
            print(' '*numesp+f'{nummostr}*'*(nummostr-1)+f'{nummostr}')
        nummostr += 1
    elif lin >= nintr:
        if lin%2 == 1:
            print(' '*numesp+f'{nummostr}-'*(nummostr-1)+f'{nummostr}')
        else:
            print(' '*numesp+f'{nummostr}*'*(nummostr-1)+f'{nummostr}')
        nummostr -= 1
    lin += 1
print()


#Act 11
'''
cifr = int(input('Introduzca un número: '))
palab = input('Introduzca una palabra: ')
cont = 1
while cont <= cifr:
    if cont%2 == 1:
        aster = cifr
        contelin = palab[0].upper+palab[1:len(palab)]+' '+'*'*aster+' '
        while aster < 0:
            aster -= 1
            contelin +=
'''
