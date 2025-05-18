# asistente/services.py
import os
import requests
from dotenv import load_dotenv
from .prompts import cooking_prompt
import json
import openai
from openai import OpenAI

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def ask_groq(message, temperature=0.7, top_p=0.9):
    if not GROQ_API_KEY:
        return {"error": "No se ha definido la clave API de Groq."}

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    prompt = cooking_prompt(message)

    payload = {
        "model": "llama3-70b-8192",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
        "top_p": top_p,
    }

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30,
        )
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"]

        # Intenta parsear como JSON
        receta = json.loads(content)
        return receta
    except requests.exceptions.RequestException as e:
        return {"error": f"Ocurrió un error al conectar con el asistente: {e}"}
    except (KeyError, json.JSONDecodeError):
        return {"error": "Error: Respuesta inesperada del modelo. Verifica el formato JSON."}


def generar_imagen_receta(titulo):
    prompt = (
        f"A professional, high-resolution food photo of the dish '{titulo}', beautifully plated, "
        f"restaurant presentation, top-down view with vibrant colors."
    )

    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            style="vivid"
        )
        return response.data[0].url
    except Exception as e:
        print("Error generando imagen:", e)
        return None