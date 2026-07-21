user_name = input("Felhasznalnev: ").lower().replace(" ", "")

password = input("Jelszo: ")

if user_name == "david": 
    if password == "python123":
        print("Sikeres bejelentkezes! ")
    else:
        print("Hibas jelszo")
else:
    print("Ismeretlen felhasznalo")
