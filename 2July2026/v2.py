products = [
    {'id': 1, 'name': 'Milk', 'price': 75, 'stock': 90},
    {'id': 2, 'name': 'Bread', 'price': 35, 'stock': 90}
]
orders = [
    {"product_id": 1, "quantity": 3},
    {"product_id": 2, "quantity": 2}
]

total_revenue = 0
for order in orders:
    for product in products:
        if order["product_id"] == product["id"]:
            order_price = product["price"] * order["quantity"]
            print(order_price)
            total_revenue = total_revenue + order_price

print(total_revenue)