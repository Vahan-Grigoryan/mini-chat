import uvicorn
from src.core.config import CommonSettings
from fastapi import FastAPI
from auth.router import router as auth_router


app = FastAPI()
app.include_router(auth_router)
common_settings = CommonSettings()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=common_settings.host,
        port=common_settings.port,
        reload_delay=0
    )
