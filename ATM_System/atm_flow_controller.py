from device_service import DeviceService
from account_service import AccountService
from cash_dispenser import CashDispenser


class ATMFlowController:

    def __init__(self):
        self.device_service = DeviceService()
        self.account_service = AccountService()
        self.cash_dispenser = CashDispenser()

    def withdraw(self, account_id: str, amount: float):
        handle = self.device_service.get_device_handle()
        self.device_service.ensure_device_available(handle)

        record = self.device_service.retrieve_device_record(handle)
        self.device_service.ensure_device_active(record)
        self.device_service.ensure_network_connected(record)

        self.account_service.ensure_sufficient_balance(account_id, amount)

        self.cash_dispenser.dispense_cash(handle, amount)

        return "SUCCESS"