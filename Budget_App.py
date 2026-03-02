class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append(
            {'amount': amount, 'description': description})  # adding amount and description to the ledger

    def withdraw(self, amount, description=''):
        if not self.check_funds(
                amount):  # uses check_funds() method to see if there's enough money in your account for withdrawal
            return False
        self.ledger.append({'amount': -amount,
                            'description': description})
        return True

    def get_balance(self):
        total = 0  # start balance at 0

        for items in self.ledger:
            total += items['amount']
        return total

    def transfer(self, amount, category):
        if not self.check_funds(amount):  # uses check_funds() method to see if you have enough money in your account.
            return False
        self.withdraw(amount,
                      f'Transfer to {category.name}')
        category.deposit(amount,
                         f'Transfer from {self.name}')
        return True

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30,
                                 '*') + '\n'
        items = ''

        #
        for item in self.ledger:
            description = item['description'][:23].ljust(
                23)
            amount = f'{item["amount"]:.2f}'.rjust(
                7)
            items += description + amount + '\n'

        total = f'Total: {self.get_balance():.2f}'
        return title + items + total


def create_spend_chart(categories):
    spending = []
    total_spent = 0

    for category in categories:
        spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                spent += -item['amount']
        spending.append(spent)  # adding the specific value spent to the spending list
        total_spent += spent  # adding number spent to the rest of the amount spent aka total_spent

    percentages = []
    for spent in spending:
        percent = int(round((
                                        spent / total_spent) * 100 // 10 * 10))
        percentages.append(percent)  # add percent calculated to the percentages list

    chart = 'Percentage spent by category\n'

    for level in range(100, -1,
                       -10):
        chart += str(level).rjust(
            3) + '| '  # Turns level value into a string, so it can properly concatenate to chart
        for percent in percentages:
            chart += 'o  ' if percent >= level else "   "  # adds an 'o'
        chart += '\n'  # newline

    chart += '    ' + '-' * (
                len(categories) * 3 + 1) + '\n'  # Adds a new lign and appends it to chart

    max_length = max(len(category.name) for category in
                     categories)  # used for text alignment

    for i in range(max_length):  # Use max_length or longest word from the categories for the range
        chart += '     '  # Adds 5 spaces so start of each row aligns under the chart bar

        # Use this to create category names and write the vertically under the chart.
        for j, category in enumerate(categories):  # create an index number for each category
            # if length is less than index, it will append the value that's in the index for category.name to chart
            if i < len(category.name):
                chart += category.name[i]
            else:
                chart += ' '  # adds space if index is greater than length of category.name
            chart += '  '
        chart += '\n'

    return chart.rstrip('\n')  # removes the next newline on the right


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
