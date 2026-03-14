from auth import signup, login, forgot_password
from inventory import add_product, search_sku
from operations import receive_stock, deliver_stock, transfer_stock
from dashboard import show_dashboard

while True:

    print("\n1 Signup")
    print("2 Login")
    print("3 Forgot password")
    print("4 Exit")

    choice = input("Choose: ")

    if choice == "1":
        signup()

    elif choice == "2":

        if login():

            while True:

                print("\nInventory Menu")

                print("1 Dashboard")
                print("2 Add Product")
                print("3 Receive Stock")
                print("4 Deliver Stock")
                print("5 Transfer Stock")
                print("6 SKU Search")
                print("7 Logout")

                c = input("Select: ")

                if c == "1":
                    show_dashboard()

                elif c == "2":
                    add_product()

                elif c == "3":
                    receive_stock()

                elif c == "4":
                    deliver_stock()

                elif c == "5":
                    transfer_stock()

                elif c == "6":
                    search_sku()

                elif c == "7":
                    break

                else:
                    print("Invalid")

    elif choice == "3":
        forgot_password()

    elif choice == "4":
        break