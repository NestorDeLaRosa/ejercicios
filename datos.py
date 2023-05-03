nombre = input("Por favor, ingresa tu nombre completo: ")


while not nombre.replace(' ', '').isalpha():
    nombre = input("Por favor, ingresa un nombre válido (solo letras y espacios): ")


edad = input("Por favor, ingresa tu edad: ")
telefono = input("Por favor, ingresa tu número de teléfono: ")
correo = input("Por favor, ingresa tu correo electrónico: ")

print("\nResumen de la información ingresada:")
print("Nombre: ", nombre)
print("Edad: ", edad)
print("Teléfono: ", telefono)
print("Correo electrónico: ", correo)

