# models/ngan_hang_test_cases.py
from sqlalchemy import Column, Integer, ForeignKey, JSON
from sqlalchemy.orm import relationship
from base_class import Base

class NganHangTestCases(Base):
    __tablename__ = "ngan_hang_test_cases"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_cau_hoi = Column(Integer, ForeignKey("ngan_hang_code.id"), nullable=False)
    input = Column(JSON, nullable=False)   # Changed from String to JSON to store lists
    output = Column(JSON, nullable=False)  # Changed from String to JSON to store lists

    # Relationships
    ngan_hang_code = relationship("NganHangCode", back_populates="test_cases")
    bai_nop_test_cases = relationship("BaiNopTestCases", back_populates="ngan_hang_test_cases")
