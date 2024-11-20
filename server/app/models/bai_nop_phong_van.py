# models/bai_nop_phong_van.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, JSON
from sqlalchemy.orm import relationship
from base_class import Base

class BaiNopPhongVan(Base):
    __tablename__ = "bai_nop_phong_van"

    id_resume = Column(String(50), ForeignKey("ung_vien.username"), primary_key=True)
    id_cau_hoi = Column(Integer, ForeignKey("test_phong_van.id_cau_hoi"), primary_key=True)
    cau_tra_loi = Column(String, nullable=True)
    diem_matching = Column(Float, nullable=True)
    ket_qua_phong_van = Column(JSON, nullable=True)

    # Relationships
    ung_vien = relationship("UngVien", back_populates="bai_nop_phong_van")
    test_phong_van = relationship("TestPhongVan", back_populates="bai_nop_phong_van")
