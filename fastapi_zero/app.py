from http import HTTPStatus

from fastapi import FastAPI

from fastapi_zero.routers import auth, todos, users
from fastapi_zero.schemas import Message

app = FastAPI(title='Minha API BALA!')

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(todos.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}
