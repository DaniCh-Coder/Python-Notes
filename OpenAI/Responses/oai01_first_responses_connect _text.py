'''
En este script, se muestra cómo utilizar la API de chat de OpenAI para generar texto.
Nota: Este es un ejemplo simple con APIs que usan client.resonses
Desde Marzo 2025, OpenAI ha cambiado a la API de Completions.
Para más información:
https://platform.openai.com/docs/guides/responses-vs-chat-completions
https://beta.openai.com/docs/api-reference/completions/create
https://platform.openai.com/docs/api-reference/responses
'''
from openai import OpenAI
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Obtener la clave API desde el archivo .env
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# Crear un cliente con la nueva versión del SDK
# Detecta la clave automáticamente de OPENAI_API_KEY
# No hay que pasar la clave como parámetro
client = OpenAI()

# Llamada a la API de chat
response = client.responses.create(
    model="gpt-4o",
    input="Write a one-sentence bedtime story about a unicorn."
)

# Imprimir la respuesta
print(response.output_text)