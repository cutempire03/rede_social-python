from fastapi import FastAPI
from src.api.configuration import configure_db, configure_routes

def create_app():
    app = FastAPI()

    configure_db(app)
    configure_routes(app)
    
    return app

app = create_app()