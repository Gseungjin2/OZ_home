class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "Woof!"
    
    def info(self):
        return f"Dog Name: {self.name}, Age: {self.age}"