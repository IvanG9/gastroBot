# 🍳 GastroBot — Asistente de Cocina con Django + Tailwind CSS

GastroBot es una aplicación web que permite a los usuarios registrarse, iniciar sesión, consultar recetas y utilizar un asistente de cocina con inteligencia artificial. Está construida con Django, Django Tailwind y aprovecha modernas tecnologías de frontend para una experiencia visual atractiva y fluida.

---

## ✅ Requisitos

- **Python** 3.11 o superior  
- **Node.js** (versión LTS recomendada)  
- **npm**  
- **Git** (opcional, si clonas el repositorio)

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/IvanG9/gastroBot
cd gastrobot
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv env
.\env\Scripts\Activate.ps1   # En Windows
# source env/bin/activate   # En Linux o macOS
```

### 3. Instalar dependencias del backend

```bash
pip install -r requirements.txt
```

---

## 🎨 Configuración de Tailwind CSS

### 4. Instalar dependencias de Node.js para Tailwind

```bash
python manage.py tailwind install
```

### 5. Iniciar el compilador de Tailwind (en una terminal aparte)

```bash
python manage.py tailwind start
```

---

## 🗄️ Base de Datos y Migraciones

```bash
python manage.py migrate
```

---

## 👤 Crear un superusuario (opcional)

```bash
python manage.py createsuperuser
```

---

## 🖥️ Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

Abre en el navegador:  
📍 http://127.0.0.1:8000

---

## 📦 Regenerar `requirements.txt` (si instalas nuevas dependencias)

```bash
pip freeze > requirements.txt
```

---

## 📁 Estructura de Carpetas Sugerida

```
gastrobot/
│
├── core/            # Página de bienvenida, home
├── usuarios/        # Registro, login, logout, perfiles
├── recetas/         # Modelo y lógica de recetas
├── asistente/       # Chatbot de cocina con IA
├── theme/           # Tailwind CSS y configuración
├── templates/       # Plantillas globales
├── static/          # Archivos estáticos
└── manage.py
```

---

## ✨ Autor

Desarrollado por **Iván Perales López**  
📚 Ciclo Formativo DAM — Desarrollo de Aplicaciones Multiplataforma
