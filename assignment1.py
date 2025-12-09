#chapter 1 Assignment 
class Country:
    def __init__(self, country_code, country_name, neighboring_countries):
        self.country_code = country_code
        self.country_name = country_name
        self.neighboring_countries = neighboring_countries

    def display_country_info(self):
        print(f"Country: {self.country_name}")
        if self.neighboring_countries:
            print("Adjacent countries: " + ", ".join(self.neighboring_countries))
        else:
            print("No adjacent countries found.")


class CountryDirectory:
    def __init__(self):
        self.country_map = {
            "IN": Country("IN", "India", ["Pakistan", "China", "Nepal", "Bhutan", "Bangladesh", "Myanmar"]),
            "US": Country("US", "United States", ["Canada", "Mexico"]),
            "NZ": Country("NZ", "New Zealand", []),
            "AU": Country("AU", "Australia", ["Papua New Guinea", "Indonesia"]),
            "CN": Country("CN", "China", ["India", "Pakistan", "Nepal", "Bhutan", "Myanmar", "Laos", "Vietnam",
                                           "Mongolia", "Russia", "North Korea"]),
            "FR": Country("FR", "France", ["Belgium", "Luxembourg", "Germany", "Switzerland", "Italy", "Spain",
                                           "Andorra", "Monaco"])
        }

    def find_country_by_code(self, country_code):
        return self.country_map.get(country_code.upper())


def main():
    directory = CountryDirectory()
    country_code = input("Enter a Country Code (eg- IN, US, NZ): ").strip()
    country = directory.find_country_by_code(country_code)

    if not country:
        print("Invalid country code!")
        return

    country.display_country_info()


if __name__ == "__main__":
    main()
