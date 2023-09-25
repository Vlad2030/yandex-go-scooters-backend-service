from sqlalchemy import Column, Integer, String
from core.database import Base


class PhoneCodesDatabase(Base):
    __tablename__ = "phoneCodes"

    id = Column(Integer, primary_key=True, index=True)
    region = Column(String, nullable=False)
    country_code = Column(String, nullable=False)
    number_code = Column(String, nullable=False)
