colores = ("Rojo", "Negro", "Verde", "Azul", "Naranja")

numeros = (23, 45, 12, -4)

colores_numeros = (colores, numeros, 123, "Violeta", "Marrón", 458)

colores = ("Rojo", "Negro", "Verde", "Azul", "Naranja")
print(f"El número de elementos de la tupla colores es: {len(colores)}")

colores = ("Rojo", "Negro", "Verde", "Azul", "Naranja")
print(colores[2])

colores = ("Rojo", "Negro", "Verde", "Azul", "Naranja")
numeros = (23, 45, 12, -4)
colores_numeros = (colores, numeros, 123, "Violeta", "Marrón", 458)
print(colores_numeros[1])

numeros = (23, 45, 12, -4, 12, 4, 12, 87)
print(numeros.count(12))

numeros = (23, 45, 12, -4, 12, 4, 12, 87)
print(numeros.index(12))

numeros = (23, 45, 12, -4, 12, 4, 12, 87)

elemento = 88
if numeros.count(elemento) > 0:
    print(f"Posición del elemento {elemento} en la tupla \"numeros\": {numeros.index(elemento)}")
else:
    print(f"No se ha encontrado el elemento {elemento} en la tupla \"numeros\"")
    
tVacia = ()
if tVacia.count("Verde") > 0:
    tVacia = ("Verde", "Azul")
else:
    tVacia = ("Verde", "Rojo")
print(tVacia)

tupla_un_elemento = ("Color", )
print(f"La tupla {tupla_un_elemento} tiene {len(tupla_un_elemento)} elemento")

num1 = 43
num2 = -4
color1 = "Verde"
color2 = "Marrón"
num_color = num1, num2, color1, color2
print(f"La tupla num_color tiene los valores: {num_color}")

num1 = 43
num2 = -4
color1 = "Verde"
color2 = "Marrón"
num_color = num1, num2, color1, color2
v1, v2, v3, v4 = num_color
print(f"La tupla num_color se desempaquetó en las variables v1 -> {v1}, v2 -> {v2}, v3 -> {v3} y v4 -> {v4}")