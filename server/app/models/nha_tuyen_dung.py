# models/nha_tuyen_dung.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base_class import Base

class NhaTuyenDung(Base):
    __tablename__ = "nha_tuyen_dung"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    hashed_pw = Column(String, nullable=False)
    ten = Column(String(50), nullable=False)
    email = Column(String(30), unique=True, index=True, nullable=False)

    # Relationships
    cong_viec = relationship("CongViec", back_populates="nha_tuyen_dung")
