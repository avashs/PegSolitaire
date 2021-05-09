
totalPeg = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
global allMoves;


## starts the game, loads the board, calculates moves available on the board.
def gameStart():
    global posboard;## board showing the peg position
    posboard = 1;## condition for board to print is used only at the start of game
    global remainingPeg; ## current board
    remainingPeg = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1];
    print("Type ""quit"" to exit the game.");
    print("Type ""res"" to restart the game.");

    printBoard(totalPeg);## prints board with the position of the peg
    hole = input("Pick a hole from postion 1,2,...,15\n"); ## peg to be removed
    while 1:
        ## checks if user wants to exit the game
        if(hole.lower() == "quit"):
                return;
        if(hole.lower() == "res"):
                return "restart";
        ## checking if the input is integer
        try:
            val = int(hole);
            ## checking if the input is position in the board
            if(val < 1 or val > 15):
                hole = input("Try again. Choose position from 1-15 on the board.\n");
            else:
                break;
        except ValueError:
            hole = input("Try again. The input variable is not an integer.\n");
            
    posboard+=1;
    ## imports all moves possible in the board
    findAllMoves();
    i = 0; ## position of the peg
    for peg in totalPeg:
        ## checks if the input hole is equal to current peg
        if peg == int(hole):
            ## changes the board in the postion of the peg
            remainingPeg[i] = 0;
            break;
        i+=1;
    ## prints the current board where 1 represents peg present and 0 represent no peg
    printBoard(remainingPeg);
    ## finds legal moves available and store in list
    list = findLegalMoves();
    ## checks if user wants to restart
    check = makeMove(list,remainingPeg);
    return check;
    

## asks for user to choose the move, updates the board, and continues the game if there are legal moves are available 
def makeMove(alist, blist):
    while alist:
        print(alist); ## prints the current board
        ## asks for the move to be played
        move = input("Pick a peg from and to the location you want to go.(in format ""from,to"" Eg. ""1,3""):\n");
        ## makes sure user gives correct input
        cond = True;
        while cond:

            if(move.lower() == "quit"):
                return;
            elif(move.lower() == "res"):
                return "restart";
            elif not "," in move:
                move = input("Try again. Use ',' to seperate from and to position.Pick a peg from and to the location you want to go.:\n");
                continue;
            else:
                pos = move.split(",");
                if len(pos) != 2:
                    move = input("Try again. Choose position from and to the location you want on the board.\n");
                    continue;
                try:
                    val1 = int(pos[0]);
                    val2 = int(pos[1]);
                    if(val1 < 1 or val1 > 15) or (val2 < 1 or val2 > 15):
                        move = input("Try again. Choose position from 1-15 on the board.\n");
                        continue;
                    else:
                        for a in alist:
                    ## checks if the initial position and destination is available in the legal move list
                            if a[0] == int(pos[0]) and a[2] == int(pos[1]) :
                                updatePeg(a[0],a[1],a[2]); ## update the board
                                cond = False;
                                break;
                        if cond != False:
                            move = input("Try again. The move is not available.\n");
                            continue;
                except ValueError:
                    move = input("Try again. The input variable is not an integer.\n");
                    continue;
                ## checks if there are available moves
                
        printBoard(blist);
        ## checks to see if the game is finished and only one peg remains
        if(sum(blist) == 1):
            print("Congratulation!!! You solved the puzzle.");
            chk = input("Do you want to restart? (Y/N):\n"); ## asks user if they want to restart the game
            if chk.lower() == 'y':
                return "restart";
        alist = findLegalMoves(); ## updates the legal moves left after the board is changed 
    if (sum(blist) != 1):
            print("Sorry!! Better luck next time.");
            chk = input("Do you want to restart? (Y/N):\n");
            if chk.lower() == 'y':
                return "restart";
    

## updates the board so that the initial position of the peg is changed to destination and removes the peg in middle position.
def updatePeg(pos1,pos2,pos3):
    remainingPeg[pos1-1] = 0;
    remainingPeg[pos2-1] = 0;
    remainingPeg[pos3-1] = 1;

## prints the  board
def printBoard(alist):
    print("         "," ",alist[0]);
    print("     ","  ",alist[1],"  ",alist[2]);
    print("    "," ",alist[3],"  ",alist[4], "  ",alist[5]);
    print("  ", " ",alist[6],"  ",alist[7],"  ",alist[8]," ",alist[9]);
    global posboard;
    if(posboard != 1):
        print("  ",alist[10],"  ",alist[11],"  ",alist[12],"  ",alist[13]," ",alist[14]);    ## prints the current board

    else:
        print(" ",alist[10]," ",alist[11]," ",alist[12]," ",alist[13]," ",alist[14]);    ## prints the postional board

       
## finds the legal moves available of current board, checks to see if from the all moves there are moves that are available in the current board          
def findLegalMoves():
    global allMoves;
    global remainingPeg;
    alist = [];
    for moves in allMoves: 
        ## checks if the initial postion, and middle position in the board has a peg and if the destination position is empty
        if (remainingPeg[moves[0]-1] == 1) and (remainingPeg[moves[1]-1] == 1) and (remainingPeg[moves[2]-1] == 0) :
            alist.append(moves);
    return alist;

## initializes all possible moves in the board
def findAllMoves():
    global allMoves;
    allMoves = [[1,2,4],[1,3,6], [2,4,7],[2,5,9],[3,5,8],[3,6,10],[4,7,11],[4,5,6],[4,8,13],[5,8,12],[5,9,14],[6,9,13],[6,10,15],[7,8,9],[8,9,10],[11,12,13],[12,13,14],[13,14,15]];
    alist = [];
    ## finds the reverse moves from the moves.
    for x in allMoves:
        list = [x[2],x[1],x[0]];
        alist.append(list);
    for y in alist:
        allMoves.append(y);
        


## main of the program, starts the game
def main():
    restart = gameStart();
    ## checks if the user wants to restart
    while restart == "restart":
        restart = gameStart();
    
## starts the program
main();