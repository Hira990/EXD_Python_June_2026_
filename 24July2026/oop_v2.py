class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        print(f"Full name: {self.first_name} {self.last_name}")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.stack} - "

class Developer(Employee):
    def __init__(self, first_name, last_name, stack):
        super().__init__(first_name, last_name)
        self.stack = stack

    def welcome(self):
        return f"Welcome, {self.first_name}, {self.last_name} to the dept of {self.stack}"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.stack}"

# dev = Developer()  # error cz currently dev has not init,
dev = Developer("Iftikhar", "Hussain", "python")
print(dev)
print(dev.welcome())