def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if starts_with_letter(s) and characters(s) and punctuation(s)  and numbers(s)== True:
        return True
    else: 
        return False


def starts_with_letter(s):
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in s[0:2]:
        if i not in number:
           return True
        else:
            return False


def characters(s):
    charx = len(s)
    if charx >= 2 and charx <= 6:
        return True
    else: 
        return False

def punctuation(s):
    punctuation_marks = [".", ",", " ", "?", "!"]
    for i in s:
        if i in punctuation_marks:
            return False
    return True

def numbers(s):
    found_number = False
    for i in s:
        if i.isdigit() and found_number == False :
            found_number = True
            if i == "0":
                return False
        elif i.isalpha() and found_number == True:
            return False
    return True

main()
