# Python Vehicle Rental System

A mini vehicle rental application built using Python Object-Oriented Programming (OOP).

## Concepts Covered

- Classes and Objects
- Inheritance
- Parent and Child Classes
- `super()`
- Instance Attributes
- Instance Methods
- Method Overriding
- Static Methods
- Input Validation
- Exception Handling

## Class Structure

```text
Vehicle
├── Car
└── Bike
```

## Vehicle Class

The parent `Vehicle` class contains:

- Vehicle number
- Brand
- Model
- Rental price per day

It provides:

- `display_vehicle()`
- `calculate_rent(days)`
- `is_valid_rental_duration(days)` - static method

## Car Class

`Car` inherits from `Vehicle` and adds:

- Number of seats

## Bike Class

`Bike` inherits from `Vehicle` and adds:

- Engine capacity

## Rental Calculation

```text
Total Rent = Rental Price Per Day × Number of Days
```

Rental duration must be greater than zero.

## How to Run

Make sure Python 3 is installed.

```bash
python main.py
```

## Example

```text
===== Toyota Innova =====
Vehicle Number   : CAR101
Brand            : Toyota
Model            : Innova
Rental Price/Day : ₹2500
Number of Seats  : 7
Rental Duration  : 3 days
Total Rent       : ₹7500
```
