# Proyecto Entregable 4: CI/CD con Docker y Azure Pipelines

API simple en Flask desplegada automáticamente en Azure mediante un pipeline CI/CD completo. El proyecto vive originalmente en Azure DevOps; este repositorio Git contiene los archivos fuente ya que el proyecto de DevOps no permite compartirse externamente.

## Arquitectura del Pipeline

```
Push a main
    |
    v
[Stage 1: Test]  -->  pytest sobre la app
    |
    v
[Stage 2: Build & Push]  -->  docker build + push a Azure Container Registry (ACR)
    |
    v
[Stage 3: Deploy]  -->  Despliegue en Azure Container Instances (ACI)
    |
    v
http://<dns-label>.westeurope.azurecontainer.io:5000
```

### Flujo detallado

1. **Test** - Instala dependencias y ejecuta `pytest` para validar la app antes de construir la imagen.
2. **Build & Push** - Construye la imagen Docker y la sube al ACR (`acrentregable4xxx.azurecr.io`).
3. **Deploy** - Elimina la instancia ACI anterior (si existe) y crea una nueva con la imagen recién publicada, exponiendo el puerto 5000 con una etiqueta DNS pública.

## Estructura del Proyecto

```
proyecto-entregable-4/
├── app.py                  # API Flask con endpoint raíz
├── Dockerfile              # Imagen basada en python:3.11-slim
├── requirements.txt        # flask==3.0.3, pytest==8.2.0
├── azure-pipelines.yml     # Pipeline CI/CD (3 stages)
├── tests/
│   └── test_app.py         # Test del endpoint /
└── README.md
```

## Requisitos Previos

- Python 3.11+
- Docker
- Cuenta de Azure con:
  - Resource Group (`rg-entregable4`)
  - Azure Container Registry (`acrentregable4xxx`)
  - Service Connection en Azure DevOps (`SC-AZURE`)

## Ejecución Local

### Sin Docker

```bash
pip install -r requirements.txt
python app.py
# Acceder a http://localhost:5000
```

### Con Docker

```bash
docker build -t flask-entregable4 .
docker run -p 5000:5000 flask-entregable4
# Acceder a http://localhost:5000
```

## Tests

```bash
pip install -r requirements.txt
python -m pytest -q
```

## Recursos de Azure Utilizados

| Recurso | Nombre | Propósito |
|---------|--------|-----------|
| Resource Group | `rg-entregable4` | Agrupación de recursos |
| Container Registry (ACR) | `acrentregable4xxx` | Almacén de imágenes Docker |
| Container Instances (ACI) | `aci-entregable4` | Ejecución del contenedor |
| Service Connection | `SC-AZURE` | Autenticación del pipeline con Azure |

## Pipeline CI/CD (`azure-pipelines.yml`)

El pipeline se activa automáticamente con cada push a la rama `main` y ejecuta tres stages secuenciales:

- **Test**: Verifica que Python está disponible en el agente, instala dependencias y corre los tests con pytest.
- **Build & Push**: Se autentica contra el ACR usando credenciales de administrador, construye la imagen Docker etiquetada con el BuildId y la sube al registro.
- **Deploy**: Obtiene credenciales del ACR, elimina cualquier instancia ACI previa y crea una nueva con la imagen actualizada. Al finalizar, imprime la URL pública del contenedor.

El pipeline usa un agente self-hosted (pool `Default`) y PowerShell como shell de scripting.

## Nota sobre el Repositorio

Este proyecto fue desarrollado y ejecutado en Azure DevOps. Dado que no es posible compartir el proyecto de DevOps directamente, los archivos se subieron a este repositorio Git como evidencia del trabajo realizado. El pipeline `azure-pipelines.yml` está configurado para funcionar con la infraestructura de Azure DevOps (agentes, service connections, variables).
