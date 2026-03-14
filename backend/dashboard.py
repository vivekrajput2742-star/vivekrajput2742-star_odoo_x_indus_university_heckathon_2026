from database import cursor

def show_dashboard():

    cursor.execute("SELECT COUNT(*) as total FROM products")
    total = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) as low FROM products WHERE reorder_level<5")
    low = cursor.fetchone()["low"]

    cursor.execute("SELECT COUNT(*) as receipts FROM move_history WHERE operation='RECEIPT'")
    receipts = cursor.fetchone()["receipts"]

    cursor.execute("SELECT COUNT(*) as deliveries FROM move_history WHERE operation='DELIVERY'")
    deliveries = cursor.fetchone()["deliveries"]

    print("\nDashboard")

    print("Total products:",total)
    print("Low stock:",low)
    print("Receipts:",receipts)
    print("Deliveries:",deliveries)