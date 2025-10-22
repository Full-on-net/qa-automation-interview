# FastAPI QA Challenge 

Este proyecto es una API sencilla construida con **FastAPI** que contiene errores intencionados.
Tu objetivo es demostrar tu capacidad para **detectar bugs** y **automatizar pruebas básicas** sobre endpoints REST.
Necesitarás tener python instalado en tu máquina. 

---

## 🚀 Cómo ejecutar la API

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

La API estará disponible en `http://localhost:8000`. Y su documentacion en `http://localhost:8000/docs`.
Puedes hacer uso de la documentacion para probar los endpoints manualmente.

---

## ▶️ Pruebas BDD (behave)

Desde la raíz del proyecto:

```bash
behave
```

Si tu entorno busca por defecto la carpeta `features` en la raíz, también puedes ejecutar:

```bash
behave tests/features
```