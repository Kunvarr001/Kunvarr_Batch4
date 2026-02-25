from decimal import Decimal

from activity_logger import ActivityLogger
from alert_dispatcher import AlertDispatcher
from transaction_handler import TransactionHandler
from transaction_request import TransactionRequest


def main():
    activity_logger = ActivityLogger()
    alert_dispatcher = AlertDispatcher()
    transaction_handler = TransactionHandler(activity_logger, alert_dispatcher)
    transaction_request = TransactionRequest("CLIENT_789", Decimal("10000"))
    outcome = transaction_handler.handle_transaction(transaction_request)

    print("Transaction is Successful:", outcome.is_successful)
    print("Status Message:", outcome.status_message)
    print("Reference ID:", outcome.reference_id)

if __name__ == "__main__":
    main()