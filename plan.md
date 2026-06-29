# Plan - Entregable 4: CI/CD con Docker y Azure Pipelines

## Rúbrica (resumen)

| Criterio | Peso | Estado |
|---|---|---|
| Dockerfile bien estructurado y funcional | 20% | ⬜ Pendiente |
| Pipeline CI bien definido con etapas claras | 30% | ⬜ Pendiente |
| Pruebas automatizadas dentro del pipeline | 20% | ⬜ Pendiente |
| Imagen subida y funcional en Docker Hub | 20% | ⬜ Pendiente |
| Documentación README.md | 10% | ⬜ Pendiente |

## Ya completado

- [x] `app.py` — Flask app con ruta `/` que devuelve saludo
- [x] `tests/test_app.py` — Test básico (necesita fix de indentación)
- [x] `requirements.txt` — flask + pytest

## Tareas pendientes

### 1. Fix test_app.py (indentación rota)
- Corregir indentación del test
- Añadir assert para verificar status 200 y contenido respuesta

### 2. Dockerfile (20% rúbrica)
- Imagen base: `python:3.12-slim`
- `WORKDIR /app`
- Copiar `requirements.txt` e instalar deps (capa cacheada)
- Copiar resto del código
- `EXPOSE 5000`
- `CMD ["python", "app.py"]`

### 3. Pipeline Azure Pipelines (30% rúbrica)
Archivo: `azure-pipelines.yml`
- **Trigger**: push a `main`
- **Stage 1 - Test**: checkout → UsePythonVersion → install deps → pytest (publicar resultados)
- **Stage 2 - Build & Push**: checkout → Docker task login → build imagen → push a Docker Hub
- Variables/secretos: `DOCKER_USERNAME`, `DOCKER_PASSWORD` (configurar en Azure DevOps pipeline variables)

### 4. Configurar secretos Docker Hub (20% rúbrica)
- Crear cuenta/token en Docker Hub
- Añadir variables secretas en Azure DevOps → Pipeline → Variables (o crear Service Connection tipo Docker Registry)

### 5. README.md (10% rúbrica)
- Descripción del proyecto
- Requisitos previos
- Instrucciones para construir imagen local
- Instrucciones para ejecutar contenedor
- Estructura del proyecto
- Explicación del pipeline CI/CD
- Mínimo 2 páginas, Arial 12, interlineado 1.5

## Orden de ejecución

1. Fix tests
2. Crear Dockerfile
3. Probar Docker local (`docker build` + `docker run`)
4. Crear pipeline `azure-pipelines.yml`
5. Crear README.md
6. Init git repo, push a Azure Repos
7. Configurar secrets Docker Hub en Azure DevOps
8. Verificar pipeline ejecuta correctamente
