from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.api.v1 import email_routes, calendar_routes, hello
from app.config.settings import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)

# Serve static files (e.g., favicon)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Route for favicon.ico
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")

# Include routers
app.include_router(hello.router, prefix="/api/v1/hello", tags=["Hello"])
app.include_router(email_routes.router, prefix="/api/v1/email", tags=["Email"])
app.include_router(calendar_routes.router, prefix="/api/v1/calendar", tags=["Calendar"])

@app.get("/")
def root():
    return {
        "message": f"{settings.app_name} API is running 🚀",
        "env": settings.app_env
    }
