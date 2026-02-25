class TransactionEntry:
    def __init__(self,client_identifier,transaction_amount,processed_at):
        self.client_identifier = client_identifier
        self.transaction_amount = transaction_amount
        self.processed_at = processed_at