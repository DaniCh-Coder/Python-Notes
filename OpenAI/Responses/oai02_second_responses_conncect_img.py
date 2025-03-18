'''
En este script, se muestra cómo utilizar la API de chat de OpenAI para hacer preguntas sobre imágenes
Nota: Este es un ejemplo simple con APIs que usan client.responses
Desde Marzo 2025, OpenAI ha cambiado a la API de Completions.
https://platform.openai.com/docs/guides/images?api-mode=responses
'''
# --------------------------------------------------------------
# Image example of openAI API with responses
# --------------------------------------------------------------
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

response = client.responses.create(
    model="gpt-4o",
    input=[
        {"role": "user", "content": "what teams are playing in this image?"},
        {
            "role": "user",
            "content": [
                {
                    "type": "input_image",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3b/LeBron_James_Layup_%28Cleveland_vs_Brooklyn_2018%29.jpg",
                }
            ],
        },
    ],
)

print(response.output_text)