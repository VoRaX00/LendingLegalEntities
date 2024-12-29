from fastapi import FastAPI
from routing.admin import router as router_admin
from routing.credit_product import router as router_credit_product
from routing.legal_user import router as router_legal_user
from routing.payment import router as router_payment
from routing.request import router as router_request
app = FastAPI(openapi="/openapi.json", docs_url="/docs")

app.include_router(router_admin)
app.include_router(router_credit_product)
app.include_router(router_legal_user)
app.include_router(router_payment)
app.include_router(router_request)