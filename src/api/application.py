from fastapi import FastAPI
from src.api.configuration import configure_db, configure_routes

app = FastAPI()

def create_app():
    app = FastAPI()

    # iniciar db/tortoise
    configure_routes(app)
    configure_db(app)
    

    return app

app = create_app()
