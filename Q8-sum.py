
def total_sum(x):
    if type(x) != int:
       print("provide an integer value")
    else:
       print("x is a valid integer")
    if x < 0 or x > 9:
        raise ValueError("Input must be a single digit (0–9).")

    total = 0
    pattern = ""
    for _ in range(4):
        pattern += str(x)
        total += int(pattern)

    return total

print(total_sum(3))
