# Entorno

API simple con FastAPI para usuarios + script Python de fuerza bruta para el endpoint /login/. Uso educativo y en entornos controlados.

Requisitos

Python 3.10+

Dependencias: fastapi[standard], sqlmodel, requests

Instalar:

pip install fastapi uvicorn[standard] sqlmodel requests

Ejecutar la API
uvicorn api_main:app --reload --host 127.0.0.1 --port 8000

Ejecutar el script de brute force

Asegúrate que la API esté corriendo. Luego:

python brute_force.py


Configura en el script: username, url, alfabeto, longitud_maxima.

Endpoints clave

POST /login/ — JSON: {"username":"Katty","password":"aa"} → {"message":"Login exitoso"} si es correcto.

GET /users/, POST /users/, GET/PUT/DELETE /users/{id}


