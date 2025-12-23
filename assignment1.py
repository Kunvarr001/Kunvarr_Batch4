class Country:
    def __init__(self, country_code, country_name, neighboring_countries):
        self.country_code = country_code
        self.country_name = country_name
        self.neighboring_countries = neighboring_countries

    def display_country_info(self):
        print("Country:", self.country_name)
        if self.neighboring_countries:
            print("Adjacent countries:", ", ".join(self.neighboring_countries))
        else:
            print("No adjacent countries found.")

class CountryDirectory:
    def __init__(self):
        self.country_map = {
            "IN": Country("IN", "India", ["Pakistan", "China", "Nepal", "Bhutan", "Bangladesh", "Myanmar"]),
            "US": Country("US", "United States", ["Canada", "Mexico"]),
            "NZ": Country("NZ", "New Zealand", []),
            "AU": Country("AU", "Australia", []),
            "CN": Country("CN", "China", ["India", "Pakistan", "Nepal", "Bhutan", "Myanmar", "Laos", "Vietnam",
                                           "Mongolia", "Russia", "North Korea"]),
            "FR": Country("FR", "France", ["Belgium", "Luxembourg", "Germany", "Switzerland", "Italy", "Spain",
                                           "Andorra", "Monaco"])
        }

    def find_country_by_code(self, country_code):
        for key in self.country_map:
            if key == country_code:
                return self.country_map[key]
        return None

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

def main():
    directory = CountryDirectory()
    user_input = input("Enter a Country Code (eg- IN, US, NZ): ")

    country_code = normalize_country_code(user_input)
    country = directory.find_country_by_code(country_code)

    if not country:
        print("Invalid country code!")
        return

    country.display_country_info()

if __name__ == "__main__":
    main()
