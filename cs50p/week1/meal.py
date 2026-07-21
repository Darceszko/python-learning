def main():
    time = input("What time is it? ")

    if 7.00 <= convert(time) <= 8.00:
        print("breakfast time")
    elif 12.00 <= convert(time) <= 13.00:
        print("lunch time")
    elif 18.00 <= convert(time) <= 19.00:
        print("dinner time")

def convert(time):

    hour, minutes = time.split(":")
    hour = float(hour)
    minutes = float(minutes)

    return hour + (minutes/60)

if __name__ == "__main__":
    main()
