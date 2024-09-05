numerosenteros=[]
while True:#con la funcion break
    numero=int(input("ingrese un numero entero:"))
    numerosenteros.append(numero)
    if numero==0:
        break
    print("el valor mayor es:")
    print(max(numerosenteros))