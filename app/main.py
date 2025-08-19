from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, List
import requests

app = FastAPI()

class StatusResponse(BaseModel):
    listLinks: List[str]

class SSiteStatus(BaseModel):
    available: bool
    code: int
    info: str

class SRequestModel(BaseModel):
    request: Dict[str, SSiteStatus]

@app.post("/check", response_model=SRequestModel)
def checkAvailbility(links: StatusResponse):
    print(links.listLinks)  
    return{
  "request": {
    "additionalProp1": {
      "available": True,
      "code": 0,
      "info": "string"
    }
  }
}