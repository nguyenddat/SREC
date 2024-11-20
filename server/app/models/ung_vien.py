# models/ung_vien.py
from sqlalchemy import (
    Column,
    Integer,
    String,
    Enum,
    ForeignKey,
    JSON
)
from sqlalchemy.orm import relationship
from base_class import Base
import enum

class TrangThaiEnum(enum.Enum):
    active = "active"
    inactive = "inactive"
    pending = "pending"

class UngVien(Base):
    __tablename__ = "ung_vien"

    id_resume = Column(Integer, ForeignKey("resume.id"), nullable=False)
    username = Column(String(50), primary_key=True, index=True)
    hashed_pw = Column(String, nullable=False)
    id_cong_viec = Column(Integer, ForeignKey("cong_viec.id"), nullable=False)
    trang_thai = Column(Enum(TrangThaiEnum), nullable=True)
    ket_qua_tinh_cach = Column(JSON, nullable=True)

    # Relationships
    cong_viec = relationship("CongViec", back_populates="ung_vien")
    resume = relationship("Resume", back_populates="ung_vien")
    bai_nop_code = relationship("BaiNopCode", back_populates="ung_vien")
    bai_nop_tinh_cach = relationship("BaiNopTinhCach", back_populates="ung_vien")
    bai_nop_phong_van = relationship("BaiNopPhongVan", back_populates="ung_vien")
