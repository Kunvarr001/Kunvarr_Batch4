class FileDataSource:
    
    def read_lines(self, file_path: str) -> list[str]:
        with open(file_path, "r") as file:
            return file.readlines()