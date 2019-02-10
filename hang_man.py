from random import randint

temp = []
var = 6

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
    i = 0
    print("let the game begin but remeber you have to guess the correct words")
    chx = input(" please write a sigle guess only: ")
    temp.append(chx)
    for t in x:
        if t == chx:
            dis[i] = t
            print(i)
        i = i + 1
    print (dis)
    if chx not in x:
        global var
        var -= 1
        print("ops!!! you have", var,"chances left")
    if "-" in dis and var != 0:
        game_play(x, dis)


    return dis

#y is collecting the randmized word
y = get_word()
print(y)
#a random value is being selected based on the range of the word provided
ww = randint(0,len(y)-1)
x = y[ww]
print(x)
# a display is being generated
print(display_val(y[ww]))
dis = display_val(y[ww])
# the game has been initialized
print(game_play(x,dis))
