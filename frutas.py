frutas= {"frutilla": {"precio": 1800}, "durazno":{"precio": 700}}

#indicar el total
total=0

#solicitar al usuario que ingrese la fruta y la cantidad
fruta=input("ingrese la fruta que desea vender: ")
cant=float(input("Ingrse la cantidad de fruta que desea vender:"))

#verificar si la fruta esta en el diccionario
if fruta in frutas:
    #calcular el total
    total=frutas[fruta]["precio"] * cant
    print(f"el total a pagar por {cant} kilos de {fruta} es: {total}")
    print("el precio de ",cant,"kg", "de", fruta, " es de:", total)

else:
    print("la fruta ingresada no existe en el diccionario")