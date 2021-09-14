import random
from random import choice

'''
The Code simulate  the Game from Movie "21"


'''
def ShowManOpenOneDoor(prize,player):
    Doors = [prize, player]
    OpenDoor = 0
    if prize != player:
        if Doors.count(1) == 0:
            OpenDoor = 1
        elif Doors.count(2) == 0:
            OpenDoor = 2
        elif Doors.count(3) == 0:
            OpenDoor = 3
    else:
        #print(Doors.count(1),Doors.count(2),Doors.count(3))
        if Doors.count(1) == 2:
            list = [2, 3]
            OpenDoor = random.sample(list,1)
            OpenDoor = OpenDoor[0]
        elif Doors.count(2) == 2:
            list = [1,3]
            OpenDoor = random.sample(list,1)
            OpenDoor = OpenDoor[0]
        elif Doors.count(3) == 2:
            list = [1,2]
            OpenDoor = random.sample(list,1)
            OpenDoor = OpenDoor[0]




    return OpenDoor

def CleverGame(prize,player,Open):
    # Player change his mind
    clever_counter = 0;
    DoorList = [player, Open]
    if DoorList.count(1) == 0:
        LastDoor = 1
    elif DoorList.count(2) == 0:
        LastDoor = 2
    elif DoorList.count(3) == 0:
        LastDoor = 3

    player = LastDoor

    if player == prize:
        clever_counter = 1;
        print('Clever Player WIN')
    return clever_counter




def SillyGame(prize,player,Open):
    # Player Do not change his mind
    silly_counter = 0

    if player == prize:
        silly_counter = 1
        print('Silly Player Win')
    else:
        print('Silly Player Lose')
    return silly_counter




def Game():
    GameCounter = 0
    silly_counter = 0
    clever_counter = 0
    while GameCounter < 100000:
        GameCounter += 1
        prize = random.randint(1, 3)
        #print('prize = ', prize)
        player = random.randint(1, 3)
        #print('player = ', player)
        Open = ShowManOpenOneDoor(prize, player)
        #print('Opened Door = ', Open)
        # print('Silly Player Strategy')
        silly = SillyGame(prize, player, Open)
        # print('Clever Player Strategy')
        clever = CleverGame(prize, player, Open)
        if silly == 1:
            silly_counter += 1
        else:
            clever_counter += 1
        print("Silly Wins in ", (silly_counter/GameCounter)*100,"%", "Clever wins in ", (clever_counter/GameCounter)*100, "%" )






def main():
    # test cases
    Game()

if __name__ == "__main__":
    main()