# FastAPI QA Challenge 

Este proyecto es una pequeña API construida con **FastAPI**, que contiene **errores intencionados** en su implementación.
Tu misión es **detectar estos errores** y **crear un framework de automatización de pruebas desde cero**.
Necesitarás tener python instalado en tu máquina. 
---

## 🚀 Cómo ejecutar la API

Instala dependencias y levanta el servidor:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Por defecto la API estará disponible en `http://localhost:8000`. Y su documentacion en `http://localhost:8000/docs`.
Puedes hacer uso de la documentacion para probar los endpoints manualmente.

---

## 🧪 Pruebas

No se incluye framework de testing preconfigurado. Debes crear tu framework (por ejemplo, `behave`) dentro de la carpeta `tests/`.

Se recomienda cubrir:

- `GET /tasks`
- `POST /tasks`
- `DELETE /tasks`
- `PUT /tasks`

---

## 🧩 Qué debe hacer el candidato

- Crear desde cero un entorno de automatización de pruebas (BDD recomendado behave).
- Escribir test cases que prueben los endpoints y detecten bugs. Los tests pueden entregarse en estado failed si detectan un bug. 