pswrd = "dupaaa"
pswrd = list(pswrd)
ingame_pswrd = ['x','x','x','x','x','x']
l = 'a'

for v, i in enumerate(pswrd):  # v to wartość i to indeks
    if l == i:
        ingame_pswrd[v] = l
        print("Podana litera znajduje się w haśle:")
        print(ingame_pswrd)


print('final', ingame_pswrd)