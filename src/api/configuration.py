from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from src.api.routes import users, home, post

def configure_routes(app: FastAPI):
    app.include_router(users.router)
    app.include_router(home.router)
    app.include_router(post.router)

def configure_db(app: FastAPI):
    register_tortoise(
        app=app,
        # db_url='postgres://postgres:qwerty123@localhost:5432/events'
        # db_url='sqlite://db.sqlite3',
        modules={"models": ["src.datalayer.models.user"]},

        config={
            'connections': {
                # 'default': 'postgres://postgres:qwerty123@localhost:5432/events'
                'default': 'sqlite://db.sqlite3'
            },
            'apps': {
                'models': {
                    'models': [
                        'src.datalayer.models.user',
                        'src.datalayer.models.post'
                    ],
                    'default_connection': 'default',
                }
            }
        },
        generate_schemas=True,
        add_exception_handlers=True,
    )