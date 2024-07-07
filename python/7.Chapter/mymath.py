# mymath.py

import math

def triangle_area(base, height):
    """삼각형의 넓이를 계산하는 함수"""
    return 0.5 * base * height

def circle_area(radius):
    """원의 넓이를 계산하는 함수"""
    return math.pi * radius ** 2

def rectangular_prism_area(length, width, height):
    """직육면체의 표면적을 계산하는 함수"""
    return 2 * (length * width + width * height + height * length)