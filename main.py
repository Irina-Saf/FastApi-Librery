from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
from core.db import SessionLocal
from models.router import router_genre, router_book, router_author


app = FastAPI(title="library")


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


app.include_router(router_genre)
app.include_router(router_book)
app.include_router(router_author)
