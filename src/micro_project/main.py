from fastapi import FastAPI
from enum import Enum


dev_tools = [{'frontend': 'next.js', 'backend': 'fastapi', 'mobile': 'react native', 'aiops': 'pydanticai', 'devops': 'docker', 'db': 'postgresql'}]


class ModelName(str, Enum):
    alexnet =  'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'AI model evolution'}


# Path Parameter with Function Parameters
@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {'file_path': file_path}


# Query Parameter with Function Query Parameter
@app.get('/tools/')
async def read_dev_tools(skip: int = 0, limit: int = 5):
    return dev_tools[skip: skip + limit]