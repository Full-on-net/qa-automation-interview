# Instructions - QA Automation Challenge

## Objetivo
Demostrar habilidades en diseño y análisis de API, automatización de pruebas, Docker e integración continua sobre una API FastAPI con errores intencionados.

## Tareas

1. **Identificar bugs en la API**
   - Revisa `/app` y documenta problemas de validación, tipos, respuestas y códigos de estado.

2. **Crear un framework de automatización desde cero**
   - Crea tu estructura en `/tests/` (por ejemplo: `behave`).
   - Añade dependencias de test en un `requirements.txt` dentro de `tests/` (mantén las dependencias de runtime en el `requirements.txt` de la raíz, usado por Docker y ejecución local).

3. **Implementar test cases automatizados**
   - Cubre `GET /users`, `POST /users`, `GET /orders`, `POST /orders`, `GET /orders/{user_id}`.
   - Incluye casos negativos (email inválido, cantidad negativa, usuario inexistente, etc.).

4. **Dockerizar los tests**
   - Añade un servicio o imagen para ejecutar las pruebas (puede ser otro `Dockerfile` o una sección en `docker-compose.yml`).

5. **Completar la pipeline de CI**
   - Edita `.github/workflows/ci.yml` para:
     - Instalar dependencias.
     - Levantar la API.
     - Ejecutar los tests y pasar o fallar la pipeline si hay test cases fallando.

6. **Documentar en `NOTES.md`**
   - Explica decisiones, cómo ejecutar tus pruebas y qué cubren.
   - Enumera bugs detectados y posibles mejoras.
   - Añade cualquier otra información relevante.


## 🧩 Qué debe hacer el candidato

- Todo el código que se cree tiene que estar contenido dentro de la carpeta /tests/, no se puede modificar ningun otro fichero
- Crear desde cero un entorno de automatización de pruebas (BDD recomendado behave) dentro de la carpeta /tests/.
- Escribir test cases que prueben los endpoints y detecten bugs si los hay. Los tests pueden entregarse en estado failed si detectan un bug. 
- Dockerizar el entorno de pruebas.
- Completar la pipeline de CI en `.github/workflows/ci.yml` para que se ejecute cuando se haga una pull request a la rama `main`.


## Entrega
- Enlace al repositorio o archivo `.zip` con la solución completa.