
from fastapi import FastAPI
from routes import auth_routes, recharge_routes, bill_routes, dashboard_routes

app = FastAPI()

app.include_router(auth_routes.router, prefix="/api")
app.include_router(recharge_routes.router, prefix="/api")
app.include_router(bill_routes.router, prefix="/api")
app.include_router(dashboard_routes.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "DeshPay API Running"}
