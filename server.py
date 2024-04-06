from fastapi import FastAPI, Response, Request
from src import services, utils

app = FastAPI()


@app.get('/hello')
async def hello():
    return {'msg': 'Hello!'}


@app.get('/user')
async def get_user(response : Response, user_id: int | None = None):
    res: utils.Res = services.UserService().get_user(user_id=user_id)
    return res

@app.post('/user/create')
async def create_user(payload: Request):
    payload = await payload.json()
    return services.UserService().create_user(**payload)