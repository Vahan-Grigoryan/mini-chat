from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api.auth.routes import router as auth_router
from core.config import Settings


app = FastAPI()
app.include_router(auth_router)
app.mount("/images", StaticFiles(directory="images"), name="images")
settings = Settings()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    """
    Change fastapi default error message for be similar to HTTPException
    """
    return JSONResponse(
        status_code=400,
        content=jsonable_encoder({
            "detail": {
                "field": exc.errors()[0]["loc"][-1],
                "message": exc.errors()[0]["msg"]
            }
        })
    )


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=True,
        reload_delay=0
    )
