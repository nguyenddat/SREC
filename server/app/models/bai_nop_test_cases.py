# models/bai_nop_test_cases.py
from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from base_class import Base

class BaiNopTestCases(Base):
    __tablename__ = "bai_nop_test_cases"

    id_bai_nop_code = Column(Integer, ForeignKey("bai_nop_code.id"), primary_key=True)
    id_test_case = Column(Integer, ForeignKey("ngan_hang_test_cases.id"), primary_key=True)
    trang_thai = Column(Boolean, default=False)

    # Relationships
    bai_nop_code = relationship("BaiNopCode", back_populates="bai_nop_test_cases")
    ngan_hang_test_cases = relationship("NganHangTestCases", back_populates="bai_nop_test_cases")
