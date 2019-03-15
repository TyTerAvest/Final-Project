'''
3/13/19
Ty Ter Avest
Final Project
Huge shoutout to Bob Nystrom because I used his code for reference
When ever I was stuck I just checked what he was doing
'''
# The code below makes the maze random everytime
from random import shuffle, randrange
import time
w = int(input('Put how wide you want the maze to be: '))
h = int(input('Put how tall you want the maze to be: '))
def make_maze(w, h):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]
# the code below allows the user to their typing cursor to move through the maze
    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "+  "
            if yy == y: ver[y][max(x, xx)] = "   "
            walk(xx, yy)
# The code below makes the functions join to create the maze
    walk(randrange(w), randrange(h))
    for (a, b) in zip(hor, ver):
        print(''.join(a + ['\n'] + b))

while 10:
    make_maze(w, h)
    time.sleep(2)
    x = input('Type stop to stop')
    if x == 'stop':
        break
print('Finished')