lstColores = ["Rojo", "Negro", "Verde", "Azul", "Naranja"]
print("El elemento \"Rojo\" aparece en la posición {0} de la lista".format(
    lstColores.index("Naranja")))
print(f"La lista tiene {len(lstColores)} elementos")

lstColores = ["Rojo", "Negro", "Verde", "Azul", "Naranja"]
print(lstColores[:2])

lstColores = ["Rojo", "Negro", "Verde", "Azul", "Naranja"]
print(lstColores[2:4])

lstColores = ["Rojo", "Negro", "Verde", "Azul", "Naranja"]
print(lstColores[:-1])

lstColores = ["Rojo", "Negro", "Verde", "Azul", "Naranja"]
print("El elemento 2 tiene el valor {0}".format(lstColores[2]))
lstColores[2] = "Amarillo"
print("Ahora, el elemento 2 tiene el valor {0}".format(lstColores[2]))

lstColores = ["Rojo", "Negro", "Verde", "Azul", "Naranja"]
print(f"La lista tiene {len(lstColores)} elementos")
lstColores.append("Blanco")
print(f"Ahora, la lista tiene {len(lstColores)} elementos")

lstColores = ["Rojo", "Negro", "Verde", "Azul", "Naranja"]
print(lstColores)
# Insertaremos un elemento en la posición 3
lstColores.insert(3, "Violeta")
print(lstColores)

lstColores = ["Rojo", "Negro", "Verde", "Azul", "Naranja"]
print(lstColores)
# Extendemos la lista con varios elementos más
lstColores.extend(["Violeta", "Rosa", "Púrpura", "Blanco"])
print(lstColores)

lstColores = ["Rojo", "Negro", "Verde", "Azul", "Naranja"]
print(lstColores)
# Eliminamos el elemento "Verde"
lstColores.remove("Verde")
print(lstColores)

lstColores = ["Rojo", "Negro", "Verde", "Azul", "Naranja"]
print(lstColores)
# Eliminamos el elemento de la posición 1
lstColores.pop(1)
print(lstColores)

lstColores = ["Rojo", "Negro", "Verde", "Azul", "Naranja"]
if "Naranja" in lstColores:
    print("El color 'Naranja' existe en la lista")
else:
    print("El color 'Naranja' no existe en la lista")
    
lstColores = ["Rojo", "Negro", "Verde", "Azul", "Naranja"]
if "Naranja" in lstColores:
    print("El color 'Naranja' existe en la lista, en la posición {0}".format(
        lstColores.index("Naranja")))
else:
    print("El color 'Naranja' no existe en la lista")
    
lstColores = ["Rojo", "Negro", "Verde", "Azul", "Naranja"]
print(f"La lista antes de invertir el orden: {lstColores}")
lstColores.reverse()
print(f"La lista antes tras invertir el orden: {lstColores}")

lstColores = ["Rojo", "Negro", "Verde", "Azul", "Naranja"]
print(f"La lista antes de ordenar: {lstColores}")
lstColores.sort()
print(f"La lista antes tras ordenar: {lstColores}")

lstColores = ["Rojo", "Negro", "Verde", "Azul", "Naranja"]
print(f"La lista antes de ordenar: {lstColores}")
lstColores.sort(reverse=True)
print(f"La lista antes tras ordenar: {lstColores}")

lstNumeros = [2, -1, 45, 0, -23, 132]
print(lstNumeros)
lstNumeros.sort()
print(lstNumeros)

lstNumeros = [2, -1, 45, 0, -23, 132]
print(lstNumeros)
lstNumeros.reverse()
print(lstNumeros)