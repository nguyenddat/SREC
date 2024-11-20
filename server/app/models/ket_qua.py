# models/ket_qua.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base_class import Base

class KetQua(Base):
    __tablename__ = "ket_qua"

    id_resume = Column(Integer, ForeignKey("resume.id"), primary_key=True)
    ket_qua_code = Column(String, nullable=True)
    ket_qua_tinh_cach = Column(String, nullable=True)
    ket_qua_phong_van = Column(String, nullable=True)

    # Relationships
    resume = relationship("Resume", back_populates="ket_qua")
