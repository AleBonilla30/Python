nombres = ["Alejandta", "Jorge", "Damaris", "Alma", "Jose de la cruz"]
print(nombres)
for i, nombre in enumerate(nombres):
    print( f"Se inscribio {nombre} en la lista con el indice {i}")
#en las listas para agregar un nombre al final se usa nombres.append("clara")
nombres.append("Clara")
print(nombres)
print(len(nombres))
nombres.remove("Clara")
print(nombres)
#del se usa para quitar el elemento del indice 
del nombres[0]
print(nombres)
#al utilizar in revisa si un valor que le decimos se encuentra en la lista
print("Alejandra" in nombres)

