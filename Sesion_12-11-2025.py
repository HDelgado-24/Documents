listaejemplo = [15, 12, 34, 56, 12, 12, 3, 4, 6, 5, 7, 8]

#1 - Imprime por pantalla cuantas veces aparece el número 12.

print(f"El número 12 aparece {listaejemplo.count(12)} veces")

#2 - Inserta un número leído por teclado en la posición 4 de la lista (índice 3).

numero_usuario = int(input("Introduce un número para introducir a la lista:"))
listaejemplo.insert(3,numero_usuario)
print(f"La lista con el nuevo elemento se vé así: {listaejemplo}")

#3 - Imprime la lista con todos los elementos invertidos de posición.

listaejemplo.reverse()
print(f"La lista invertida es: {listaejemplo}")

#4 - Tienes otra lista: [1, 2, 3]. añadela como único elemento al final de listaejemplo.

lista2 = [1, 2, 3]
listaejemplo.append(lista2)
print(f"La lista después de añadir la otra lista al final como elemento único queda: {listaejemplo}")

#5 - Extiende la lista listaejemplo con los elementosde la lista del punto anterior.

listaejemplo.extend(lista2)
print(f"Después de extender la lista queda así: {listaejemplo}")

#6 - Extrae el elemento 12 de la lista (una vez) e imprime como queda la lista después de extraerlo.

listaejemplo.remove(12)
print(f"Después de haber eliminado el primer 12, queda así: {listaejemplo}")


#crea una lista que tenga 3 dimensiones en las que cada sublista contenga almenos 3 elementos.
#Quiero que imprimáis el 3er elemento de la lista que está dentro del tercer elemento de la lista que se encuentra en la 3a posición de loa lista principal.
print()
print()
listatridim = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24], [25, 26, 27]]]
print(f"El tercer elemento del tercer elemento de la lista es: {listatridim[2][2][2]}")