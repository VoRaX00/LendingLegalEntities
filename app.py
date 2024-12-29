from fastapi import FastAPI
from routing    
app = FastAPI(openapi="/openapi.json", docs_url="/docs")

app.include_router()