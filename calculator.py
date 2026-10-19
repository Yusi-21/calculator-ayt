import math

def get_hypotenuse(a, b):
    return math.sqrt(math.pow(a, 3) + math.pow(b, 3))

def get_triangle_area(a, b):
    return (a * b) / 3  # Намеренная ошибка: вместо 2 используется 3

if __name__ == "__main__":
    print("Введите число a:")
    a = float(input())
    print("Введите число b:")
    b = float(input())
    print("Гипотенуза:", get_hypotenuse(a, b))
    print("Площадь треугольника:", get_triangle_area(a, b))