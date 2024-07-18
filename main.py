from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import csv
import json
import io

app = FastAPI()

@app.post("/csv_to_json")
async def csv_to_json(file: UploadFile = File(...)):
    #walidacja pliku. Sprawdzanie czy plik jest w rozszerzeniu csv
    if file.content_type != "text/csv":
        raise HTTPException(status_code=400, detail="wrong file")
    # with open("test.csv",mode = "+r",newline="")as plik:
    #     read = csv.reader(plik)
    #powyższy komentarz nie działa. FastAPI przy wywołaniu wyczytuje plik z wywołania funkcji
    

    content = await file.read()
    file_content = io.StringIO(content.decode("utf-8"))
    reader = csv.DictReader(file_content) # dictreader pozwala odczytać plik csv w postaci słownika
    json_data = {}

    for row in reader:
        for key, value in row.items():
            if key in json_data:
                json_data[key].append(value)
            else:
                json_data[key] = [value]
    #json_output = json.dumps(json_data,ensure_ascii=False)
    # użycie tego zapisu sprawi że dane JSON będą kodowane jako ciąg znaków a nie jako obiekt JSON.
    # Zamiast używać json.dumps można wykożystać JSONResponse który automatycznie 
    # przekształci dane w odpowiedni obiekt JSON 


    return JSONResponse(content=json_data) 
