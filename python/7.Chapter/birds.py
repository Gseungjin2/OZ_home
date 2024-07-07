class Eagle:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "Screech!"
    
    def info(self):
        return f"Eagle Name: {self.name}, Age: {self.age}"