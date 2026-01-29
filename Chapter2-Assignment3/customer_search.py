from case_insensitive_matcher import CaseInsensitiveMatcher


class CustomerSearch:
    def __init__(self, customers_list):
        self.customers_list = customers_list

    def search_by_country(self, country_name):
        result_list = []
        for customer in self.customers_list:
            if CaseInsensitiveMatcher.contains(customer.country, country_name):
                result_list.append(customer)
        return self.sort_by_customer_id(result_list)

    def search_by_company_name(self, company_name):
        result_list = []
        for customer in self.customers_list:
            if CaseInsensitiveMatcher.contains(customer.company_name, company_name):
                result_list.append(customer)
        return self.sort_by_customer_id(result_list)

    def search_by_contact_name(self, contact_name):
        result_list = []
        for customer in self.customers_list:
            if CaseInsensitiveMatcher.contains(customer.contact_name, contact_name):
                result_list.append(customer)
        return self.sort_by_customer_id(result_list)

    def sort_by_customer_id(self, customer_list):
        for outer_index in range(len(customer_list)):
            for inner_index in range(outer_index + 1, len(customer_list)):
                if customer_list[outer_index].customer_id > customer_list[inner_index].customer_id:
                    temp = customer_list[outer_index]
                    customer_list[outer_index] = customer_list[inner_index]
                    customer_list[inner_index] = temp
        return customer_list



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