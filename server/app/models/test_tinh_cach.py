# models/test_tinh_cach.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base_class import Base

class TestTinhCach(Base):
    __tablename__ = "test_tinh_cach"

    id_cong_viec = Column(Integer, ForeignKey("cong_viec.id"), primary_key=True)
    id_cau_hoi = Column(Integer, ForeignKey("ngan_hang_tinh_cach.id"), primary_key=True)

    # Relationships
    cong_viec = relationship("CongViec", back_populates="test_tinh_cach")
    ngan_hang_tinh_cach = relationship("NganHangTinhCach", back_populates="test_tinh_cach")
    bai_nop_tinh_cach = relationship("BaiNopTinhCach", back_populates="test_tinh_cach")
