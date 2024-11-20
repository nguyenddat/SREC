# models/linh_vuc.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base_class import Base

class LinhVuc(Base):
    __tablename__ = "linh_vuc"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ten = Column(String, nullable=False)

    # Relationships
    cong_viec = relationship("CongViec", back_populates="linh_vuc")
