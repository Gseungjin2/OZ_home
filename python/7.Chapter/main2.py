# main.py

from animals.mammals import Dog
from animals.birds import Eagle

def main():
    # Dog 객체 생성
    my_dog = Dog("바둑이", 3)
    print(my_dog.info())
    print(my_dog.bark())

    # Eagle 객체 생성
    my_eagle = Eagle("날개", 5)
    print(my_eagle.info())
    print(my_eagle.fly())

if __name__ == "__main__":
    main()