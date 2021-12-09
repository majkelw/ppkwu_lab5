from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from bs4 import BeautifulSoup
from pathlib import Path

import uvicorn
import requests
import json

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/api/search/{employee}", response_class=HTMLResponse)
def find_employees(request: Request, employee):
    url = "https://panoramafirm.pl/{}".format(employee)
    data = extract_data(url)
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse("exmployees.html", {"request": request, "data": data})


def extract_data(url):
    data = []
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    result = soup.select("script[type=\"application/ld+json\"]")
    for r in result:
        data.append(json.loads(r.contents[0]))
    return data


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8080)
