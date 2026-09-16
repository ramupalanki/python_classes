from product import Product


products = [
    Product("P101", "Laptop", 55000, "Electronics", 10),
    Product("P102", "Smartphone", 30000, "Electronics", 15),
    Product("P103", "Headphones", 2500, "Accessories", 25),
    Product("P104", "Backpack", 1800, "Bags", 20),
    Product("P105", "Keyboard", 1500, "Accessories", 30),
]


print("AVAILABLE PRODUCTS")
print("=" * 40)

for product in products:
    product.display_product()


print("\nBUYING PRODUCTS")
print("=" * 40)

# Buy 2 laptops
laptop = products[0]
quantity = 2
total = laptop.calculate_total_price(quantity)
laptop.update_stock(-quantity)

print(f"Bought {quantity} x {laptop.name}")
print(f"Total price: ₹{total:.2f}")
print(f"Remaining stock: {laptop.stock_quantity}")


# Buy 3 headphones
headphones = products[2]
quantity = 3
total = headphones.calculate_total_price(quantity)
headphones.update_stock(-quantity)

print(f"\nBought {quantity} x {headphones.name}")
print(f"Total price: ₹{total:.2f}")
print(f"Remaining stock: {headphones.stock_quantity}")


print("\nADDING NEW STOCK")
print("=" * 40)

# Add 10 keyboards to stock
keyboard = products[4]
keyboard.update_stock(10)

print(f"Added 10 units to {keyboard.name}")
print(f"Updated stock: {keyboard.stock_quantity}")


print("\nVALIDATING PRICES")
print("=" * 40)

print("Price 1000 is valid:", Product.is_valid_price(1000))
print("Price 0 is valid:", Product.is_valid_price(0))
print("Price -500 is valid:", Product.is_valid_price(-500))
