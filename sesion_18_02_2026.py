#2

frase = input('Introduzca una frase: ')
linea = 1
listafrase = frase.split(' ')
textlinea = ""
sime = ''
i = 0
isime = len(listafrase) -1
while linea <= len(listafrase) * 2 - 1:
    if linea < len(listafrase):
        textlinea += listafrase[i]+' '
        sime = '/n'+listafrase[isime] + sime
        print(f'{textlinea}')
        i += 1
    elif linea == len(listafrase):
        textlinea += listafrase[i]
        print(f'{textlinea}')
        textlinea = str(listafrase[::-1]).join(' ')
    elif linea <= len(listafrase) * 2 - 1:
        i -= 1
        textlinea -= listafrase[::-1][i]
        print(f'{textlinea}')
    linea += 1
print()




#3
n = int(input('Introduzca un número entero: '))
numlin = 1
linea = ''
simetria = ''
cont = 1
contn = n
while numlin < n*2:
    if numlin%2==1:
        linea = ((str(cont)*cont)+' - ')*cont
        print(linea)
        cont +=1
        simetria = linea+'\n'+simetria
    elif numlin%2==0:
        linea = '*'*contn
        print(linea)
        contn-=1
        simetria = linea+'\n'+simetria
    numlin +=1
print(simetria)
    
