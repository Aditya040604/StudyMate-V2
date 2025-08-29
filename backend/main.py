from fastapi import FastAPI, UploadFile, Form

import shutil
import uuid
import os
import bot_response
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# UPLOAD_DIR = "uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# @app.post("/ask_question/")
# async def ask_question(file: UploadFile, question: str = Form(...)):
#     # Save the uploaded file
#     file_id = str(uuid.uuid4())
#     file_path = os.path.join(UPLOAD_DIR, f"{file_id}_{file.filename}")  
#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)
    
#     # Get the bot response
#     response = bot_response.main(question, file_path)
    
#     return {"response": response}

@app.post("/upload_pdf")
async def upload_pdf(file: UploadFile):
    file_bytes = await file.read()
    with open("temp.pdf", "wb") as f:
        f.write(file_bytes)

    result = bot_response.process_pdf("temp.pdf")
    return result

@app.post("/ask_question")
async def ask_question(question: str = Form(...)):
    return bot_response.ask_question(question)