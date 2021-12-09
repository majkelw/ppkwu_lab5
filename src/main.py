from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from bs4 import BeautifulSoup
import vobject
import uvicorn
import requests
import json

app = FastAPI()


@app.get("/api/search/{employee}", response_class=HTMLResponse)
def find_employees(request: Request, employee):
    url = "https://panoramafirm.pl/{}".format(employee)
    data = extract_data(url)
    templates = Jinja2Templates(directory="../templates")
    return templates.TemplateResponse("exmployees.html", {"request": request, "data": data})


@app.post("/api/vcard", response_class=FileResponse)
def create_vcard(name: str = Form(...), email: str = Form(...), telephone: str = Form(...)):
    v = vobject.vCard()
    print(name)
    print(email)
    v.add('fn').value = name
    v.add('email').value = email
    v.add('tel').value = telephone
    return HTMLResponse(content=v.serialize(),
                        headers={"Content-Type": "text/x-vcard",
                                 "Content-Disposition": "attachment; filename=\"VCARD.VCF\""})


def extract_data(url):
    data = []
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    result = soup.select("script[type=\"application/ld+json\"]")
    for r in result:
        data.append(json.loads(r.contents[0]))
    return data


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8080)
