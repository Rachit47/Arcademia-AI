from fastapi import FastAPI
from application.api.v1 import health
from application.api.v1 import ai

app = FastAPI(
    title="Arcademia AI",
    description="Agentic Game Intelligence Platform",
    version="1.0"
)

# Register health router
app.include_router(
    health.router,
    prefix = "/api/v1"
)

# Register AI router
app.include_router(
    ai.router,
    prefix = "/api/v1"
)
