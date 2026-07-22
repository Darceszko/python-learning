def main():
    amount = 50

    coke(amount)

def coke(amount):
    while(amount > 0):
        print(f"Amount Due: {amount}")
        money = int(input("Insert Coin: "))
        if(money == 5 or money == 10 or money == 25):
            amount = amount - money
    if amount <= 0:
        print(f"Change Owed: {amount * -1}")



main()
