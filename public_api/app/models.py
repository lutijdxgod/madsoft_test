from sqlalchemy import (
    TIMESTAMP,
    Column,
    Integer,
    String,
)
from sqlalchemy.sql.expression import text
from .database import Base


class Meme(Base):
    __tablename__ = "memes"

    id = Column(Integer, primary_key=True, nullable=False)
    image_url = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
