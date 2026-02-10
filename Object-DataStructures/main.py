from Wallet import Wallet
from Customer import Customer
from Paperboy import Paperboy

def main():
    initial_amount = 5000
    amount_to_be_paid = 600

    customer_first_name = "Aarav"
    customer_last_name = "Sharma"

    wallet = Wallet(initial_amount)
    customer = Customer(customer_first_name, customer_last_name, wallet)
    paperboy = Paperboy()

    print(f"Wallet Balance: ₹{customer.get_current_balance()}")
    print(f"Paperboy requesting to collect: ₹{amount_to_be_paid}")

    paperboy.collect_payment(customer, amount_to_be_paid)

    print(f"Customer Remaining Balance: ₹{customer.get_current_balance()}")

if __name__ == "__main__":
    main()