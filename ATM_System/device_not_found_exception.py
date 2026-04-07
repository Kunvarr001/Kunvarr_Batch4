class DeviceNotFoundException(Exception):
    def __init__(self, message="ATM device not found"):
        super().__init__(message)