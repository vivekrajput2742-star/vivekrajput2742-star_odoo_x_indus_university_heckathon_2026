from database import cursor, db

def receive_stock():

    sku = input("SKU: ")
    warehouse = input("Warehouse: ")
    qty = int(input("Quantity: "))

    cursor.execute(
    "INSERT INTO stock(sku,warehouse,quantity) VALUES(%s,%s,%s)",
    (sku,warehouse,qty)
    )

    cursor.execute(
    "INSERT INTO move_history(sku,operation,quantity,warehouse,status) VALUES(%s,'RECEIPT',%s,%s,'DONE')",
    (sku,qty,warehouse)
    )

    db.commit()

    print("Stock received")

def deliver_stock():

    sku = input("SKU: ")
    warehouse = input("Warehouse: ")
    qty = int(input("Quantity: "))

    cursor.execute(
    "UPDATE stock SET quantity=quantity-%s WHERE sku=%s AND warehouse=%s",
    (qty,sku,warehouse)
    )

    cursor.execute(
    "INSERT INTO move_history(sku,operation,quantity,warehouse,status) VALUES(%s,'DELIVERY',%s,%s,'DONE')",
    (sku,qty,warehouse)
    )

    db.commit()

    print("Delivery completed")

def transfer_stock():

    sku = input("SKU: ")
    source = input("From warehouse: ")
    dest = input("To warehouse: ")
    qty = int(input("Quantity: "))

    cursor.execute(
    "UPDATE stock SET quantity=quantity-%s WHERE sku=%s AND warehouse=%s",
    (qty,sku,source)
    )

    cursor.execute(
    "INSERT INTO stock(sku,warehouse,quantity) VALUES(%s,%s,%s)",
    (sku,dest,qty)
    )

    cursor.execute(
    "INSERT INTO move_history(sku,operation,quantity,warehouse,status) VALUES(%s,'TRANSFER',%s,%s,'DONE')",
    (sku,qty,source)
    )

    db.commit()

    print("Transfer done")