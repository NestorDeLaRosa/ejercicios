import re
popular_domains = ["gmail.com", "yahoo.com", "hotmail.com"]

email = input("Introduce tu direcci�n de correo electr�nico: ")

match = re.search(r'(?<=@)[^.@][^@]+', email)
if match:
    domain = match.group(0)
else:
    print("Direcci�n de correo electr�nico no v�lida")

if domain in popular_domains:
    print("Este es un correo electr�nico con un dominio popular")
else:
    print("Este es un correo electr�nico con un dominio personalizado")
