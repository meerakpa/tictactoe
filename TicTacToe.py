# there are no global variables or constants
# import the helper file to use fxns within
import TicTacToeHelper

# random needed to play computer
import random

# fxn: isValidMove
# input1: list representing the board
# input2: int corresponding to index position that user would like to place letter on
# return/output: boolean value
# side effect: return True or False
# looks at spot to see if taken or not
def printPrettyBoard(boardList):
    # space between text and the board
    print()
    counter = 0
    for i in range(3):
        for j in range(2):
            print(boardList[counter], end=" | ")
            counter += 1
        print(boardList[counter])
        counter += 1
        print("- - - - - ")
        # print()

# fxn: isValidMove
# input1: list representing the board
# input2: int corresponding to index position that user would like to place letter on
# return/output: boolean value
# side effect: return True or False
# looks at spot to see if taken or not
def isValidMove(boardList, spot):
    # checks the int value on the list as an index
    # if it is already taken there will be 'x' or 'o'
    if boardList[spot] == 'x':
        return False
    elif boardList[spot] == 'o':
        return False
    else:
        return True

# fxn: updateBoard
# input1: list representing board
# input2: an int corresponding to the index position the user would like to place letter on
# input3: str representing the user's letter
# return: none
# side effect:
# takes all values to figure out the placement on board
def updateBoard(boardList, spot, playerLetter):
    # replace the string of int with the playerLetter
    boardList[spot] = playerLetter

# fxn: playGame
# input: none
# return: none
# side effect: pints the game out and the final board of game
# where game is played using other fxns
def playGame():
    # initial board of strings from 0-8
    boardList = ["0","1","2","3","4","5","6","7","8"]

    # the counter for the  number of moves (start at 0)
    move_Counter = 0

    # if odd then 'x' turn and even means 'o'
    oddOrEven = 1

    # 1 player or 2 player input?
    computer = int(input("Press 1 to play with a friend or press 2 to play against the computer: "))

    # play with a friend
    if computer == 1:
        # need the game to start and stop at the right time otherwise an infinite loop
        status = "n"
        while status == 'n':
            printPrettyBoard(boardList)

            # % to see if 0 or 1 remainder
            # if 1 then odd so 'x' turn
            if oddOrEven % 2 == 1:
                playerLetter = "x"
                # adds number ensuring the next is even
                oddOrEven += 1
                move_Counter += 1
                spot = int(input("Player x, pick a spot: "))
                taken = isValidMove(boardList,spot)
                if taken == True:
                    updateBoard(boardList,spot,playerLetter)
                else:
                    print("Invalid move, please try again.")
                    spot = int(input("Player x, pick a spot: "))
                    taken = isValidMove(boardList, spot)
                    if taken == True:
                        updateBoard(boardList, spot, playerLetter)

             # even so 'o' turn
            else:
                # adds number ensuring the next is odd
                playerLetter = "o"
                oddOrEven += 1
                move_Counter += 1
                spot = int(input("Player o, pick a spot: "))
                taken = isValidMove(boardList, spot)
                if taken == True:
                    updateBoard(boardList, spot, playerLetter)
                else:
                    print("Invalid move, please try again.")
                    spot = int(input("Player o, pick a spot: "))
                    taken = isValidMove(boardList, spot)
                    if taken == True:
                        updateBoard(boardList, spot, playerLetter)
            status = TicTacToeHelper.checkForWinner(boardList, move_Counter)

        else:
            TicTacToeHelper.printUglyBoard(boardList)
            return status

    # play against the computer
    elif computer == 2:
        playerChoice = input("Would you like to be x or o? ")
        if playerChoice == 'x':
            # need the game to start and stop at the right time otherwise an infinite loop
            status = "n"
            while status == 'n':
                printPrettyBoard(boardList)
                # % to see if 0 or 1 remainder
                # if 1 then odd so 'x' turn
                if oddOrEven % 2 == 1:
                    playerLetter = "x"
                    # adds number ensuring the next is even
                    oddOrEven += 1
                    move_Counter += 1
                    spot = int(input("Player x, pick a spot: "))
                    taken = isValidMove(boardList, spot)
                    if taken == True:
                        updateBoard(boardList, spot, playerLetter)
                    else:
                        print("Invalid move, please try again.")
                        spot = int(input("Player x, pick a spot: "))
                        taken = isValidMove(boardList, spot)
                        if taken == True:
                            updateBoard(boardList, spot, playerLetter)

                # even so 'o' turn
                else:
                    # adds number ensuring the next is odd
                    playerLetter = "o"
                    oddOrEven += 1
                    move_Counter += 1
                    spot = random.randrange(9)
                    taken = isValidMove(boardList, spot)
                    if taken == True:
                        print("\nThe computer played its turn: ")
                        updateBoard(boardList, spot, playerLetter)
                    else:
                        spot = random.randrange(9)
                        taken = isValidMove(boardList, spot)
                        if taken == True:
                            print("\nThe computer played its turn: ")
                            updateBoard(boardList, spot, playerLetter)
                status = TicTacToeHelper.checkForWinner(boardList, move_Counter)

            else:
                TicTacToeHelper.printUglyBoard(boardList)
                return status

        elif playerChoice == 'o':
            status = "n"
            while status == 'n':
                printPrettyBoard(boardList)
                # % to see if 0 or 1 remainder
                # if 1 then odd so 'x' turn
                if oddOrEven % 2 == 1:
                    playerLetter = "x"
                    # adds number ensuring the next is even
                    oddOrEven += 1
                    move_Counter += 1
                    spot = random.randrange(9)
                    taken = isValidMove(boardList, spot)
                    if taken == True:
                        print("\nThe computer played its turn: ")
                        updateBoard(boardList, spot, playerLetter)
                    else:
                        spot = random.randrange(9)
                        taken = isValidMove(boardList, spot)
                        if taken == True:
                            print("\nThe computer played its turn: ")
                            updateBoard(boardList, spot, playerLetter)

                # even so 'o' turn
                else:
                    # adds number ensuring the next is odd
                    playerLetter = "o"
                    oddOrEven += 1
                    move_Counter += 1
                    spot = int(input("Player o, pick a spot: "))
                    taken = isValidMove(boardList, spot)
                    if taken == True:
                        updateBoard(boardList, spot, playerLetter)
                    else:
                        print("Invalid move, please try again.")
                        spot = int(input("Player o, pick a spot: "))
                        taken = isValidMove(boardList, spot)
                        if taken == True:
                            updateBoard(boardList, spot, playerLetter)
                status = TicTacToeHelper.checkForWinner(boardList, move_Counter)

            else:
                TicTacToeHelper.printUglyBoard(boardList)
                return status

    else:
        # to keep error checking while number is not 1 or 2
        while computer != range(1,3):
            print("Invalid choice! Try again.")
            # 1 player or 2 player input?
            computer = int(input("Press 1 to play with a friend or press 2 to play against the computer: "))

            # play with a friend
            if computer == 1:
                # need the game to start and stop at the right time otherwise an infinite loop
                status = "n"
                while status == 'n':
                    printPrettyBoard(boardList)

                    # % to see if 0 or 1 remainder
                    # if 1 then odd so 'x' turn
                    if oddOrEven % 2 == 1:
                        playerLetter = "x"
                        # adds number ensuring the next is even
                        oddOrEven += 1
                        move_Counter += 1
                        spot = int(input("Player x, pick a spot: "))
                        taken = isValidMove(boardList, spot)
                        if taken == True:
                            updateBoard(boardList, spot, playerLetter)
                        else:
                            print("Invalid move, please try again.")
                            spot = int(input("Player x, pick a spot: "))
                            taken = isValidMove(boardList, spot)
                            if taken == True:
                                updateBoard(boardList, spot, playerLetter)

                    # even so 'o' turn
                    else:
                        # adds number ensuring the next is odd
                        playerLetter = "o"
                        oddOrEven += 1
                        move_Counter += 1
                        spot = int(input("Player o, pick a spot: "))
                        taken = isValidMove(boardList, spot)
                        if taken == True:
                            updateBoard(boardList, spot, playerLetter)
                        else:
                            print("Invalid move, please try again.")
                            spot = int(input("Player o, pick a spot: "))
                            taken = isValidMove(boardList, spot)
                            if taken == True:
                                updateBoard(boardList, spot, playerLetter)
                    status = TicTacToeHelper.checkForWinner(boardList, move_Counter)

                else:
                    TicTacToeHelper.printUglyBoard(boardList)
                    return status

            # play against the computer
            elif computer == 2:
                playerChoice = input("Would you like to be x or o? ")
                if playerChoice == 'x':
                    # need the game to start and stop at the right time otherwise an infinite loop
                    status = "n"
                    while status == 'n':
                        printPrettyBoard(boardList)
                        # % to see if 0 or 1 remainder
                        # if 1 then odd so 'x' turn
                        if oddOrEven % 2 == 1:
                            playerLetter = "x"
                            # adds number ensuring the next is even
                            oddOrEven += 1
                            move_Counter += 1
                            spot = int(input("Player x, pick a spot: "))
                            taken = isValidMove(boardList, spot)
                            if taken == True:
                                updateBoard(boardList, spot, playerLetter)
                            else:
                                print("Invalid move, please try again.")
                                spot = int(input("Player x, pick a spot: "))
                                taken = isValidMove(boardList, spot)
                                if taken == True:
                                    updateBoard(boardList, spot, playerLetter)

                        # even so 'o' turn
                        else:
                            # adds number ensuring the next is odd
                            playerLetter = "o"
                            oddOrEven += 1
                            move_Counter += 1
                            spot = random.randrange(9)
                            taken = isValidMove(boardList, spot)
                            if taken == True:
                                print("\nThe computer played its turn: ")
                                updateBoard(boardList, spot, playerLetter)
                            else:
                                spot = random.randrange(9)
                                taken = isValidMove(boardList, spot)
                                if taken == True:
                                    print("\nThe computer played its turn: ")
                                    updateBoard(boardList, spot, playerLetter)
                        status = TicTacToeHelper.checkForWinner(boardList, move_Counter)

                    else:
                        TicTacToeHelper.printUglyBoard(boardList)
                        return status

                elif playerChoice == 'o':
                    status = "n"
                    while status == 'n':
                        printPrettyBoard(boardList)
                        # % to see if 0 or 1 remainder
                        # if 1 then odd so 'x' turn
                        if oddOrEven % 2 == 1:
                            playerLetter = "x"
                            # adds number ensuring the next is even
                            oddOrEven += 1
                            move_Counter += 1
                            spot = random.randrange(9)
                            taken = isValidMove(boardList, spot)
                            if taken == True:
                                print("\nThe computer played its turn: ")
                                updateBoard(boardList, spot, playerLetter)
                            else:
                                spot = random.randrange(9)
                                taken = isValidMove(boardList, spot)
                                if taken == True:
                                    print("\nThe computer played its turn: ")
                                    updateBoard(boardList, spot, playerLetter)

                        # even so 'o' turn
                        else:
                            # adds number ensuring the next is odd
                            playerLetter = "o"
                            oddOrEven += 1
                            move_Counter += 1
                            spot = int(input("Player o, pick a spot: "))
                            taken = isValidMove(boardList, spot)
                            if taken == True:
                                updateBoard(boardList, spot, playerLetter)
                            else:
                                print("Invalid move, please try again.")
                                spot = int(input("Player o, pick a spot: "))
                                taken = isValidMove(boardList, spot)
                                if taken == True:
                                    updateBoard(boardList, spot, playerLetter)
                        status = TicTacToeHelper.checkForWinner(boardList, move_Counter)

                    else:
                        TicTacToeHelper.printUglyBoard(boardList)
                        return status

# fxn: main
# input: none
# return: none
# side effect: prints/plays whole game
# while loop to cont the game until the user wants to stop
def main():
    print("Welcome to Tic Tac Toe!")
    playAgain = True
    while playAgain == True:
        letter = playGame()
        print("Game Over!")
        if letter == 'x':
            print("Player x is the winner!")
        elif letter == 'o':
            print("Player o is the winner!")
        elif letter == 's':
            print("Stalemate reached!")
        else:
            print("error")
        contGame = input("Would you like to play another round? (y/n): ")
        # game shall continue
        if contGame.lower() == 'y':
            playAgain = True
        # game will terminate
        elif contGame.lower() == 'n':
            playAgain = False
        # error checking if something other than variation of y or n is inputted
        else:
            while contGame.lower() != 'y' and contGame.lower() != 'n':
                print("That was an invalid choice.")
                contGame = input("Would you like to play another round? (y/n): ")
                if contGame.lower() == 'y':
                    playAgain = True
                elif contGame.lower() == 'n':
                    playAgain = False
    # outside while loop the user does not want to play
    print("Goodbye!")

main()
