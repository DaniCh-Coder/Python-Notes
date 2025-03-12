# Este script lista los modelos de OpenAI disponibles en la cuenta
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