from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api.auth.routes import router as auth_router
from api.chat.routes import router as chat_router
from core.config import Settings


app = FastAPI()
app.include_router(auth_router)
app.include_router(chat_router)
app.mount("/images", StaticFiles(directory="images"), name="images")
settings = Settings()

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    """
    Change fastapi default error message for be similar to HTTPException
    """
    errors = []
    for error in exc.errors():
        errors.append({
            "field": error["loc"][-1],
            "message": error["msg"]
        })
    return JSONResponse(
        status_code=400,
        content=jsonable_encoder({"detail": errors})
    )


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=True,
        reload_delay=0
    )
