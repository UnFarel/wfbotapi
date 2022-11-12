from typing import Union

from fastapi import FastAPI
import json


app = FastAPI()


@app.get("/")
def read_root():
    with open("json-HW-IT.json") as rf:
        data = json.load(rf)
    return(data)
