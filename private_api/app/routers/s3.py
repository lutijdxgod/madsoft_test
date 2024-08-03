from fastapi import APIRouter, Depends, File, Query, status, HTTPException, UploadFile
from sqlalchemy.orm import Session
from ..s3_storage_utils import S3Client
from ..config import settings


router = APIRouter(prefix="/s3", tags=["Memes"])


ALLOWED_IMAGE_TYPES = ["image/jpg", "image/jpeg", "image/png"]
MAX_FILE_SIZE_BYTES = 6291456


@router.post("/")
async def upload_photo(file_name: str, file: UploadFile = File(...)):
    s3_client = S3Client(
        access_key=settings.aws_access_key_id,
        secret_key=settings.aws_secret_access_key,
        endpoint_url=settings.endpoint_s3,
        bucket_name=settings.bucket_name,
    )

    if file.content_type in ALLOWED_IMAGE_TYPES and file.size <= MAX_FILE_SIZE_BYTES:
        await s3_client.upload_file(object=file.file, object_name=file_name)

        profile_image_url = "https://51070322-b300-4509-b403-b1173025eb86.selstorage.ru/" + file_name
    else:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Either file is not an image or file is bigger then 6 Mb.",
        )

    return {"image_url": profile_image_url}


@router.delete("/")
async def delete_photo(file_name=Query(...)):
    s3_client = S3Client(
        access_key=settings.aws_access_key_id,
        secret_key=settings.aws_secret_access_key,
        endpoint_url=settings.endpoint_s3,
        bucket_name=settings.bucket_name,
    )
    await s3_client.delete_file(object_name=file_name)
