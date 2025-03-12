animalesES_IN = {"Pájaro": "Bird", "León": "Lion", "Murciélago": "Bat", "Araña": "Spider", "Perro": "Dog", "Gato": "Cat"}
print("Pájaro en inglés es {0}".format(animalesES_IN["Pájaro"]))
print("Murciélago en inglés es {0}".format(animalesES_IN["Murciélago"]))

animalesES_IN = {"Pájaro": "Bird", "León": "Lion", "Murciélago": "Bat", "Araña": "Spider", "Perro": "Dog", "Gato": "Cat"}
clave = "murciélago"
if animalesES_IN.get(clave) == None:
    print(f"'{clave}' no existe en el diccionario")
else:
    print("{0} en inglés es {1}".format(clave, animalesES_IN[clave]))
    
animalesES_IN = {"Pájaro": "Bird", "León": "Lion", "Murciélago": "Bat", "Araña": "Spider", "Perro": "Dog", "Gato": "Cat"}
clave = "murciélago"
mensaje = ""
if animalesES_IN.get(clave) == None:
    # Intentamos convirtiendo la primera letra en mayúscula
    clave = clave.capitalize()
    if animalesES_IN.get(clave) == None:        
        mensaje = f"'{clave}' no existe en el diccionario"
    else:
        mensaje = "{0} en inglés es {1}".format(clave, animalesES_IN[clave])
else:
    mensaje = "{0} en inglés es {1}".format(clave, animalesES_IN[clave])
print(mensaje)    

animalesES_IN = {"Pájaro": "Bird", "León": "Lion", "Murciélago": "Bat", "Araña": "Spider", "Perro": "Dog", "Gato": "Cat"}
for animal in animalesES_IN:
  print(f"{animal} en inglés es {animalesES_IN[animal]}")
  
animalesES_IN = {"Pájaro": "Bird", "León": "Lion", "Murciélago": "Bat", "Araña": "Spider", "Perro": "Dog", "Gato": "Cat"}
for animalES, animalIng in animalesES_IN.items():
  print(f"{animalES} en inglés es {animalIng}")
  
animalesES_IN = {"Pájaro": "Bird", "León": "Lion", "Murciélago": "Bat", "Araña": "Spider", "Perro": "Dog", "Gato": "Cat"}
print(animalesES_IN.keys())

animalesES_IN = {"Pájaro": "Bird", "León": "Lion", "Murciélago": "Bat", "Araña": "Spider", "Perro": "Dog", "Gato": "Cat"}
print(animalesES_IN.values())

animalesES_IN = {"Pájaro": "Bird", "León": "Lion", "Murciélago": "Bat", "Araña": "Spider", "Perro": "Dog", "Gato": "Cat"}
print(animalesES_IN.items())

animalesES_IN = {"Pájaro": "Bird", "León": "Lion", "Murciélago": "Bat", "Araña": "Spider", "Perro": "Dog", "Gato": "Cat"}
print(f"Claves del diccionario animales antes de inserción: {animalesES_IN.keys()}")
# Insertamos un nuevo elemento en el diccionario
animalesES_IN["Gusano"] = "Worm"
print(f"Claves del diccionario animales después de inserción: {animalesES_IN.keys()}")

animalesES_IN = {"Pájaro": "Bird", "León": "Lion", "Murciélago": "Bat", "Araña": "Spider", "Perro": "Dog", "Gato": "Cat", "Gusano": "Worm"}
print(f"Valores del diccionario animales antes de modificación: {animalesES_IN.values()}")
# Modificamos un nuevo elemento existente en el diccionario
animalesES_IN["Gusano"] = "Caterpillar"
print(f"Valores del diccionario animales después de modificación: {animalesES_IN.values()}")

animalesES_IN = {"Pájaro": "Bird", "León": "Lion", "Murciélago": "Bat", "Araña": "Spider", "Perro": "Dog", "Gato": "Cat", "Gusano": "Worm"}
print(f"Claves del diccionario animales antes de eliminación: {animalesES_IN.keys()}")
# Eliminamos dos elementos del diccionario
animalesES_IN.pop("Gusano")
animalesES_IN.pop("Perro")
print(f"Claves del diccionario animales después de eliminación: {animalesES_IN.keys()}")

animalesES_IN = {"Pájaro": "Bird", "León": "Lion", "Murciélago": "Bat", "Araña": "Spider", "Perro": "Dog", "Gato": "Cat", "Gusano": "Worm"}
print(f"Claves del diccionario animales antes de vaciar contenido: {animalesES_IN.keys()}")
# Vaciamos el diccionario
animalesES_IN.clear()
print(f"Claves del diccionario animales después de vaciar contenido: {animalesES_IN.keys()}")

codigosPostales = {"Murcia": 30, "Albacete": 2, "Burgos": 9, "Granada": 18, "Madrid": 28}
print(codigosPostales.items())

codigosPostales = {30: "Murcia", 2: "Albacete", 9: "Burgos", 18: "Granada", 28: "Madrid"}
print(codigosPostales.items())