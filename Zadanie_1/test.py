tasks = [10, 5, 4, 'a',"",]

for i in tasks:
    print(type(i))

def checking_data(names, surnemes, tasks):
    for i in tasks:
        if type(i) is int:
            print("OK")
        else:
            print(f' Błędne dane lub brak danych dla studenta {})

checking_data(tasks)
