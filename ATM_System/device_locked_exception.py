class DeviceLockedException(Exception):
    def __init__(self, message="ATM device is suspended"):
        super().__init__(message)