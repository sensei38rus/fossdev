

import math

def circle_area(radius: float) -> float:
    
    if radius < 0:
        raise ValueError("Радиус не может быть отрицательным!")
    return math.pi * radius ** 2

def rectangle_area(length: float, width: float) -> float:
  
    if length < 0 or width < 0:
        raise ValueError("Длина и ширина не могут быть отрицательными!")
    return length * width

def triangle_area(base: float, height: float) -> float:
  
    if base < 0 or height < 0:
        raise ValueError("Основание и высота не могут быть отрицательными!")
    return 0.5 * base * height