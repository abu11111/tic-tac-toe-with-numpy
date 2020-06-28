import numpy as np


def board():
    x = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1]).reshape(3, 3)
    return x


# START THE GAME
print(' WELCOME TO TC_TAC_TO')
pl1 = int(input('enter any number'))
pl2 = int(input('enter any number other than pl1'))
if pl1 == pl2:
    print('plese choose different numbers')
    pl2 = int(input('enter any number other than pl1'))
elif pl1 == 0:
    print('plese choose a nonzero number')
    pl1 = int(input('enter any number'))
elif pl2 == 0:
    print('plese choose a nonzero number')
    pl2 = int(input('enter any number other than pl1'))

print(' EXCELLENT LETs START THE GAME')
di = {'a': (0, 0), 'b': (0, 1), 'c': (0, 2), 'd': (1, 0), 'e': (1, 1), 'f': (1, 2), 'g': (2, 0), 'h': (2, 1),
      'i': (2, 2)}
print('HELLO PLAYERS THESE ARE THE POSITIONS PLS SELECT ANY ONE & REMEMBER IF U RE-ENTER A POSITION 1 CHANCE WILL BE DEDUCTED FROM BOTH OF U')
print(di)
brd = board()

def assign():
    global count
    for i in range(4):
        try:
            pos1 = input('player1 select the position')
            pos2 = input('player2 select the position')
            brd[di[pos1][0], di[pos1][1]] = pl1
            brd[di[pos2][0], di[pos2][1]] = pl2
            print(brd)
            del di[pos1]
            del di[pos2]
        except:
            print('wooh player u have already entered the position')

    pos1 = input('player1 select the position')
    brd[di[pos1][0], di[pos1][1]] = pl1


def winner():
    x= np.any([np.sum(brd[0:,0])==3*pl1,np.sum(brd[0:,1])==3*pl1,np.sum(brd[0:,2])==3*pl1,np.sum(brd[0,0:])==3*pl1,np.sum(brd[1,0:])==3*pl1,np.sum(brd[2,0:])==3*pl1,(brd[0,0]+brd[1,1]+brd[2,2])==3*pl1,(brd[2,0]+brd[1,1]+brd[0,2]==3*pl1)])
    y= np.any([np.sum(brd[0:,0])==3*pl2,np.sum(brd[0:,1])==3*pl2,np.sum(brd[0:,2])==3*pl2,np.sum(brd[0,0:])==3*pl2,np.sum(brd[1,0:])==3*pl2,np.sum(brd[2,0:])==3*pl2,(brd[0,0]+brd[1,1]+brd[2,2])==3*pl2,(brd[2,0]+brd[1,1]+brd[0,2])==3*pl2])
    if x:
        print('PLAYER 1 U WON')
    elif y:
        print('PLAYER 2 U WON')
    else:
        print('SORRY PLAYERS IT IS A TIE')


assign()
print('LETS CHECK WHO WON THE MATCH')
winner()
