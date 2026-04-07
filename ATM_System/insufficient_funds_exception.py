class InsufficientFundsException(Exception):
    def __init__(self, message="Insufficient balance in account"):
        super().__init__(message)