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
async def create_vcard(name: str = Form(...), email: str = Form(...), telephone: str = Form(...),
                       fullAddress: str = Form(...)):
    v = vobject.vCard()
    email = email[:-1]
    telephone = telephone[:-1]
    fullAddress = fullAddress[:-1]
    v.add('fn').value = name
    v.add('email').value = email
    v.add('tel').value = telephone
    v.add('addr').value = fullAddress
    print(v.serialize())
    return HTMLResponse(content=v.serialize(),
                        headers={"Content-Type": "text/x-vcard",
                                 "Content-Disposition": "attachment; filename=\"vcard.vcf\""})


def extract_data(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    result = soup.select("script[type=\"application/ld+json\"]")
    data = []
    for r in result:
        one = json.loads(r.contents[0])
        if "address" in one:
            full_address = "{}, {}, {}".format(
                one["address"]["addressLocality"], one["address"]["streetAddress"], one["address"][
                    "postalCode"])
        else:
            full_address = "Brak adresu"
        one.update({'fullAddress': full_address})
        data.append(one)
    return data


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8080)
