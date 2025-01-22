from typing import Annotated

from fastapi import Request, FastAPI, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory = 'templates')

logs = []

class event:
    def __init__(self, ce_time, ce_type, ce_source, ce_id, ce_specversion, body):
        self.ce_time = ce_time
        self.ce_type = ce_type
        self.ce_source = ce_source
        self.ce_id = ce_id
        self.ce_specversion = ce_specversion
        self.body = body


@app.post("/event")
async def getNewEvent(request: Request, 
                      ce_time: Annotated[str | None, Header()] = None,
                      ce_type: Annotated[str | None, Header()] = None,
                      ce_source: Annotated[str | None, Header()] = None,
                      ce_id: Annotated[str | None, Header()] = None,
                      ce_specversion: Annotated[str | None, Header()] = None):
    print(ce_time)
    print(ce_type)
    print(ce_source)
    print(ce_id)
    print(ce_specversion)
    body = await request.json()
    print(body)
    logs.append(event(ce_time, ce_type, ce_source, ce_id, ce_specversion, body))
    return "204"

@app.get("/logs")
async def getLog(request: Request):
    return templates.TemplateResponse(
    'logs.html',
    {'request': request, 'events': logs})
