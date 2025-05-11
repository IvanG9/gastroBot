# asistente/services.py
import os
import requests
from dotenv import load_dotenv
from .prompts import cooking_prompt

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def ask_groq(message, temperature=0.7, top_p=0.9):
    if not GROQ_API_KEY:
        return "Error: No se ha definido la clave API de Groq."

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    prompt = cooking_prompt(message)

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "user", "content": prompt}
        ],
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
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Ocurrió un error al conectar con el asistente: {e}"
    except KeyError:
        return "Error: Respuesta inesperada del modelo."
