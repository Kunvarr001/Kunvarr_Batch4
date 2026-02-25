#Assignment 2: Find the floor of the expected value(mean) of the subarray from Left to Right.

class SubarrayQueryProcessor:
    def __init__(self, array_elements):
        self.array_elements = array_elements
        self.prefix_sums = self.calculate_prefix_sums(array_elements)

    def calculate_prefix_sums(self, array_elements):
        prefix_sums = [0]
        running_sum = 0
        for element in array_elements:
            running_sum += element
            prefix_sums.append(running_sum)
        return prefix_sums

    def calculate_floor_mean(self, left_index, right_index):
        subarray_sum = self.prefix_sums[right_index] - self.prefix_sums[left_index - 1]
        subarray_length = right_index - left_index + 1
        floor_mean = subarray_sum // subarray_length
        return floor_mean

    def read_positive_integer(self, prompt_message):
        while True:
            user_input = input(prompt_message)
            if user_input == "":
                print("Input cannot be empty.")
                continue

            is_number = True
            for character in user_input:
                if character < '0' or character > '9':
                    is_number = False
                    break

            if is_number:
                numeric_value = 0
                for character in user_input:
                    numeric_value = numeric_value * 10 + (ord(character) - ord('0'))
                if numeric_value > 0:
                    return numeric_value

            print("Invalid input. Please enter a positive integer.")

    def read_array_of_positive_integers(self, prompt_message, expected_length):
        while True:
            user_input = input(prompt_message)
            array_elements = []
            current_number_str = ""

            for character in user_input + " ":
                if '0' <= character <= '9':
                    current_number_str += character
                elif character == ' ':
                    if current_number_str != "":
                        numeric_value = 0
                        for digit_char in current_number_str:
                            numeric_value = numeric_value * 10 + (ord(digit_char) - ord('0'))
                        array_elements.append(numeric_value)
                        current_number_str = ""
                else:
                    current_number_str = ""
                    break

            if len(array_elements) != expected_length:
                print(f"Please enter exactly {expected_length} positive integers separated by spaces.")
                continue

            valid = True
            for number in array_elements:
                if number <= 0:
                    valid = False
                    break

            if valid:
                return array_elements

            print("All numbers must be positive integers.")

    def read_query_indices(self, query_number, number_of_elements):
        while True:
            user_input = input(
                f"Enter query {query_number} (starting index and ending index separated by space): "
            )

            left_index_str = ""
            right_index_str = ""
            reading_left_index = True
            invalid_input_flag = False

            for character in user_input + " ":
                if '0' <= character <= '9':
                    if reading_left_index:
                        left_index_str += character
                    else:
                        right_index_str += character
                elif character == ' ':
                    if reading_left_index and left_index_str != "":
                        reading_left_index = False
                    elif not reading_left_index and right_index_str != "":
                        break
                else:
                    invalid_input_flag = True
                    break

            if invalid_input_flag or left_index_str == "" or right_index_str == "":
                print("Invalid input. Enter exactly two positive integers for indices.")
                continue

            left_index = 0
            for character in left_index_str:
                left_index = left_index * 10 + (ord(character) - ord('0'))

            right_index = 0
            for character in right_index_str:
                right_index = right_index * 10 + (ord(character) - ord('0'))

            if left_index < 1 or right_index > number_of_elements or left_index > right_index:
                print(
                    f"Invalid indices. Please enter values between 1 and {number_of_elements} "
                    f"with left_index <= right_index."
                )
                continue

            return left_index, right_index

def main():
    print("Welcome to the Subarray Floor Mean Calculator Program!")

    processor = SubarrayQueryProcessor([])

    number_of_elements = processor.read_positive_integer(
        "Enter the number of elements in the array: "
    )
    number_of_queries = processor.read_positive_integer(
        "Enter the number of queries you want to perform: "
    )

    array_elements = processor.read_array_of_positive_integers(
        f"Enter {number_of_elements} elements of the array separated by spaces: ",
        number_of_elements
    )

    processor = SubarrayQueryProcessor(array_elements)

    for query_number in range(1, number_of_queries + 1):
        left_index, right_index = processor.read_query_indices(
            query_number, number_of_elements
        )

        floor_mean_result = processor.calculate_floor_mean(
            left_index, right_index
        )
        print(f"The floor of the mean for query {query_number} is: {floor_mean_result}")

main()


"""
Mistakes / Issues in the Original C# Code:
    1. Poor naming: NQ, arr, sumarr, RL are unclear.
    2. No input validation: Assumes correct integers for array size, elements, and queries.
    3. Single responsibility violation: Main does everything—input, computation, output.
    4. Readability & formatting: Confusing indentation and incomplete code lines.
    5. Logical issue: No handling of invalid or out-of-range indices; query parsing is incomplete.
"""