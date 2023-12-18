class FileHandler:
    @staticmethod
    def open_file(file_path, mode='r'):
        try:
            file = open(file_path, mode)
            return file
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def read_file(file):
        if file:
            return file.read()
        else:
            print("File is not open.")

    @staticmethod
    def write_to_file(file, data):
        if file:
            file.write(data)
        else:
            print("File is not open.")

    @staticmethod
    def close_file(file):
        if file:
            file.close()
        else:
            print("File is not open.")
