#2-Ingresar números enteros positivos por teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
numerospositivos=[]
while True:#con la funcion break
    numero=int(input("ingrese un numero positivo:"))
    numerospositivos.append(numero)
    if numero==0:
        break
    print("el valor mayor es:")
    print(max(numerospositivos))