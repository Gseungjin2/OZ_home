# animals/birds.py

class Eagle:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fly(self):
        return f"{self.name}가 날고 있습니다! 휘익!"

    def info(self):
        return f"이름: {self.name}, 나이: {self.age}살"