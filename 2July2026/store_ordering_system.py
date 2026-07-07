products = [
    {"id": 1, "name": "Milk", "price": 75, "stock": 90},
    {"id": 2, "name": "Bread", "price": 35, "stock": 90},
]
orders = []

def show_products():
    for product in products:
        print(f"Product ID: {product['id']}\nName:  {product['name']}\nPrice:  {product['price']}\nStock:  {product['stock']}")

def add_product():
    name=input("Enter product name: ")
    price=input("Enter product price: ")
    stock=input("Enter product stock: ")
    id=3
    new_product={"id": id, "name": name, "price": price, "stock": stock}
    products.append(new_product)
    print("Product added")

def update_stock():
    product_id = int(input("Enter product id: "))
    product_ids = []
    for product in products:
        product_ids.append(product["id"])
    if product_id not in product_ids:
        print("Product id not in list")
    else:
        stock = int(input("Enter product stock: "))
        for product in products:
            if product["id"] == product_id:
                product["stock"] = product["stock"] + stock
                print("Product stock updated")


def create_order():
    product_id = int(input("Enter product id: "))
    quantity = int(input("Enter product quantity: "))
    orders.append({"product_id": product_id, "quantity": quantity})
    for product in products:
        if product["id"] == product_id:
            product["stock"] = product["stock"] - quantity

def sales_report():
    total_revenue = 0
    for order in orders:
        for product in products:
            if order["product_id"] == product["id"]:
                order_price = product["price"] * order["quantity"]
                print(order_price)
                total_revenue = total_revenue + order_price
    print("Total revenue: ", total_revenue)

while True:
    print("Stock Management System and Ordering System")
    print("1. View Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Create Order")
    print("5. View Sales Reports")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        show_products()
    elif choice == 2:
        add_product()
    elif choice == 3:
        update_stock()
    elif choice == 4:
        create_order()
    elif choice == 5:
        sales_report()
    elif choice == 6:
        exit()
    else:
        print("Invalid choice... Please try again")