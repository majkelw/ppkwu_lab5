from fastapi import FastAPI
from bs4 import BeautifulSoup
import uvicorn
import requests
import json

app = FastAPI()


@app.get("/api/search/{employee}")
def find_employees(employee):
    data = []
    url = "https://panoramafirm.pl/{}".format(employee)
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    result = soup.select("script[type=\"application/ld+json\"]")
    for r in result:
        data.append(json.loads(r.contents[0]))
    return data


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8080)
