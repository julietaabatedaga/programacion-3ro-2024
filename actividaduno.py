#1-Escribir un programa que permita Inresar números enteros por teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresado

suma=0
while True:
    num= int("ingrese u numero")
    if num==0:
        break
    if num > 0:
        suma+=num
        print("la suma de los numeros es:", suma)
