# animals/mammals.py

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name}가 짖습니다! 멍멍!"

    def info(self):
        return f"이름: {self.name}, 나이: {self.age}살"