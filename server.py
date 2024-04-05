from fastapi import FastAPI, Response
from src import services, utils

app = FastAPI()


@app.get('/hello')
async def hello():
    return {'msg': 'Hello!'}


@app.get('/user')
async def bye(response : Response, user_id: int | None = None):
    res: utils.Res = services.UserService().get_user(user_id=user_id)
    return res