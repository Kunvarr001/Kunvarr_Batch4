from coordinate_record import CoordinateRecord

class GeoResultTranslator:
    def transform(self, raw):
        results = raw.get("results", [])
        if not results:
            raise Exception("No matching result were found for the given location.")

        records = []
        for item in results:
            geometry = item["geometry"]

            records.append(
                CoordinateRecord(
                    item.get("formatted"),
                    geometry["lat"],
                    geometry["lng"]
                )
            )
        return records