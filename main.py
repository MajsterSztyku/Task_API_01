from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import csv
import json
import io

app = FastAPI()

@app.post("/csv_to_json")
async def csv_to_json(file: UploadFile = File(...)):
    # with open("test.csv",mode = "+r",newline="")as plik:
    #     read = csv.reader(plik)
    # <--- nie działa cały komentarz. Zrozumieć czemu
    content = await file.read()
    file_content = io.StringIO(content.decode("utf-8"))
    reader = csv.DictReader(file_content)
    rows= []
    for row in reader:
        rows.append(row)
    return rows
