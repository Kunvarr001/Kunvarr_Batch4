from country import Country

class CountryDirectory:
    def __init__(self):
        self.country_map = {
            "IN": Country("IN", "India", ["Pakistan", "China", "Nepal", "Bhutan", "Bangladesh", "Myanmar"]),
            "US": Country("US", "United States", ["Canada", "Mexico"]),
            "NZ": Country("NZ", "New Zealand", []),
            "AU": Country("AU", "Australia", []),
            "CN": Country(
                "CN",
                "China",
                ["India", "Pakistan", "Nepal", "Bhutan", "Myanmar", "Laos",
                 "Vietnam", "Mongolia", "Russia", "North Korea"]
            ),
            "FR": Country(
                "FR",
                "France",
                ["Belgium", "Luxembourg", "Germany", "Switzerland",
                 "Italy", "Spain", "Andorra", "Monaco"]
            )
        }

    def find_country_by_code(self, country_code):
        for key in self.country_map:
            if key == country_code:
                return self.country_map[key]
        return None
