significado_completo = input("Ingrese el significado completo de una organizaci�n o concepto: ")

palabras = significado_completo.split()

acronimo = ""

for palabra in palabras:
    acronimo += palabra[0]

print("El acr�nimo de", significado_completo, "es:", acronimo.upper())
