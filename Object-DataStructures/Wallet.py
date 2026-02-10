class Wallet:
    def __init__(self, initial_amount):
        self.amount = initial_amount

    def get_total_money(self):
        return self.amount

    def set_total_money(self, new_amount):
        self.amount = new_amount

    def subtract_money(self, amount_to_be_debited):
        self.amount -= amount_to_be_debited
