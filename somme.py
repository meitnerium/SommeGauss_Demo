def somme_iterative(n: int) -> int:

    if n < 0:
        raise ValueError("n doit être positif ou nul")

    total = 0
    for i in range(1, n):
        total += i

    return total