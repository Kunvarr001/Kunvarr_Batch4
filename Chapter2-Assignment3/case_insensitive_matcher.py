class CaseInsensitiveMatcher:
    @staticmethod
    def contains(full_string, search_string):
        full_lower = ""
        for char in full_string:
            if 'A' <= char <= 'Z':
                full_lower += chr(ord(char) + 32)
            else:
                full_lower += char

        search_lower = ""
        for char in search_string:
            if 'A' <= char <= 'Z':
                search_lower += chr(ord(char) + 32)
            else:
                search_lower += char

        for outer_index in range(len(full_lower) - len(search_lower) + 1):
            match = True
            for inner_index in range(len(search_lower)):
                if full_lower[outer_index + inner_index] != search_lower[inner_index]:
                    match = False
                    break
            if match:
                return True
        return False
