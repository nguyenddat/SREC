# models/test_code.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base_class import Base

class TestCode(Base):
    __tablename__ = "test_code"

    id_cong_viec = Column(Integer, ForeignKey("cong_viec.id"), primary_key=True)
    id_cau_hoi = Column(Integer, ForeignKey("ngan_hang_code.id"), primary_key=True)

    # Relationships
    cong_viec = relationship("CongViec", back_populates="test_code")
    ngan_hang_code = relationship("NganHangCode", back_populates="test_code")
    bai_nop_code = relationship("BaiNopCode", back_populates="test_code")
