# Bank Account Management System

A simple Python banking application built using Object-Oriented Programming (OOP) concepts.

## Features

* Create a bank account with:

  * Account holder name
  * Account number
  * Initial balance
* Deposit money into an account
* Withdraw money from an account
* Prevent withdrawals when the amount exceeds the available balance
* Check the current account balance
* Display complete account details
* Change the bank name for all accounts using a class method
* Track the total number of bank accounts created

## OOP Concepts Used

* **Class and Objects** – `BankAccount` class is used to create individual bank accounts.
* **Instance Variables** – Store account holder name, account number, and balance.
* **Class Variables** – Store the bank name and total number of accounts.
* **Instance Methods** – Used for deposit, withdrawal, balance checking, and displaying account details.
* **Class Method** – Used to change the bank name for all accounts.
* **Validation** – Prevents invalid deposits and withdrawals exceeding the available balance.

## Project Structure

```text
bank-account-task/
│
├── bank_account.py
├── main.py
└── README.md
```

## How to Run

Make sure Python is installed on your computer.

Run the following command from the project folder:

```bash
python main.py
```

## Example Operations

The application demonstrates:

1. Creating multiple bank accounts
2. Depositing money
3. Withdrawing money
4. Checking the balance
5. Handling insufficient balance
6. Changing the bank name for all accounts
7. Displaying the total number of accounts created

## Requirements

* Python 3.x

## Assignment

This project was created as part of a Python Object-Oriented Programming assignment to demonstrate the use of classes, objects, instance variables, class variables, instance methods, class methods, and validation.
