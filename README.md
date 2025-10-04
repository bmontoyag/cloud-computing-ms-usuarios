# Microservicio de Usuarios

Gestión de usuarios y roles para el sistema de cotizaciones.

## Arquitectura
- FastAPI + AWS Lambda + API Gateway
- Base de datos: Amazon Aurora (PostgreSQL)
- Auth: AWS Cognito (futuro)

## Ejecutar local
```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Despliegue con SAM
```bash
sam build
sam deploy --guided
```

## Variables de entorno
Ver `.env.example` y configura estas variables en Lambda o localmentte.

## Endpoints
- GET /api/usuarios
- POST /api/usuarios

## Diagrama ER
Ver `diagram_usuarios_er.md`.
