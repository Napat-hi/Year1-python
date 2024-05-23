def fibbonacci(n):
    sequence = []
    a, b = 0, 1
    while n > a:
        sequence.append(a)
        a, b = b, a+b

    return sequence
