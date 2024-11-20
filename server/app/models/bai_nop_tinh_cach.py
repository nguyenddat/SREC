# models/bai_nop_tinh_cach.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base_class import Base

class BaiNopTinhCach(Base):
    __tablename__ = "bai_nop_tinh_cach"

    id_resume = Column(String(50), ForeignKey("ung_vien.username"), primary_key=True)
    id_cau_hoi = Column(Integer, ForeignKey("test_tinh_cach.id_cau_hoi"), primary_key=True)
    cau_tra_loi = Column(Integer, nullable=True)

    # Relationships
    ung_vien = relationship("UngVien", back_populates="bai_nop_tinh_cach")
    test_tinh_cach = relationship("TestTinhCach", back_populates="bai_nop_tinh_cach")
