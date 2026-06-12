class CashRegister:
    def __init__(self, discount=0):
        if not isinstance(discount, int) or not (0 <= discount <= 100):
            print("Not valid discount")
            discount = 0

        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        # correct discount calculation
        discount_amount = (self.discount / 100) * self.total
        self.total = self.total - discount_amount

        # format like test expects (NO decimals)
        formatted_total = int(self.total)

        print(f"After the discount, the total comes to ${formatted_total}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        last = self.previous_transactions.pop()

        self.total -= last["price"] * last["quantity"]

        for _ in range(last["quantity"]):
            self.items.remove(last["item"])