from fastapi import UploadFile
import httpx
from .config import settings


def upload_image(file: UploadFile, file_name: str):
    with httpx.Client() as client:
        request = client.post(
            f"{settings.private_api_url}/s3/",
            files={"file": (file.filename, file.file)},
            params={"file_name": f"{file_name}.{file.content_type.split('/')[-1]}"},
        )
    return request


def delete_image(file_name: str):
    with httpx.Client() as client:
        request = client.delete(
            f"{settings.private_api_url}/s3/",
            params={"file_name": file_name},
        )
    return request
