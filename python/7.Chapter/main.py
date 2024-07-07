# main.py

import mymath

# 삼각형의 넓이 계산
base = 10
height = 5
triangle_area = mymath.triangle_area(base, height)
print(f"밑변이 {base}이고 높이가 {height}인 삼각형의 넓이는 {triangle_area} 입니다.")

# 원의 넓이 계산
radius = 7
circle_area = mymath.circle_area(radius)
print(f"반지름이 {radius}인 원의 넓이는 {circle_area} 입니다.")

# 직육면체의 표면적 계산
length = 4
width = 3
height = 2
rectangular_prism_area = mymath.rectangular_prism_area(length, width, height)
print(f"길이가 {length}, 너비가 {width}, 높이가 {height}인 직육면체의 표면적은 {rectangular_prism_area} 입니다.")