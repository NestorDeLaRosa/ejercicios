nombre = input("Por favor, ingresa tu nombre completo: ")


while not nombre.replace(' ', '').isalpha():
    nombre = input("Por favor, ingresa un nombre v�lido (solo letras y espacios): ")


edad = input("Por favor, ingresa tu edad: ")
telefono = input("Por favor, ingresa tu n�mero de tel�fono: ")
correo = input("Por favor, ingresa tu correo electr�nico: ")

print("\nResumen de la informaci�n ingresada:")
print("Nombre: ", nombre)
print("Edad: ", edad)
print("Tel�fono: ", telefono)
print("Correo electr�nico: ", correo)

