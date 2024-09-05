usuario="JULI"
contra="2009"
u=input("ingresa el nombre de usuario")
c=input("ingresa la contraseña")
contador=1
while u!=usuario and c!=contra and contador <4:

    u=input("ingresa tu nombre de usuario:")
    c=input("ingresa tu contraseña:")
    print("Vuelta numero: ", contador)
    contador=contador+1

    if u==usuario and c==contra:
        print("Bienvenido/a al sistema")
    else:
        print("No podes ingresar al sistema")