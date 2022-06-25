stage1 = '''






    ___|___   
'''

stage2 = '''
       ┌
       |
       |
       |
       |       
       |               
    ___|___   
'''

stage3 = '''
       ┌--------
       |
       |
       |
       |       
       |               
    ___|___   
'''

stage4 = '''
       ┌--------┐
       |        |
       |
       |
       |       
       |               
    ___|___   
'''

final_hangman = '''
       ┌--------┐
       |        |
       |        O
       |       -┼-
       |       ┌┴┐
       |                SORRY YOU'RE DEAD
    ___|___             
'''

def display_hangman(proba):
    if proba == 1:
        print(stage1)
    elif proba == 2:
        print(stage2)
    elif proba == 3:
        print(stage3)
    elif proba == 4:
        print(stage4)

def display_final_hangman():
    print(final_hangman)

