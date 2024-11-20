# models/resume.py
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey
)
from sqlalchemy.orm import relationship
from base_class import Base

class Resume(Base):
    __tablename__ = "resume"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_cong_viec = Column(Integer, ForeignKey("cong_viec.id"), nullable=False)
    ten = Column(String(50), nullable=False)
    tuoi = Column(String(30), nullable=True)
    gmail = Column(String, nullable=True)
    ky_nang = Column(String, nullable=True)
    hoc_van = Column(String, nullable=True)
    chuyen_nganh = Column(String, nullable=True)
    ngoai_ngu = Column(String, nullable=True)
    chung_chi = Column(String, nullable=True)
    kinh_nghiem = Column(String, nullable=True)
    tinh_cach = Column(String, nullable=True)
    duong_dan_file = Column(String, nullable=True)
    diem_matching = Column(Float, nullable=True)

    # Relationships
    cong_viec = relationship("CongViec")
    ung_vien = relationship("UngVien", back_populates="resume")
    ket_qua = relationship("KetQua", back_populates="resume")
