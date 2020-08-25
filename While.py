def nb_year(p0, percent, aug, p):
    # your code
    pi = p0 * (1 + (percent * 0.01)) + aug
    count = 0
    while pi < p:
        pi = pi * (1 + (percent * 0.01)) + aug
        count = count + 1
    return count

print(nb_year(1000, 6, 50, 5000))