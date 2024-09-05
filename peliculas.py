peliculas={"P01":{"nombre":"culpa mia","estreno":2023,"protagonista":"Nooa","genero":"Drama","director":"Domingo Gonzales" },"P02":{"nombre":"buscando a nemo","estreno":2003,"protagonista":"nemo","genero":"infantil","director":"Andrew Stanton"}}


print(peliculas)
print("__________________________________________")


for c,v in peliculas.items():
    print(c, ":", v )
    print("_________________________________________")
