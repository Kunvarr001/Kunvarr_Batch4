from datetime import datetime

class ProcessingJournal:

    def __init__(self):
        self.entries = []

    def record(self, message: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.entries.append(f"[{timestamp}] {message}")

    def persist(self, file_path: str):
        with open(file_path, "w") as file:
            file.write("\n".join(self.entries))