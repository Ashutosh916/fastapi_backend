# FastAPI Auth + AI Integration

A backend project built with FastAPI demonstrating user authentication, protected routes, and external AI API integration.

## Features
- User signup and login with JWT authentication
- Protected API routes
- Async-safe external AI text generation
- Clean project structure (routes, schemas, utils)
- API testing via Postman and Swagger

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- JWT
- Argon2
- External AI APIs (Gemini)
- Postman, Swagger

## Run locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
