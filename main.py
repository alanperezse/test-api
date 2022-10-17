from typing import Any, List, Union
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Position(BaseModel):
    x: float
    y: float

class Node(BaseModel):
    nodeId: str
    data: Any
    position: Position
    relationships: List[str]

nodes = [
    {
        'nodeId': '1234',
        'data': {
            'label': 'Window',
        },
        'position': {'x': 200, 'y': 200},
        'relationships': []
    },
    {
        'nodeId': '12345',
        'data': {
            'label': 'A/C',
        },
        'position': {'x': 200, 'y': 300},
        'relationships': ['123456',]
    },
    {
        'nodeId': '123456',
        'data': None,
        'position': None,
        'relationships': ['12345',],
    },
    {
        'nodeId': '1234567',
        'data': None,
        'position': None,
        'relationships': ['12345',],
    },
]


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

@app.get('/projects/{project_id}/nodes')
def get_nodes(project_id: str, ):
    print(nodes)
    return nodes

@app.put('/projects/{project_id}/nodes')
def update_nodes(project_id: str, updated_nodes: List[Node]):
    json_nodes = []
    for node in updated_nodes:
        json_nodes.append({
            'nodeId': node.nodeId,
            'data': node.data,
            'position': {'x': node.position.x, 'y': node.position.y},
            'relationships': node.relationships
        })

    for json_node in json_nodes:
        print(json_node)
        
    global nodes
    nodes = json_nodes