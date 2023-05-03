import random

def guess_number():
    
    number = random.randint(1, 50)
    max_attempts = 5
    attempts = 0
    
   
    while attempts < max_attempts:
        guess = int(input("Adivina el número entre 1 y 50: "))
        
        
        if guess < 1 or guess > 50:
            print("Número inválido. Debe estar entre 1 y 50.")
            continue
        
        attempts += 1
        
        
        if guess == number:
            print(f"Felicidades, adivinaste el número en {attempts} intentos.")
            return
        else:
            
            remaining_attempts = max_attempts - attempts
            print(f"Número incorrecto. Te quedan {remaining_attempts} intentos.")
    
    
    print(f"Lo siento, no adivinaste el número en {max_attempts} intentos. El número era {number}.")


guess_number()