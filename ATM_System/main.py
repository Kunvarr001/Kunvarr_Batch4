from atm_flow_controller import ATMFlowController
from device_locked_exception import DeviceLockedException
from insufficient_funds_exception import InsufficientFundsException
from network_connection_exception import NetworkConnectionException
from device_not_found_exception import DeviceNotFoundException


def main():
    controller = ATMFlowController()

    account_id = input("Enter Account ID: ")

    try:
        amount = float(input("Enter amount to withdraw: "))

        result = controller.withdraw(account_id, amount)
        print(f"{result}")

    except ValueError:
        print("Invalid input! Please enter a valid number for amount.")

    except DeviceLockedException as e:
        print(f"Device Error: {e}")

    except NetworkConnectionException as e:
        print(f"Network Error: {e}")

    except InsufficientFundsException as e:
        print(f"Balance Error: {e}")

    except DeviceNotFoundException as e:
        print(f"Device Not Found: {e}")

    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()