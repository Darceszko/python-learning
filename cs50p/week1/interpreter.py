def main():
    x, y, z = input("Expression: ").split()
    print(solution(x,y,z))

def solution(x, y, z):
    if y == "+":
        return float(x) + float(z)
    elif y == "-":
        return float(x) - float(z)
    elif y == "*":
        return float(x) * float(z)
    elif y == "/":
        return float(x) / float(z)

main()
