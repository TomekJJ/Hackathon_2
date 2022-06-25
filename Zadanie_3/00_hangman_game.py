from geting_password import upload_file, user_category_choice, draw_pass
from game_elements import print_emtpy_pass, guess_letter, find_letter, show_used_letters, choice_todo, guess_full_pswrd
from display_hangman import display_hangman, display_final_hangman

def game():

    #losowanie hasła z pliku
    pets, rivers, cities = upload_file('passwords.csv')
    choice = user_category_choice()
    pswrd = draw_pass(choice, pets, rivers, cities)
    print(f'hasło to: {pswrd}')

    # przebieg gry
    n = 4
    attempt = 1
    used_letters = []
    ingame_pswrd = print_emtpy_pass(pswrd)

    while attempt <= n:
        print()
        print(f'***** Attempt {attempt} *****')

        choice = choice_todo()
        if choice == "y":
            user_guess = input("Enter the password -->").lower()
            if user_guess == pswrd:
                print("Congratulations! You've guessed the password !!!")
                break
            else:
                print("The password is incorrect")
                display_hangman(attempt)
            attempt += 1

        elif choice == "n":
            letter = guess_letter()
            ingame_pswrd, letter = find_letter(letter, pswrd, ingame_pswrd)
            print()
            print(*list(ingame_pswrd))
            attempt += 1
            used_letters = show_used_letters(used_letters, letter)

            display_hangman(attempt)

        if ingame_pswrd == list(pswrd):
            print()
            print("Brawo. Ogadłeś całe hasło!")
            break

        print(f'Dotychczas użyte litery to:', *used_letters)

        if attempt == n + 1:
            print()
            display_final_hangman()
            print("Przegrałeś, spróbuj jeszcze raz!")
            print(f'Odgadywanym słowem było "{pswrd}"')
            break


def main():
    game()
    again = input("Play again? (y/n)").lower()
    if again == "y":
        print()
        print('**********************************')
        game()
    else:
        print("Thanks for playing!")


if __name__ == '__main__':
    main()

