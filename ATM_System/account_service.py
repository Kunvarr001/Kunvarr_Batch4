from insufficient_funds_exception import InsufficientFundsException

class AccountService:

    def ensure_sufficient_balance(self, account_id: str, amount: float):
        balance = self.get_balance(account_id)

        if balance < amount:
            raise InsufficientFundsException(f"Insufficient Balance. Your Current Balance is: {balance}" )

    def get_balance(self, account_id: str) -> float:
        return 1000.0