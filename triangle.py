def is_triangle(a, b, c):
    if c < a + b and b < a + c and a < b + c:
        return True
    return False

print(is_triangle(2, 3, 5))