from fastapi import FastAPI
from routing.admin import router as router_admin
app = FastAPI(openapi="/openapi.json", docs_url="/docs")

app.include_router(router_admin)