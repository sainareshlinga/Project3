class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.category}")
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}{item['amount']:>7.2f}\n"
            total += item['amount']
        output = title + items + f"Total: {total:.2f}"
        return output


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    category_names = []
    spent = []
    total_spent = 0

    for category in categories:
        total_spent += category.get_balance()
        category_names.append(category.category)
        spent.append(category.get_balance())

    for i in range(len(spent)):
        spent[i] /= total_spent
        spent[i] *= 100
        spent[i] = spent[i] // 10 * 10

    for i in range(100, -1, -10):
        chart += f"{i:3d}| "
        for amount in spent:
            if amount >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max([len(name) for name in category_names])

    for i in range(max_len):
        chart += "     "
        for name in category_names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        chart += "\n"

    return chart
