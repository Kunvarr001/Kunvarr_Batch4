class TransactionOutcome:
    def __init__(self, is_successful, status_message, reference_id):
        self.is_successful = is_successful
        self.status_message = status_message
        self.reference_id = reference_id