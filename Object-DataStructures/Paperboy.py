class Paperboy:
    def collect_payment(self, customer, payment_amount):
        payment_status = customer.pay(payment_amount)

        if payment_status:
            print("Payment is successful")
        else:
            print("Payment processing failed")