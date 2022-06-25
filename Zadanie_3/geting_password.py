import random

def upload_file(filename):

    with open(filename) as f:
        content = f.readlines()
        pets = []
        rivers = []
        cities = []

        for i in content:
            row = i.split(';')
            pets.append(row[0])
            rivers.append(row[1])
            cities.append(row[2])

    return pets, rivers, cities

def user_category_choice():
    possible_choices = (1,2,3)

    while True:
        choice = int(input("Choose category (1 - pets, 2 - rivers, 3 - cities: )"))
        if choice in possible_choices:
            return choice
        else:
            print('Wrong choice. Choose category (1 - pets, 2 - rivers, 3 - cities: )')


def draw_pass(choice, pets, rivers, cities):
    if choice == 1:
        pswrd = random.choice(pets)
    if choice == 2:
        pswrd = random.choice(rivers)
    if choice == 3:
        pswrd = random.choice(cities)

    return pswrd
