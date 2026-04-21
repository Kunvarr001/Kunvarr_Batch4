class DivisorCount:
    def get_count(self, number: int) -> int:
        if number <= 0:
            raise ValueError("Number must be positive")

        count = 0
        i = 1

        while i * i <= number:
            if number % i == 0:
                if i == number // i:
                    count += 1
                else:
                    count += 2
            i += 1

        return count