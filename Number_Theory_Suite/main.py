from consecutive_match import ConsecutiveMatch

class MainRunner:
    def run(self):
        matcher = ConsecutiveMatch()

        test_cases = int(input("Enter number of test cases: "))

        for _ in range(test_cases):
            limit = int(input("Enter value of k: "))
            result = matcher.get_valid_count(limit)
            print(result)


if __name__ == "__main__":
    MainRunner().run()