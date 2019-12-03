from mpi4py import MPI
import sys
import os
from time import sleep

comm = MPI.COMM.WORLD
size = comm.Get_size()
rank = comm.Get_rank()
stat = MPI.Status()


aliveChar = "*"
deadChar = "."

width = int(input("Plane width: "))
height = int(input("Plane height: "))
rotation = int(input("Primary rotation (0=N; 1=E; 2=S; 3=W): "))
slp = float(input("Sleep: "))
x = input("Primary X (if CENTER, leave blank): ")
y = input("Primary Y (if CENTER, leave blank): ")

if x == "":
    x = int(width / 2)
else:
    x = int(x)

if y == "":
    y = int(height / 2)
else:
    y = int(y)

os.system("clear")

plane = [[False for x in range(width)] for y in range(height)]

def printplane():
    for yp in range(0, height):
        for xp in range(0, width):
            if plane[yp][xp]:
                sys.stdout.write(aliveChar)
            else:
                sys.stdout.write(deadChar)
        print()
        
def move(xpos, ypos):
    plane[ypos][xpos] = not plane[ypos][xpos]

    '''if (rotation == 0) or (type(rotation / 4) is int):
        ypos -= 1
    elif (rotation == 1) or (type(rotation / 4) is int):
        xpos += 1
    elif rotation == 2:
        ypos += 1
    else:
        xpos -= 1'''

    if rotation % 4 == 0:
        ypos -= 1
    elif rotation % 4 == 1:
        xpos += 1
    elif rotation % 4 == 2:
        ypos += 1
    else:
        xpos -= 1

    return [xpos, ypos]

inc = 0

while True:
    print("X = " + str(x))
    print("Y = " + str(y))
    print("INC = " + str(inc))
    print()

    m = move(x, y)

    inc += 1

    x = m[0]
    y = m[1]

    if plane[y][x]:
        rotation += 1
    else:
        rotation -= 1

    printplane()

    if slp == 0:
        input()
    else:
        sleep(slp)

    os.system("clear")
