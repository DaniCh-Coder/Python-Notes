'''
En este script, se muestra cómo utilizar la API de chat de OpenAI para generar texto.
Nota: Este es un ejemplo simple con APIs que usan chat.xxx. 
Desde Marzo 2025, OpenAI ha cambiado la API de Completions por la de Responses API.
Para más información, ver el siguiente enlace: https://beta.openai.com/docs/api-reference/completions/create
'''
import openai
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Obtener la clave API desde el archivo .env
openai.api_key = os.getenv("OPENAI_API_KEY")

# Crear un cliente con la nueva versión del SDK
# Detecta la clave automáticamente de OPENAI_API_KEY
# No hay que pasar la clave como parámetro
client = openai.OpenAI()

# Llamada a la API de chat
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hola, ¿cómo estás?"}]
)

# Imprimir la respuesta
print(response.choices[0].message.content)