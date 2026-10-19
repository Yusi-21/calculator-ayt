import math

def get_hypotenuse(a, b):
    return math.sqrt(math.pow(a, 3) + math.pow(b, 3))

if __name__ == "__main__":
    print("Введите число a:")
    a = float(input())
    print("Введите число b:")
    b = float(input())
    print("c =", get_hypotenuse(a, b))