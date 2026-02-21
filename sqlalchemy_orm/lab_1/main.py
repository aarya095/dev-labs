from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy_orm.database import engine
from sqlalchemy_orm.lab_1.models import Product


# Delete Product
with Session(engine) as session:
    product_to_delete = session.query(Product).filter_by(product_name="Sharpner").one()
    session.delete(product_to_delete)
    session.commit()

# Update Product
"""with Session(engine) as session:
    product_record = session.scalar(select(Product).where(Product.product_name == "CUtter"))
    product_record.product_name = "Cutter"
    session.commit()"""

# View Product
"""with Session(engine) as session:
    result = session.query(Product).all()
    #print(result)
    for row in result:
        print(row.product_name)"""

#Create Product
"""with Session(engine) as session:
    pencil = Product(
        product_name = "Sharpner",
        sku = "127",
        price = 4.0,
        stock_quantity = 30
    )
    eraser = Product(
        product_name = "CUtter",
        sku = "128",
        price = 30.0,
        stock_quantity = 40
    )
    session.add_all([pencil,eraser])
    session.commit()"""

