from Wallet import Wallet
from Customer import Customer
from Paperboy import Paperboy

def main():
    initial_amount = float(input("Enter initial wallet balance: "))
    amount_to_be_paid = float(input("Enter amount to be paid: "))

    customer_first_name = input("Enter customer first name: ")
    customer_last_name = input("Enter customer last name: ")

    wallet = Wallet(initial_amount)
    customer = Customer(customer_first_name, customer_last_name, wallet)
    paperboy = Paperboy()

    print(f"\nWallet Balance: ₹{customer.get_current_balance()}")
    print(f"Paperboy requesting to collect: ₹{amount_to_be_paid}")

    paperboy.collect_payment(customer, amount_to_be_paid)

    print(f"Customer Remaining Balance: ₹{customer.get_current_balance()}")

if __name__ == "__main__":
    main()