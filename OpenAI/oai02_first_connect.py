'''
En este script, se muestra cómo utilizar la API de chat de OpenAI para generar texto.
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

models = client.models.list()
for model in models:
    print(model.id)

# Llamada a la API de chat
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hola, ¿cómo estás?"}]
)

# Imprimir la respuesta
print(response.choices[0].message.content)