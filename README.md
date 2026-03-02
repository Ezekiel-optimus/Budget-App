# Budget App


A simple Python application to help you manage your finances by tracking deposits, withdrawals, and transfers across different categories, as well as visualizing spending with a percentage chart.

This project fulfills the requirements for a lab that builds a Category class with a ledger and a spending chart.

## Installation

Install my-project with npm

```bash
git clone https://github.com/Ezekiel-optimus/Budget-App.git
cd Budget-App
```

## Features

- Create budget categories (e.g., Food, Clothing, Entertainment).
- Deposit money into a category with an optional description.
- Withdraw money with automatic balance checking.
- Transfer money between categories.
- Display category ledger in a neatly formatted string.
- Generate a vertical bar chart showing the percentage of spending per category.


## Usage/Examples

```Python
# Create categories
food = Category('Food')
clothing = Category('Clothing')
entertainment = Category('Entertainment')

# Add transactions
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing.deposit(500, 'initial deposit')
food.transfer(50, clothing)

# Print ledger
print(food)
print(clothing)

# Generate and print spending chart
print(create_spend_chart([food, clothing, entertainment]))

```
