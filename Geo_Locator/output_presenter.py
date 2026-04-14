class OutputPresenter:
    def render(self, records):
        for rec in records:
            print(f"Address: {rec.address}")
            print(f"Latitude: {rec.latitude}")
            print(f"Longitude: {rec.longitude}")
            print("-" * 40)