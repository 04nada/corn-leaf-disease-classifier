from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

import requests
import tempfile

import cnn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "こんにちは、せかい！"}

@app.post("/svm-classify")
async def svm_classify(file: UploadFile = File(...)):
    contents = await file.read()

    result = "Blight"
    return JSONResponse(content={"result": result})

@app.post("/cnn-classify")
async def cnn_classify(file: UploadFile = File(...)):
    contents = await file.read()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpeg") as tmp:
        tmp.write(contents)
        tmp_path = tmp.name

    result = cnn.predict_image(tmp_path)

    return JSONResponse(content={"result": result})