class Product:
    def __init__(self, product_id, name, price, category, stock_quantity):
        if not Product.is_valid_price(price):
            raise ValueError("Price must be greater than zero.")

        if stock_quantity < 0:
            raise ValueError("Stock quantity cannot be negative.")

        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.stock_quantity = stock_quantity

    def display_product(self):
        print(f"Product ID     : {self.product_id}")
        print(f"Name           : {self.name}")
        print(f"Price          : ₹{self.price:.2f}")
        print(f"Category       : {self.category}")
        print(f"Stock Quantity : {self.stock_quantity}")
        print("-" * 40)

    def update_stock(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError("Stock quantity must be an integer.")

        if self.stock_quantity + quantity < 0:
            raise ValueError("Insufficient stock.")

        self.stock_quantity += quantity

    def calculate_total_price(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        if quantity > self.stock_quantity:
            raise ValueError("Insufficient stock.")

        return self.price * quantity

    @staticmethod
    def is_valid_price(price):
        return price > 0
