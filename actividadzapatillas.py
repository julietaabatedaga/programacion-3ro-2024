#Actividad 1: 1- Crear un programa que permita manipular y visualizar el stock de zapatillas donde cada una tenga las siguientes propiedades: Número, material, modelo y cantidad en stock. 2- Crea un menú para agregar zapatillas y mostrar zapatillas.

Zapatillas={"D01" : {"modelo": "Nike Air Force", "material" :["algodon organico", "poliester", "caucho"], "Numero": 37, "cantidad en stock": 20}, "D02": {"modelo": "Adidas Campus", "material": ["felpa suave", "algodon organico", "goma", "cuero"], "numero": 40, "cantidad en stock": 6 }, "D03" :{"modelo" : "Vans Lowland", "material": ["lona", "cuero sintetico", "textil", "goma"], "numero": 39, "cantidad en stock": 7}}

while True:
  opcion=input("ingrese una de las siguientes opciones: /n1 mostrar zapatillas en stock /n2 agregar zapatillas al stock")
  if opcion=="1":
    print("Zapatillas")
    for c,v in Zapatillas.items():
      print(c, ":", v)

  elif opcion=="2":
    zapatillasagregar=input("escriba codigo de zapatillas a agregar al stock")
    modelo=input("ingrese el modelo de zapatillas que desea agregar")
    material=input("ingrese el material de las zapatillas que desea agregar")
    numero=input("ingrese el numero de las zapatillas que desea agregar")
    stock=input("ingrese la cantidad de zapatillas que tiene en stock para agregar")
    Zapatillas[zapatillasagregar]=modelo,material,numero,stock
  elif opcion=="3":
     break



