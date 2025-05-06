from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from utils.ml_utils import analyze_csv_and_train_model

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "ML Dashboard API is running."}

@app.post("/upload/")
async def upload_csv(file: UploadFile = File(...)):
    contents = await file.read()
    result = analyze_csv_and_train_model(contents)
    return result
