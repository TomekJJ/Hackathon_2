import sys

def print_emtpy_pass(pswrd):
    pswrd_len = len(pswrd)
    empty_pswrd = pswrd_len * '_'
    print()
    print(f'**** Password contains {pswrd_len} letters ****')
    print(*list(empty_pswrd))

    return list(empty_pswrd)


def guess_letter():
    while True:
        letter = str(input("Guess letter -->")).lower()
        if not letter.isalpha():
            print("It is not a letter. Try again: ")
        elif len(letter) != 1:
            print("Too many characters. Try again: ")
        else:
            return letter


def find_letter(letter, pswrd, ingame_pswrd):
    pswrd = list(pswrd)

    if letter in pswrd:
        for i, v in enumerate(pswrd):  # i to indeks; v to wartość
            if letter == v:
                ingame_pswrd[i] = letter
        print("Way to go! The given letter is in the password!")
        return ingame_pswrd, letter

    else:
        print("There is no such letter in the password :(")
        return ingame_pswrd, letter


def show_used_letters(used_letters, letter):
    used_letters = list(used_letters)
    used_letters.append(letter)
    used_letters = sorted(used_letters)

    return used_letters


def choice_todo():
    while True:
        choice = str(input("Do you want to guess the whole password (y / n)? -->")).lower()
        if choice == "y" or choice == "n":
            break
        else:
            print("Wrong choice. Try again.")
    return choice


def guess_full_pswrd(pswrd):
    user_guess = input("Enter the password -->").lower()
    if user_guess == pswrd:
        print("Congratulations! You've guessed the password !!!")
        sys.exit()  # Koniec gry - użytkownik odgadł hasło
    else:
        print("The password is incorrect")
    return user_guess
