from random import randint


#takes master input froom the game controller
def get_word():
    li = []

    x = input("if you want to continue please type in a word if not write exit or Exit")
    while x != "Exit" :
        print("gotcha")
        li.append(str(input("if you want to continue please type in a word if not write exit or Exit")))
        x = li[len(li) - 1]
    return li[:-1]


#creates the - mark for the words based on their length
def display_val(val):
    for x in val:
        print("-",end='')

#name game_play checks if the user has taken the input supplied
x = get_word()
print(x)
ww = randint(0,len(x)-1)
display_val(x[ww])