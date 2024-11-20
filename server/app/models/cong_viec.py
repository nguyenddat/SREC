# models/cong_viec.py
from sqlalchemy import (
    Column,
    Integer,
    String,
    Enum,
    ForeignKey,
    DateTime
)
from sqlalchemy.orm import relationship
from base_class import Base
import enum

# Enums for various status fields
class TrangThaiEnum(enum.Enum):
    active = "active"
    inactive = "inactive"
    pending = "pending"
    # Add other statuses as needed

class CongViec(Base):
    __tablename__ = "cong_viec"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_nha_tuyen_dung = Column(String(50), ForeignKey("nha_tuyen_dung.username"), nullable=False)
    id_linh_vuc = Column(Integer, ForeignKey("linh_vuc.id"), nullable=False)
    duong_dan_file = Column(String, nullable=True)
    tieu_de = Column(String, nullable=False)
    tuoi_yeu_cau = Column(String, nullable=True)
    kinh_nghiem_yeu_cau = Column(String, nullable=True)
    ky_nang_cung_yeu_cau = Column(String, nullable=True)
    ky_nang_mem_yeu_cau = Column(String, nullable=True)
    hoc_van_yeu_cau = Column(String, nullable=True)
    ngoai_ngu_yeu_cau = Column(String, nullable=True)
    chung_chi_yeu_cau = Column(String, nullable=True)
    tinh_cach_yeu_cau = Column(String, nullable=True)
    ky_nang_cung_uu_tien = Column(String, nullable=True)
    ky_nang_mem_uu_tien = Column(String, nullable=True)
    chung_chi_uu_tien = Column(String, nullable=True)
    muc_luong = Column(String, nullable=True)
    ngay_gio_tao = Column(DateTime, nullable=False)
    ngay_gio_bat_dau = Column(DateTime, nullable=False)
    ngay_gio_ket_thuc = Column(DateTime, nullable=False)
    trang_thai = Column(Enum(TrangThaiEnum), nullable=False)

    # Relationships
    nha_tuyen_dung = relationship("NhaTuyenDung", back_populates="cong_viec")
    linh_vuc = relationship("LinhVuc", back_populates="cong_viec")
    ung_vien = relationship("UngVien", back_populates="cong_viec")
    test_code = relationship("TestCode", back_populates="cong_viec")
    test_phong_van = relationship("TestPhongVan", back_populates="cong_viec")
    test_tinh_cach = relationship("TestTinhCach", back_populates="cong_viec")
