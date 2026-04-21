from divisor_count import DivisorCount

class ConsecutiveMatch:
    def __init__(self):
        self.divisor = DivisorCount()

    def get_valid_count(self, limit: int) -> int:
        if limit <= 2:
            return 0
        
        total = 0

        for n in range(2, limit):
            if self.is_match(n):
                total += 1

        return total


    def is_match(self, number: int) -> bool:
        current = self.divisor.get_count(number)
        next_value = self.divisor.get_count(number + 1)

        return current == next_value