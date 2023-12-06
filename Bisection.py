def bisection_method(f, a, b, tol=1e-5):
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None

    a_n = a
    b_n = b
    while (b_n - a_n) / 2 > tol:
        midpoint = (a_n + b_n) / 2
        if f(midpoint) == 0:
            return midpoint
        elif f(a_n) * f(midpoint) < 0:  # The root is in the negative half.
            b_n = midpoint
        else:  # The root is in the positive half.
            a_n = midpoint
    return (a_n + b_n) / 2

if __name__ == "__main__":
  # Example
    def func(x):
        return x**3 - x - 2

    solution = bisection_method(func, 1, 2)
    print("Solution is:", solution)
