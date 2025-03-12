'''
Este script prueba la API de chat de OpenAI para generar texto. 
Aquí se muestra cómo utilizar la API de chat para simular una conversación entre un usuario y un asistente de IA. 
En este caso, el asistente es un modelo de lenguaje GPT-3.5-turbo de OpenAI.
model: Aquí se especifica el modelo que deseas usar. En este caso, gpt-3.5-turbo es el más adecuado para pruebas económicas.
messages: Esta es una lista de mensajes que simulan una conversación. El primer mensaje define el comportamiento del modelo (en este caso, como un asistente útil), y el segundo es un mensaje del usuario, que es la pregunta que deseas que el modelo responda.
response: El resultado de la API contiene la respuesta generada por el modelo, y puedes acceder a ella mediante response['choices'][0]['message']['content'].
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
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Eres un asistente util"},
        {"role": "user", "content": "¿Cómo se utiliza la API de OpenAI para generar texto?"}
    ]
    
)

# Imprimir la respuesta
print(response.choices[0].message.content)