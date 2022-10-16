from turtle import st
from typing import Union
from unicodedata import name
from xmlrpc.client import boolean
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

people = {'people': []}

class Project_Info(BaseModel):
    baud_rate: int
    initials: str
    name: str = None
    dbc_file: str = None
    blacklist_file: str = None

class Play(BaseModel):
    play: bool

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthcheck")
def get_healthcheck():
    return {'healthcheck': 'ok'}

@app.get("/projects/{project_id}/packets")
def get_people(
    project_id: int,
    size: int,
    sort: str,
    node: Union[str, None] = None,
    before: Union[str, None] = None,
    after: Union[str, None] = None,
    ):
    print('Details:')
    print(f'project_id: {project_id}')
    print(f'size: {size}')
    print(f'sort: {sort}')
    
    if before is not None:
        print(f'before: {before}')
    if after is not None:
        print(f'after: {after}')
    if node is not None:
        print(f'node: {node}')

@app.put("/projects/{project_id}/play")
def get_people(project_id: str, play: Play):
    print('Play details')
    print(f'project_id: {project_id}')
    print(play.play)


@app.put("/projects/{project_id}/play")
def get_people(project_id: str, play: Play):
    print('Play details')
    print(f'project_id: {project_id}')
    print(play.play)

@app.put("/projects/{project_id}/play")
def get_people(project_id: str, play: Play):
    print('Play details')
    print(f'project_id: {project_id}')
    print(play.play)


@app.get('/projects/{project_id}/sensors')
def get_ids(project_id: str):
    return {
        '1234': {
            'label': 'A/C',
            'active': True
        },
        '12345': {
            'label': 'Window',
            'active': True
        },
        '123456': {
            'label': None,
            'active': True
        },
    }

@app.get('/projects/{project_id}/nodes')
def get_nodes(project_id: str, ):
    return [
        {
            '_id': '1234',
            'data': {
                'label': 'Window',
            },
            'position': {'x': 200, 'y': 200},
            'relationships': [

            ]
        },
        {
            '_id': '12345',
            'data': {
                'label': 'A/C',
            },
            'position': {'x': 200, 'y': 300},
            'relationships': [
                '123456'
            ]
        },
        {
            '_id': '123456',
            'data': {
                'label': 'Motor'
            },
            'position': {'x': 400, 'y': 300},
            'relationships': [
                '12345',
            ],
        },
    ]
