# models/ngan_hang_tinh_cach.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from base_class import Base

class NganHangTinhCach(Base):
    __tablename__ = "ngan_hang_tinh_cach"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    chu_de = Column(String, nullable=False)
    noi_dung_cau_hoi = Column(Text, nullable=False)

    # Relationships
    test_tinh_cach = relationship("TestTinhCach", back_populates="ngan_hang_tinh_cach")
