grade = int(input("Adja meg a pontszamat: \n"))

if grade >= 90:
    print("Jeles")
elif grade >= 75:
    print("Jo")
elif grade >= 60:
    print("Kozepes")
elif grade >= 50:
    print("Elegseges")
elif grade < 50:
    print("Elegtelen")
