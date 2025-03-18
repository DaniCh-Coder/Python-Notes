'''
This script is used to connect to the OpenAI API and stream responses in real-time.
stream=True en la API de OpenAI permite recibir la respuesta en partes a medida que se genera, 
en lugar de esperar a que se complete toda la respuesta. 
Esto mejora la velocidad de entrega y la experiencia del usuario en aplicaciones interactivas, como chatbots en tiempo real. 
No aumenta el costo, ya que el cobro se basa en la cantidad de tokens usados, sin importar si se transmiten de una vez (stream=False)
o en flujo (stream=True).
'''
#
# streammed responses in real-time
#

from openai import OpenAI
client = OpenAI()

stream = client.responses.create(
    model="gpt-4o",
    input=[
        {
            "role": "user",
            "content": "Decí, 'Pablito, clavó un clavito. ¿Quién clavó un clavito?, que clavito clavó Pablito.' diez veces más rápido.",
        },
    ],
    stream=True,
)

for event in stream:
    print(event)