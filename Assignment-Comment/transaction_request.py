class TransactionRequest:
    def __init__(self, client_identifier, transaction_amount):
        self.client_identifier = client_identifier
        self.transaction_amount = transaction_amount