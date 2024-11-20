# models/test_phong_van.py
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from base_class import Base

class TestPhongVan(Base):
    __tablename__ = "test_phong_van"

    id_cong_viec = Column(Integer, ForeignKey("cong_viec.id"), primary_key=True)
    id_cau_hoi = Column(Integer, ForeignKey("ngan_hang_phong_van.id"), primary_key=True)
    cau_tra_loi_mong_muon = Column(String, nullable=True)

    # Relationships
    cong_viec = relationship("CongViec", back_populates="test_phong_van")
    ngan_hang_phong_van = relationship("NganHangPhongVan", back_populates="test_phong_van")
    bai_nop_phong_van = relationship("BaiNopPhongVan", back_populates="test_phong_van")
