from typing import List
from fastapi import APIRouter, Depends, File, Form, Response, UploadFile, status, HTTPException
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils
from ..config import settings
import httpx


router = APIRouter(prefix="/memes", tags=["Memes"])


@router.post("/", response_model=schemas.MemeUploadResponse)
def post_meme(file: UploadFile, description: str | None = None, db: Session = Depends(database.get_db)):
    meme_to_upload = models.Meme(**{"image_url": "", "description": description})
    db.add(meme_to_upload)
    db.commit()
    db.refresh(meme_to_upload)

    file_name = meme_to_upload.id

    request = utils.upload_image(file=file, file_name=file_name)
    if request.status_code == 200:
        meme_query = db.query(models.Meme).filter(models.Meme.id == file_name)
        meme_query.update({"image_url": request.json()["image_url"]})
        db.commit()
    else:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=request.json()["detail"])

    return request.json()


@router.get("/{id}", response_model=schemas.MemeOut)
def get_meme_by_id(id: int, db: Session = Depends(database.get_db)):
    meme_query = db.query(models.Meme).filter(models.Meme.id == id)
    meme = meme_query.first()
    if meme is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No meme with ID {id}")

    return meme


@router.put("/{id}", response_model=schemas.MemeOut)
def update_meme_by_id(
    id: int,
    file: UploadFile = File(default=None),
    description: str | None = None,
    db: Session = Depends(database.get_db),
):
    meme_query = db.query(models.Meme).filter(models.Meme.id == id)
    meme = meme_query.first()
    if meme is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No meme with ID {id}")

    if file is not None:
        file_name = meme.id

        request = utils.upload_image(file=file, file_name=file_name)
        if request.status_code == 200:
            meme_query.update({"image_url": request.json()["image_url"]})

        else:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=request.json()["detail"])

    if description is not None:
        meme_query.update({"description": description})
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/", response_model=List[schemas.MemeOut])
def get_memes_paginated(offset: int = 0, limit: int = 5, db: Session = Depends(database.get_db)):
    memes_to_return_query = db.query(models.Meme).order_by(models.Meme.id.desc()).offset(offset).limit(limit)

    return [meme for meme in memes_to_return_query.all()]


@router.delete("/{id}")
def delete_meme(id: int, db: Session = Depends(database.get_db)):
    meme_to_delete_query = db.query(models.Meme).filter(models.Meme.id == id)
    meme_to_delete = meme_to_delete_query.first()
    if meme_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No meme with ID {id}")

    utils.delete_image(file_name=meme_to_delete.image_url.split("/")[-1])

    meme_to_delete_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
