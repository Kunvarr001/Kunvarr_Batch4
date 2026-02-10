class Customer:
    def __init__(self, first_name, last_name, wallet):
        self.first_name = first_name
        self.last_name = last_name
        self.wallet = wallet

    def pay(self, amount_to_be_paid):
        if self.wallet.get_total_money() >= amount_to_be_paid:
            self.wallet.subtract_money(amount_to_be_paid)
            return True
        return False

    def get_current_balance(self):
        return self.wallet.get_total_money()