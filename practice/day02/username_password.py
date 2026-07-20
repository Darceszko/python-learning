user_name = input("Felhasznalnev: ")

password = input("Jelszo: ")

if user_name.lower() == "david": 
    if password == "python123":
        print("Sikeres bejelentkezes! ")
    else:
        print("Hibas jelszo")
else:
    print("Ismeretlen felhasznalo")
