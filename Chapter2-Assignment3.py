#Assignment 3: Customer Search

class Customer:
    def __init__(self, customer_id, company_name, contact_name, country):
        self.customer_id = customer_id
        self.company_name = company_name
        self.contact_name = contact_name
        self.country = country


class CustomerSearch:
    def __init__(self, customers_list):
        self.customers_list = customers_list

    def search_by_country(self, country_name):
        result_list = []
        for customer in self.customers_list:
            if self._contains_case_insensitive(customer.country, country_name):
                result_list.append(customer)
        return self._sort_by_customer_id(result_list)

    def search_by_company_name(self, company_name):
        result_list = []
        for customer in self.customers_list:
            if self._contains_case_insensitive(customer.company_name, company_name):
                result_list.append(customer)
        return self._sort_by_customer_id(result_list)

    def search_by_contact_name(self, contact_name):
        result_list = []
        for customer in self.customers_list:
            if self._contains_case_insensitive(customer.contact_name, contact_name):
                result_list.append(customer)
        return self._sort_by_customer_id(result_list)

    def export_to_csv(self, customer_list):
        csv_lines = []
        for customer in customer_list:
            csv_line = f"{customer.customer_id},{customer.company_name},{customer.contact_name},{customer.country}"
            csv_lines.append(csv_line)
        return "\n".join(csv_lines)

    def sort_by_customer_id(self, customer_list):
        for outer_index in range(len(customer_list)):
            for inner_index in range(outer_index + 1, len(customer_list)):
                if customer_list[outer_index].customer_id > customer_list[inner_index].customer_id:
                    temp = customer_list[outer_index]
                    customer_list[outer_index] = customer_list[inner_index]
                    customer_list[inner_index] = temp
        return customer_list

    def contains_case_insensitive(self, full_string, search_string):
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


""" 
Mistakes / Issues in the Original C# Code:
    1. SearchByCompanyName and SearchByContact incorrectly search in the Country field instead of the correct property.
    2. No input validation; passing null or empty strings could cause errors.
    3. Poor naming & readability
    4. Single Responsibility Principle (SRP) violation: Searching, sorting, and exporting are all mixed; class does multiple tasks.

Added Two Extra Functions in Python
    1. _sort_by_customer_id : Ensures results are sorted by CustomerID, mimicking C# orderby behavior, without using built-in sort functions.
    2._contains_case_insensitive : Implements case-insensitive substring search manually, since Python in operator is case-sensitive and I avoid using .lower().
"""