def main():
    text = input("Input: ")

    remove_vowel(text)

def remove_vowel(text):
    for i in text:
        if i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'i' or i.lower() == 'o' or i.lower() == 'u':
            pass
        else:
            print(i, end="")
    print()

main()
