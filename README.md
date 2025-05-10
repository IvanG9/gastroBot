
# 🧑‍🍳 Proyecto Gastrobot con Django + Tailwind CSS

Este proyecto es una aplicación web de recetas con autenticación de usuarios y diseño moderno usando Tailwind CSS.

---

## 🚀 Requisitos

- Python 3.11 o superior
- Node.js (versión LTS recomendada)
- npm
- Git (opcional)

---

## 🛠️ Instalación

### 1. Clonar el repositorio (si aplica)

```bash
git clone https://github.com/tu-usuario/proyecto-recetas.git
cd proyecto-recetas
```

### 2. Crear y activar un entorno virtual

```bash
python -m venv env
.\env\Scripts\Activate.ps1   # En Windows
source env/bin/activate      # En Linux
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 🎨 Configurar Tailwind CSS

### 4. Inicializar e instalar Tailwind (si no está hecho) en este proyecto esta hecho

```bash
python manage.py tailwind init theme
python manage.py tailwind install
```

### 5. Iniciar el compilador de estilos (en una terminal aparte)

```bash
python manage.py tailwind start
```

---

## 🔧 Migraciones y base de datos

```bash
python manage.py migrate
```

---

## 🧪 Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

---

## 🖥️ Ejecutar el servidor

```bash
python manage.py runserver
```

Visita: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📦 Generar `requirements.txt` actualizado

```bash
pip freeze > requirements.txt
```

---

## 📝 Notas

- El archivo `base.html` ya incluye el CSS generado por Tailwind (`css/dist/styles.css`)
- Los formularios están personalizados con filtros (`add_class`) definidos en `recetas/templatetags/form_filters.py`
- Usa `tailwind==3.7.0` para evitar errores con Django

---

## ✨ Autor

Proyecto desarrollado por **Iván Perales López**  
Ciclo DAM – Desarrollo de Aplicaciones Multiplataforma
