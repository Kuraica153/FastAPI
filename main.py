from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import user_router
from configs.database import create_tables

origins = [ 'http://localhost:5173' ]

create_tables()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(user_router.router)