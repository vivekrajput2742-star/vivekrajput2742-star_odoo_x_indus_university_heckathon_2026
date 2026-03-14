from database import cursor, db

def add_product():

    name = input("Product name: ")
    sku = input("SKU: ")
    category = input("Category: ")
    unit = input("Unit: ")
    reorder = int(input("Reorder level: "))

    cursor.execute(
    "INSERT INTO products(name,sku,category,unit,reorder_level) VALUES(%s,%s,%s,%s,%s)",
    (name,sku,category,unit,reorder)
    )

    db.commit()

    print("Product added")

def search_sku():

    sku = input("Enter SKU: ")

    cursor.execute(
    "SELECT * FROM products WHERE sku=%s",
    (sku,)
    )

    r = cursor.fetchone()

    if r:
        print(r)
    else:
        print("Product not found")