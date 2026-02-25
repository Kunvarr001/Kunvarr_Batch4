class AlertDispatcher:
    def dispatch(self, client_identifier, message):
        print(f"Alert sent to {client_identifier}: {message}")