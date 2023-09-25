from sqlalchemy import Column, Integer, String, ARRAY
from core.database import Base


class UserRolesDatabase(Base):
    __tablename__ = "userRoles"

    id = Column(Integer, primary_key=True, index=True)
    roles = Column(ARRAY(String))
