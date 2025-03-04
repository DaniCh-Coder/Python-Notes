# Uso de la API de OpenAI: Facturación y Primeros Pasos
Esta guía asume que:
1. ya tienes una cuenta en OpenAI y has creado una clave de API.
2. ya tienes algo de experiencia en APIS.

## **1️⃣ Configurar la facturación y el pago**
OpenAI requiere que configures un método de pago antes de poder usar su API. Para hacerlo:

1. **Ve a la sección de facturación** en OpenAI: [https://platform.openai.com/account/billing](https://platform.openai.com/account/billing)  
2. **Añade un método de pago** (tarjeta de crédito o débito).  
3. **Elige un presupuesto**: OpenAI te permite establecer un límite de gasto mensual para evitar costos inesperados.

📌 **Consejo**:  
Para aprender, lo mejor es empezar con un presupuesto pequeño, como $5 o $10 al mes, hasta que entiendas bien cómo funcionan los costos.

---

## **2️⃣ Entender los costos de la API**
OpenAI cobra según la cantidad de *tokens* utilizados.  

- Un *token* es una unidad de texto (una palabra suele ser ~1.3 tokens).  
- Se cobran tokens de entrada (lo que envías) y de salida (lo que recibes).  
- Cada modelo tiene precios diferentes:

| Modelo         | Entrada (por 1k tokens) | Salida (por 1k tokens) |
|---------------|-----------------------|-----------------------|
| **GPT-4-turbo**  | $0.01                 | $0.03                 |
| **GPT-4**       | $0.03                 | $0.06                 |
| **GPT-3.5-turbo** | $0.001                 | $0.002                 |

📌 **Consejos para ahorrar dinero**:  
1. Usa **GPT-3.5-turbo** para pruebas, ya que es mucho más barato.  
2. Reduce la cantidad de tokens en tus peticiones (mantén los mensajes cortos y concisos).  
3. Si usas un historial de conversación, asegúrate de no enviar mensajes innecesarios.  

---

## **3️⃣ Primeros pasos con Python y OpenAI API**
Ya que tienes experiencia con APIs y WhatsApp de Meta, te recomiendo conectarte a la API de OpenAI usando `openai` y `pydantic`.

### **1. Instalar las dependencias**  
```bash
pip install openai pydantic pydantic-ai
```

### **2. Configurar la clave de API en una variable de entorno**  
- Ve a [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys) y genera una clave.  
- Guarda la clave como variable de entorno en tu sistema.  

En Linux/Mac:
```bash
export OPENAI_API_KEY="tu_clave_aqui"
```

En Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="tu_clave_aqui"
```

### **3. Hacer una prueba con la API en Python**  
```python
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "¿Cómo funciona la API de OpenAI?"}],
    max_tokens=50
)

print(response["choices"][0]["message"]["content"])
```

### **4. Optimizar costos con `pydantic-ai`**  
- `pydantic-ai` permite estructurar mejor las solicitudes.  
- Lo veremos en detalle más adelante, pero te adelanto una forma optimizada de hacer una consulta:

```python
from pydantic_ai.openai import OpenAIChat

chat = OpenAIChat(model="gpt-3.5-turbo", max_tokens=50)

respuesta = chat.ask("Explica la API de OpenAI en pocas palabras.")
print(respuesta)
```

---

## **Siguientes pasos**
- **Confirma si ya configuraste tu tarjeta y límite de gastos.**  
- **Prueba el código anterior y dime si te da algún error.**  
- **Cuando estés listo, avanzamos a mejorar la eficiencia de llamadas a la API.** 🚀
