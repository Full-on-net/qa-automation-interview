# FastAPI QA Challenge 

API de ejemplo construida con **FastAPI** (sin DB externa) que simula gestión de usuarios y pedidos, con **bugs intencionados**. El objetivo es que el candidato diseñe pruebas automatizadas, dockerice el entorno y complete una pipeline de CI.
Necesitarás tener python instalado en tu máquina y docker compose para ejecutar la API.

## 🚀 Ejecución local

Instala dependencias mínimas:
```bash
pip install -r requirements.txt
```

Levanta la API:
```bash
uvicorn app.main:app --reload
```

## 🐳 Docker

Construye y ejecuta:
```bash
docker compose up --build
```

La imagen usa `requirements.txt` de la raíz para instalar dependencias de runtime.

La API estará disponible en `http://localhost:8000`. Y su documentacion en `http://localhost:8000/docs`.
Puedes hacer uso de la documentacion para probar los endpoints manualmente.

## 📚 Endpoints

- `GET /users` — Lista usuarios
- `POST /users` — Crea usuario
- `GET /orders` — Lista pedidos
- `POST /orders` — Crea pedido
- `GET /orders/{user_id}` — Lista pedidos de un usuario

### Ejemplos curl

```bash
curl http://localhost:8000/users
curl -X POST http://localhost:8000/users -H "Content-Type: application/json" -d '{"name":"Carol","email":"carol@example.com"}'

curl http://localhost:8000/orders
curl -X POST http://localhost:8000/orders -H "Content-Type: application/json" -d '{"user_id":0,"product":"Notebook","quantity":2,"price":"12.99"}'
curl http://localhost:8000/orders/0
```

