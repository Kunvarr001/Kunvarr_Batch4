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
