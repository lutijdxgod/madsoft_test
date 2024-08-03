from pydantic import BaseModel


class MemeUploadResponse(BaseModel):
    image_url: str


class MemeOut(BaseModel):
    id: int
    image_url: str
    description: str | None
