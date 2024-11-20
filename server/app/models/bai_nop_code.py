# models/bai_nop_code.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from base_class import Base

class BaiNopCode(Base):
    __tablename__ = "bai_nop_code"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_resume = Column(String(50), ForeignKey("ung_vien.username"), nullable=False)
    id_cau_hoi = Column(Integer, ForeignKey("test_code.id_cau_hoi"), nullable=False)
    ket_qua_chinh_xac = Column(String, nullable=True)
    ket_qua_convention = Column(String, nullable=True)
    trang_thai = Column(Boolean, default=False)

    # Relationships
    ung_vien = relationship("UngVien", back_populates="bai_nop_code")
    test_code = relationship("TestCode", back_populates="bai_nop_code")
    bai_nop_test_cases = relationship("BaiNopTestCases", back_populates="bai_nop_code")
