from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from core.database import Base


class UsersDatabase(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    profile_picture = Column(String, nullable=True)

    first_name = Column(String(length=255), nullable=False)
    last_name = Column(String(length=255), nullable=False)
    age = Column(DateTime, nullable=True)

    username = Column(String(length=64), nullable=True)
    phone_number = Column(String(length=16), nullable=False)
    email = Column(String(length=16), nullable=True)

    role = Column(String, default="buyer", nullable=False)
    rating = Column(Float(precision=4), default=4.00, nullable=False)

    created_at = Column(DateTime, default=datetime.now)
