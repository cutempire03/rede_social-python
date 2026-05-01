from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

def configure_db(app: FastAPI):
    register_tortoise(
        app=app,
        # db_url='postgres://postgres:qwerty123@localhost:5432/events'
        # db_url='sqlite://db.sqlite3',

        config={
            'connections': {
                # 'default': 'postgres://postgres:qwerty123@localhost:5432/events'
                'default': 'sqlite://db.sqlite3'
            },
            'apps': {
                'models': {
                    'models': [
                        'src.datalayer.models.user'
                    ],
                    'default_connection': 'default',
                }
            }
        },
        generate_schemas=True,
        add_exception_handlers=True,
    )