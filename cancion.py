canciones = {
    "1": "Canci�n 1: Letra de la canci�n 1",
    "2": "Canci�n 2: Letra de la canci�n 2",
    "3": "Canci�n 3: Letra de la canci�n 3",
    "4": "Canci�n 4: Letra de la canci�n 4",
    "5": "Canci�n 5: Letra de la canci�n 5",
    "6": "Canci�n 6: Letra de la canci�n 6",
    "7": "Canci�n 7: Letra de la canci�n 7",
    "8": "Canci�n 8: Letra de la canci�n 8",
    "9": "Canci�n 9: Letra de la canci�n 9",
    "10": "Canci�n 10: Letra de la canci�n 10",
}

print("Por favor, elige una canci�n del 1 al 10:")
for key, value in canciones.items():
    print(key + ". " + value)
eleccion = input("Ingresa el n�mero de la canci�n que deseas: ")

if eleccion in canciones.keys():
    print("\nLetra de la canci�n seleccionada:\n" + canciones[eleccion])
else:
    print("Selecci�n no v�lida. Por favor, elige un n�mero del 1 al 10.")
