from decimal import Decimal
from datetime import datetime

from transaction_error import TransactionError
from transaction_outcome import TransactionOutcome
from transaction_entry import TransactionEntry


class TransactionHandler:
    MINIMUM_ALLOWED_AMOUNT = Decimal("0.01")
    MAXIMUM_ATTEMPTS = 2

    SUCCESS_MESSAGE = "Transaction completed successfully"
    FAILURE_MESSAGE = "Transaction not completed"

    def __init__(self, activity_logger, alert_dispatcher):
        self.activity_logger = activity_logger
        self.alert_dispatcher = alert_dispatcher
        self.transaction_history = {}

    def handle_transaction(self, transaction_request):
        self.validate_request(transaction_request)
        current_attempt = 0

        while current_attempt < self.MAXIMUM_ATTEMPTS:
            try:
                self.execute_transaction(transaction_request)
                self.store_transaction(transaction_request)
                self.send_success_alert(transaction_request)
                return TransactionOutcome(True, self.SUCCESS_MESSAGE, self.create_reference_id())
            
            except TransactionError:
                current_attempt += 1
                self.activity_logger.log_event(f"Re-attempt number: {current_attempt}")
        return TransactionOutcome(False, self.FAILURE_MESSAGE, None)
    
    def validate_request(self, transaction_request):
        if (transaction_request.client_identifier is None or transaction_request.client_identifier.strip() == ""):
            raise ValueError("Client identifier must be provided")
        if (transaction_request.transaction_amount is None or transaction_request.transaction_amount < self.MINIMUM_ALLOWED_AMOUNT):
            raise ValueError("Transaction amount is invalid")

    def execute_transaction(self, transaction_request):
        self.activity_logger.log_event(f"Processing transaction amount: " f"{transaction_request.transaction_amount}")

        if transaction_request.transaction_amount > Decimal("5000"):
            raise TransactionError("Transaction limit exceeded")

    def store_transaction(self, transaction_request):
        reference_id = self.create_reference_id()
        self.transaction_history[reference_id] = TransactionEntry(transaction_request.client_identifier, transaction_request.transaction_amount, datetime.now())

    def send_success_alert(self, transaction_request):
        alert_message = (f"Your transaction of " f"{transaction_request.transaction_amount} "f"has been processed")
        self.alert_dispatcher.dispatch(transaction_request.client_identifier,alert_message)

    def create_reference_id(self):
        timestamp_value = int(datetime.now().timestamp() * 1000)
        return f"REF-{timestamp_value}"