def is_triangle(a, b, c):
    return (c < a + b) and (b < a + c) and (a < b + c)

print(is_triangle(2, 8, 5))