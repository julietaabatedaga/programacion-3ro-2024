#3-Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo compone
numero=input("introducir un numero entero positivo:")#leer un numero entero positivo desde el teclado
lista_digitos=[int(digito) for digito in numero]#convertir el numero a una lista de digitos
suma_digitos=sum(lista_digitos)#callcula la suma de los digitos
print("los digitos son:", lista_digitos)#mostrar la lista de digitos y la suma
print("la suma de los digitos es:", suma_digitos)
