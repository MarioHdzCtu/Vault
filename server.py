from fastapi import FastAPI

app = FastAPI()


@app.get('/hello')
async def hello():
    return {'msg': 'Hello!'}


@app.get('/bye')
async def bye():
    return {'msg': 'Bye!'}
