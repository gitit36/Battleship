#Sangjin Lee
#Purpose: The purpose of this program is to run a Battleship game with the addition of 'water tides' that would affect the location of the ships.


import layout

# Making The Board
Board=[] 
for i in range(layout.rows): 
    InsideBoard=[]
    for j in range(layout.columns): #(=range(10))
        InsideBoard.append(layout.marker.water)
    Board.append(InsideBoard)
#Inside the Board list, I will create another list to fill the content in such as, water, and positions of ships.

# Adding Ships
# for each ship in the list of ships
for ship in layout.ships: 

    if (ship[0][0] == ship[1][0]):
        for i in range(ship[0][1], ship[1][1]+1):
            Board[ship[0][0]][i] = layout.marker.ship

    else:
        for i in range(ship[0][0], ship[1][0]+1):
            Board[i][ship[0][1]] = layout.marker.ship
            
# Guessing
# take inputs from user until ship is sunk
turn = 0
count = 0
while True:
    turn = turn + 1
    target = input('Please enter your guess [row, col] ').split(',')
    row = int(target[0].strip())
    col = int(target[1].strip())
    if Board[row][col] == layout.marker.water:
        Board[row][col] = layout.marker.miss
    elif Board[row][col] == layout.marker.ship:
        Board[row][col] = layout.marker.hit
        count += 1

    # Printing The Board
    topline = (layout.board.corner + layout.board.top)*len(Board[0]) + layout.board.corner
    print(topline)

    # Competition Printing
    if layout.competition == False:
        for row_l in Board:
            print(layout.board.side , end = '')
            for col_l in row_l:
                if col_l == layout.marker.ship:
                    print(' '+ layout.board.side, end = '')
                else:
                    print(col_l + layout.board.side, end = '')
            print()
            print(topline)
    else:
        for row_l in Board:
            print(layout.board.side , end = '')
            for col_l in row_l:
                    print(col_l + layout.board.side, end = '')
            print()
            print(topline)
            
    print('Total Hits: ' + str(count))
    print('Total Misses: ' + str(turn - count))
    print('Guesses: ' + str(turn))

    # Water Current
    tide = layout.current()

    # vertical shift
    l = len(Board)
    b = tide[0]
    if (b<0):
        Board = Board[-b:l] + Board[:-b]  
    elif (b>0):
        Board = Board[l-b:l] + Board[:l-b]

    # horizontal shift
    idx = 0
    a = tide[1]
    for list in Board:
        #list = Board[i]
        l = len(list)
        if (a<0):
            Board[idx] = list[-a:l] + list[:-a]  
        elif (a>0):
            Board[idx] = list[l-a:l] + list[:l-a]
        idx += 1

    # Game Over
    finish = True
    for InsideBoard in Board:
        for element in InsideBoard:            
            if element == layout.marker.ship:
                finish = False
    if finish:
        break
    
score = str((count/turn)*100)
print('Your Final Score is (%): ' + score) 
