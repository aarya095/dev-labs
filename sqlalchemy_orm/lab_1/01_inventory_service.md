# Lab 01 - Inventory Service

## Objective
Learn model definition, basic CRUD, sessions, and transactions.

## Tasks

1. Define Product model

    ```python
    class Product(Base):
        __tablename__ = "products"

        product_id : Mapped[int] = mapped_column(primary_key=True)
        product_name : Mapped[str] = mapped_column(unique=True, index=True)
        sku : Mapped[int] = mapped_column(unique=True)
        price : Mapped[float]
        stock_quantity : Mapped[int]
        created_at = mapped_column(TIMESTAMP, default=datetime.datetime.utcnow)
    ```

    Output:  
    ![Image](/sqlalchemy_orm/assets/product_table_exists.png)  
    ![Image](/sqlalchemy_orm/assets/product_table_schema.png)

2. Create Product

    ```python
    with Session(engine) as session:
        eraser = Product(
            product_name = "CUtter",
            sku = "128",
            price = 30.0,
            stock_quantity = 40
        )
        session.add_all([pencil,eraser])
        session.commit()  
    ```

    Output:  
    ![Image](/sqlalchemy_orm/assets/view_products.png)

3. Update Product
    ```python
    with Session(engine) as session:
        product_record = session.scalar(select(Product).where(Product.product_name == "CUtter"))
        product_record.product_name = "Cutter"
        session.commit()
    ```

    Output:  
    ![Image](/sqlalchemy_orm/assets/Screenshot%202026-02-21%20104632.png)

3. Delete Product
    ```python
    with Session(engine) as session:
        product_to_delete = session.query(Product).filter_by(product_name="Sharpner").one()
        session.delete(product_to_delete)
        session.commit()
    ```

    Output:  
    ![Image](/sqlalchemy_orm/assets/Screenshot%202026-02-21%20111725.png)

