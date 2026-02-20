import datetime

from sqlalchemy.schema import CreateTable
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import TIMESTAMP

from sqlalchemy_orm.database import engine

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "products"

    product_id : Mapped[int] = mapped_column(primary_key=True)
    product_name : Mapped[str] = mapped_column(unique=True, index=True)
    sku : Mapped[int] = mapped_column(unique=True)
    price : Mapped[float]
    stock_quantity : Mapped[int]
    created_at = mapped_column(TIMESTAMP, default=datetime.datetime.utcnow)
    
print(CreateTable(Product.__table__))

Base.metadata.create_all(engine)