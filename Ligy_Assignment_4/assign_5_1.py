class StringProcessor:
    def __init__(self):
        self.input_string = ""

    def get_input(self):
        self.input_string = input("Enter a string: ")

    def print_uppercase(self):
        print("Uppercase:", self.input_string.upper())

# Create an instance of the class
processor = StringProcessor()

# Call the methods
processor.get_input()
processor.print_uppercase()