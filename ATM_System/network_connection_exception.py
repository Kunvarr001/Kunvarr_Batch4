class NetworkConnectionException(Exception):
    def __init__(self, message="Network connection failed"):
        super().__init__(message)