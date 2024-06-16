import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api.auth.routes import router as auth_router
from core.config import Settings


app = FastAPI()
app.include_router(auth_router)
app.mount("/images", StaticFiles(directory="images"), name="images")
settings = Settings()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=True,
        reload_delay=0
    )
