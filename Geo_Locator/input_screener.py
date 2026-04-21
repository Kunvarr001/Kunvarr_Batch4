class InputScreener:
    def is_valid(self, value):
        return value is not None and len(value.strip()) > 2