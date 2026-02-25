class CustomerCsvWriter:
    @staticmethod
    def to_csv(customer_list):
        csv_lines = []
        for customer in customer_list:
            csv_line = (
                f"{customer.customer_id},"
                f"{customer.company_name},"
                f"{customer.contact_name},"
                f"{customer.country}"
            )
            csv_lines.append(csv_line)
        return "\n".join(csv_lines)
