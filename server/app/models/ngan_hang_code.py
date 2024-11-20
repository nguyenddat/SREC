# models/ngan_hang_code.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from base_class import Base

class NganHangCode(Base):
    __tablename__ = "ngan_hang_code"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    muc_do = Column(Integer, nullable=False)
    ten = Column(String(50), nullable=False)
    mo_ta = Column(Text, nullable=True)
    test_cases_public = Column(Text, nullable=True)
    gioi_han_thoi_gian = Column(String, nullable=True)
    gioi_han_bo_nho = Column(String, nullable=True)
    nguon = Column(String, nullable=True)

    # Relationships
    test_cases = relationship("NganHangTestCases", back_populates="ngan_hang_code")
    test_code = relationship("TestCode", back_populates="ngan_hang_code")
