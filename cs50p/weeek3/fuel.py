def main():
    fraction = get_fraction("Fraction: ")
    get_percent(fraction)

def get_fraction(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            x = int(x)
            y = int(y)
            if x > y or x < 0:
                continue
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            return x / y


def get_percent(p):
    p *= 100
    p = round(p)
    if p <= 1:
        return print("E")
    elif p >= 99:
        return print("F")
    else:
        return print(f"{int(p)}%")

main()
