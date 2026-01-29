from country_directory import CountryDirectory
from country_utils import CountryUtils

def main():
    directory = CountryDirectory()
    user_input = input("Enter a Country Code (eg- IN, US, NZ): ")

    country_code = CountryUtils.normalize_country_code(user_input)
    country = directory.find_country_by_code(country_code)

    if not country:
        print("Invalid country code!")
        return

    country.display_country_info()

if __name__ == "__main__":
    main()
