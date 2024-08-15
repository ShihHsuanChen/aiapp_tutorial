# API using FastAPI
import os
import shutil
from typing import List
from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel, HttpUrl
from fastapi import File, UploadFile, Form
from tempfile import NamedTemporaryFile


from .model import load_model
from .data import read_image
from .configs import cfg


infer_model = load_model(cfg.infer_model_name_or_path)


def create_app() -> FastAPI:
    from . import __version__

    app = FastAPI(version=__version__)
    app.include_router(get_api_router(), prefix='/api')
    return app


class ResultItemSchema(BaseModel):
    label: str
    prob: float


def get_api_router() -> APIRouter:
    router = APIRouter()

    @router.post(
        '/inference/upload',
        response_model=List[ResultItemSchema],
    )
    def inference_upload(
            file: UploadFile = File(...),
            topk: int = Form(5, ge=1),
            ):
        try:
            # save file to tempfile
            suffix = os.path.splitext(file.filename)[-1]
            with NamedTemporaryFile(delete=True, suffix=suffix) as tmp:
                shutil.copyfileobj(file.file, tmp)
                try:
                    image = read_image(tmp.name)
                except:
                    raise HTTPException(status_code=406, detail='Invalid file format')
                result = infer_model.inference(image, topk=topk)
        finally:
            file.file.close()
        return [ResultItemSchema(label=label, prob=prob) for label, prob in result]

    @router.post(
        '/inference/url',
        response_model=List[ResultItemSchema],
    )
    def inference_url(
            url: HttpUrl = Form(),
            topk: int = Form(5, ge=1),
            ):
        try:
            image = read_image(str(url))
        except:
            raise HTTPException(status_code=406, detail='Given url is not a valid image file')
        result = infer_model.inference(image, topk=topk)
        return [ResultItemSchema(label=label, prob=prob) for label, prob in result]
    return router


app = create_app()
