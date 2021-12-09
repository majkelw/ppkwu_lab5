from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from bs4 import BeautifulSoup
import jinja2
import uvicorn
import requests
import json

app = FastAPI()


@app.get("/api/search/{employee}", response_class=HTMLResponse)
def find_employees(request: Request, employee):
    data = []
    url = "https://panoramafirm.pl/{}".format(employee)
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    result = soup.select("script[type=\"application/ld+json\"]")
    for r in result:
        data.append(json.loads(r.contents[0]))
    templates = Jinja2Templates(directory="../templates")
    return templates.TemplateResponse("index.html", {"request": request, "data": data})


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8080)
