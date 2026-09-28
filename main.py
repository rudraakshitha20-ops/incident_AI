from fastapi import FastAPI

from app1.api.routes import router


app = FastAPI(
    title="Incident AI Agent",
    description="AI-powered incident analysis with Hindsight memory",
    version="1.0.0"
)


app.include_router(router)