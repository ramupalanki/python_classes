# Product E-Commerce Python Project

## Objective

Create a `Product` class for a small e-commerce application.

Each product contains:
- Product ID
- Name
- Price
- Category
- Stock quantity

## Methods

### `display_product()`
Displays all product information.

### `update_stock(quantity)`
Updates the stock quantity.
- Positive quantity adds stock.
- Negative quantity reduces stock.
- Prevents stock from becoming negative.

### `calculate_total_price(quantity)`
Calculates the total price for the requested quantity and checks stock availability.

### Static method: `is_valid_price(price)`
Returns `True` when the price is greater than zero; otherwise returns `False`.

## Demonstration

The project creates 5 products and demonstrates:
1. Displaying all products.
2. Buying laptops and reducing stock.
3. Buying headphones and reducing stock.
4. Adding keyboard stock.
5. Validating product prices.

## How to Run

Make sure Python 3 is installed.

Run:

```bash
python main.py
```

## Files

- `product.py` - Contains the Product class.
- `main.py` - Creates products and demonstrates buying/updating stock.
