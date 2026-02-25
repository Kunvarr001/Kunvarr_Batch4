from customer import Customer
from customer_search import CustomerSearch
from customer_csv_writer import CustomerCsvWriter

def main():
    customers = [
        Customer(3, "Gamma Inc", "Charlie", "USA"),
        Customer(1, "Acme Corp", "Alice", "USA"),
        Customer(2, "Beta LLC", "Bob", "Canada"),
    ]

    search = CustomerSearch(customers)

    usa_customers = search.search_by_country("USA")

    csv_output = CustomerCsvWriter.to_csv(usa_customers)
    print(csv_output)


if __name__ == "__main__":
    main()
