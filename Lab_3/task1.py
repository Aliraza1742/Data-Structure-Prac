Board = [[None, None, None],
         [None, None, None],
         [None, None, None]]


def print_board(Board):
    for i in Board:
        print(i)


def First_person_input():
    print("**************** PLayer 1 Turn *****************")
    print_board(Board)

    Row_input = int(input("Enter the row number : "))
    if Row_input > 2:
        print("Invalid Input")
        return First_person_input()
    Column_input = int(input("Enter the column number :"))
    if Column_input > 2:
        print("Invalid Input")
        return First_person_input()

    if Board[Row_input][Column_input] == None:
        Board[Row_input][Column_input] = '*'
        print_board(Board)

        Comparison(Board)
        diagnol_Comparison(Board)

        print_board(Board)


    else:
        print("The entered position is Occupied ! ")
        print_board(Board)
        return First_person_input()


def Second_person_input():
    print("**************** PLayer 2 Turn *****************")
    print_board(Board)

    Row_input = int(input("Enter the row number : "))
    if Row_input > 2:
        print("Invalid Input")
        return Second_person_input()
    Column_input = int(input("Enter the column number :"))
    if Column_input > 2:
        print("Invalid Input")
        return Second_person_input()

    if Board[Row_input][Column_input] == None:
        Board[Row_input][Column_input] = '/'

        Comparison(Board)
        diagnol_Comparison(Board)

        print_board(Board)


    else:
        print("The entered position is Occupied ! ")
        print_board(Board)
        return Second_person_input()


def Player_shifter():
    turn_counter = 1
    while turn_counter < 10:
        if turn_counter % 2 != 0:
            First_person_input()

        elif turn_counter % 2 == 0:
            Second_person_input()

        elif turn_counter == 9:
            print()

        turn_counter += 1


def Comparison(Board):
    for i in range(0, 3):
        if Board[i][0] == Board[i][1] == Board[i][2] == '*':
            print("Player 1 wins ! Congratulations ! ")
            exit()

        elif Board[0][i] == Board[1][i] == Board[2][i] == '*':
            print("Player 1 wins ! Congratulations ! ")
            exit()

        elif Board[i][0] == Board[i][1] == Board[i][2] == '/':
            print("Player 2 wins ! Congratulations ! ")
            exit()

        elif Board[0][i] == Board[1][i] == Board[2][i] == '/':
            print("Player 2 wins ! Congratulations ! ")
            exit()


def diagnol_Comparison(Board):
    if Board[0][0] == Board[1][1] == Board[2][2] == '*':
        print("Player 1 wins Diagonally left ! Congratulations ! ")
        exit()

    elif Board[0][2] == Board[1][1] == Board[2][0] == '*':
        print("Player 1 wins Diagonally Right ! Congratulations ! ")
        exit()

    elif Board[0][0] == Board[1][1] == Board[2][2] == '/':
        print(Board)
        print("Player 2 wins Diagonally left ! Congratulations ! ")
        exit()

    elif Board[0][2] == Board[1][1] == Board[2][0] == '/':
        print("Player 2 wins Diagonally Right ! Congratulations ! ")
        exit()


j = Player_shifter()