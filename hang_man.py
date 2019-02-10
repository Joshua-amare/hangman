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
    dis = []
    for x in val:
        dis.append("-")
    return dis

#name game_play checks if the user has taken the input supplied
def game_play(x,dis):
    #x is the hang man puzzle and dis is the - display
    temp = []
    i = 0
    print("let the game begin but remeber you have to guess the correct words")
    chx = input(" please write a sigle guess only: ")
    temp[i]= chx
    for t in x:
        if t == chx:
            dis[i] = t
            i += 1
    return dis



x = get_word()
print(x)
ww = randint(0,len(x)-1)
print(display_val(x[ww]))
dis = display_val(x[ww])
game_play(ww,dis)
