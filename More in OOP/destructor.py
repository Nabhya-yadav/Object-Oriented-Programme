class FileHandler:

    def __init__(self, filename):

            self.file = open(filename, 'w')

            print("file open")

    def write_data(self, data):

        self.file.write(data)

    def __del__(self):

        self.file.close() # Ensure the file is closed for resource cleanup

        print("File is closed")

# Usage

handler = FileHandler("example.txt")

handler.write_data("Hello, world!")

# The destructor is automatically called when the program ends, or

# you can explicitly delete the object:

del handler