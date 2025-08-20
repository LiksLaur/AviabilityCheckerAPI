from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, List
import requests
import re

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
    result = {}
    links.listLinks = set(links.listLinks)
    for link in links.listLinks:
        try:
            r = requests.get(link)

            code = int(re.findall(r'\[(.*?)\]', str(r))[0])
            available = True if code >=200 and code <= 309 else False
            info = re.sub(r'\[.*?\]', '', str(r))[1:-1]

            print(link, code, available, info)  
            result[link] = SSiteStatus(available=available, code=code, info=info)
        
        except requests.exceptions.ConnectionError as err:
            result[link] = SSiteStatus(available=False, code=503, info=f"Service Unavailable: {str(err)}")
        except requests.exceptions.Timeout as err:
            result[link] = SSiteStatus(available=False, code=408, info=f"Request Timeout: {str(err)}")
        except requests.exceptions.RequestException as err:
            result[link] = SSiteStatus(available=False, code=400, info=f"Bad request: {str(err)}")
        except Exception as err:
            result[link] = SSiteStatus(available=False, code=1, info=f"Err: {str(err)}")
    return SRequestModel(request=result)
    
@app.get("/")
def hi():
    return"hi"