import os
import json
import glob
from typing import List

from pydantic import BaseModel
from fastapi import FastAPI
from fastapi import UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse


app = FastAPI(title="Backend API")
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RootResponce(BaseModel):
    """responce model of get "/" """

    message: str = "Hello world"


class FilelistResponce(BaseModel):
    """Responce model of get "/filelist" """

    filelist: List[str] = ["sample.txt", "sample.csv"]


@app.get("/", response_model=RootResponce)
async def root() -> json:
    """root operation

    return responce of message only.
    """
    return {"message": "Hello World"}


@app.get("/filelist", response_model=FilelistResponce)
async def fiielist() -> json:
    """filelist operation

    return uploaded files list.
    """
    filelist = [
        os.path.basename(path)
        for path in glob.glob(os.path.join("media", "*"))
        if os.path.isfile(path)
    ]
    return {"filelist": filelist}

@app.get("/download/{filename}", response_class=FileResponse)
async def download(filename: str) -> FileResponse:
    """download operation

    return selected file in media directory.
    """
    path = os.path.join("media", filename)
    response = FileResponse(path, filename=filename)
    return response


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile) -> json:
    """uploadfile operation

    upload client file to media directory of the server.
    """
    os.makedirs("media", exist_ok=True)
    contents = await file.read()
    with open(os.path.join("media", file.filename), mode="wb") as wb:
        wb.write(contents)
    return {"filename": file.filename}
