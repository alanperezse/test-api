from typing import Any, List, Union
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Position(BaseModel):
    x: float
    y: float

class Node(BaseModel):
    nodeID: str
    name: str
    data: Any
    position: Position
    relationships: List[str]

nodes = [
    {
        'nodeID': '1234',
        'data': {
            'label': 'Window',
        },
        'name': 'Window',
        'position': {'x': 200, 'y': 200},
        'relationships': []
    },
    {
        'nodeID': '12345',
        'data': {
            'label': 'A/C',
        },
        'name': 'A/C',
        'position': {'x': 200, 'y': 300},
        'relationships': ['123456', '1234567']
    },
    {
        'nodeID': '123456',
        'data': None,
        'name': 'some name',
        'position': None,
        'relationships': ['12345',],
    },
    {
        'nodeID': '1234567',
        'data': None,
        'name': 'some other name',
        'position': None,
        'relationships': [],
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
    global nodes
    for updated_node in updated_nodes:
        for node in nodes:
            if node['nodeID'] == updated_node.nodeID:
                node['data'] = updated_node.data
                node['position'] = updated_node.position
                node['relationships'] = updated_node.relationships
                node['name'] = updated_node.name
        