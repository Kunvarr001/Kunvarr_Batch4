class CountryUtils:
    @staticmethod
    def normalize_country_code(input_text):
        start_index = 0
        end_index = len(input_text) - 1

        while start_index <= end_index and input_text[start_index] == ' ':
            start_index += 1

        while end_index >= start_index and input_text[end_index] == ' ':
            end_index -= 1

        normalized_code = ""
        current_index = start_index

        while current_index <= end_index:
            current_char = input_text[current_index]

            if 'a' <= current_char <= 'z':
                current_char = chr(ord(current_char) - 32)

            normalized_code += current_char
            current_index += 1

        return normalized_code
