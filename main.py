"""
author@mdominguez@gcds.net
1/26/23
program plays game battle ship
bugs:
"""

import random


def print_b(board):
    '''
    :function prints board
    :param board: board array
    :return:
    '''
    print("a b c d e ")
    for row in range(0, 5):  # print each vale in the broad array
        for col in range(0, 5):
            print(board[row][col], end=" ")
        print("")


def board_setup(master_list, player_boat_list):
    '''

    :param master_list: the list of available positions for computer
    :param player_boat_list: the positions of the computer boats
    :return: function adds boats to a list
    '''
    counter = 1
    while counter <= 5:
        dot = random.choice(master_list)  # computer choice is equal to a random number in the master list
        player_boat_list.append(dot)  # add the computer choice to computers list
        master_list.remove(dot)
        counter += 1


def place_mark(board, mark_type, player_missile):
    '''
    function receives the board, the type of mark and the players position
    function places mark on board

    board: is the game board
    mark type: is the charter that will be placed on the board
    player_missile: the coordinate of the board that the user picked

    '''
    if player_missile == "a1":
        board[0][0] = mark_type
    if player_missile == "b1":
        board[0][1] = mark_type
    if player_missile == "c1":
        board[0][2] = mark_type
    if player_missile == "d1":
        board[0][3] = mark_type
    if player_missile == "e1":
        board[0][4] = mark_type
    #####################################################################################
    if player_missile == "a2":
        board[1][0] = mark_type
    if player_missile == "b2":
        board[1][1] = mark_type
    if player_missile == "c2":
        board[1][2] = mark_type
    if player_missile == "d2":
        board[1][3] = mark_type
    if player_missile == "e2":
        board[1][4] = mark_type
    #########################################################
    if player_missile == "a3":
        board[2][0] = mark_type
    if player_missile == "b3":
        board[2][1] = mark_type
    if player_missile == "c3":
        board[2][2] = mark_type
    if player_missile == "d3":
        board[2][3] = mark_type
    if player_missile == "e3":
        board[2][4] = mark_type
    #######################################################
    if player_missile == "a4":
        board[3][0] = mark_type
    if player_missile == "b4":
        board[3][1] = mark_type
    if player_missile == "c4":
        board[3][2] = mark_type
    if player_missile == "d4":
        board[3][3] = mark_type
    if player_missile == "e4":
        board[3][4] = mark_type
    #####################################################################
    if player_missile == "a5":
        board[4][0] = mark_type
    if player_missile == "b5":
        board[4][1] = mark_type
    if player_missile == "c5":
        board[4][2] = mark_type
    if player_missile == "d5":
        board[4][3] = mark_type
    if player_missile == "e5":
        board[4][4] = mark_type
    return board


# user board functions
def us_boat(c_available):
    '''

    :param c_available: computer boats available
    :return: function adds user boats to a list
    '''
    print("welcome please start by placing your positions")
    counter = 0
    boat_list = []  # list of user boats
    while counter < 5:  # amount of times code runs
        print("type a position a-e 1-5")
        user_in = input()
        while user_in not in c_available:  # while the users choice is not in the c_available
            print("invalid answer try again")
            user_in = input("type a position a-e 1-5")
        while user_in in boat_list:  # if the users is in boat list
            print("position taken try again")
            user_in = input("type a position a-e 1-5")
        boat_list.append(user_in)
        counter += 1
    return boat_list


def main():
    com_board = [["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"],  # board
                 ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"]]
    use_board = [["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"],  # board
                 ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"]]
    c_available = ["a1", "b1", "c1", "d1", "e1", "f1", "a2", "b2", "c2", "d2", "e2", "f2", "a3", "b3", "c3",
                   "d3", "e3", "f3", "a4", "b4", "c4", "d4", "e4", "f4", "a5", "b5", "c5", "d5", "e5",
                   "f5"]  # list of available positions on the computer board
    u_available = ["a1", "b1", "c1", "d1", "e1", "f1", "a2", "b2", "c2", "d2", "e2", "f2", "a3", "b3", "c3",
                   "d3", "e3", "f3", "a4", "b4", "c4", "d4", "e4", "f4", "a5", "b5", "c5", "d5", "e5",
                   "f5"]  # list of available position for the computer to guess
    u_boat = us_boat(c_available)  # the boats of the user
    c_win = 0  # c_win is counter of how many ships the computer guesses
    u_win = 0  # u_win is counter of how many ships the computer guesses
    for item in u_boat:
        place_mark(use_board, "⛴", item)  # boats of the user
    computer_boat = []  # boats of the user
    print("==============================================================================================\nYour board")
    print_b(use_board)  # print the users board
    board_setup(c_available, computer_boat)
    print(computer_boat)
    counter = 0
    while counter < 5:  # run loop 5 times
        user_in = input("type a position a-e 1-5")
        while user_in not in ["a1", "b1", "c1", "d1", "e1",  # while the users choice is not position on the board
                              "f1", "a2", "b2", "c2", "d2", "e2", "f2", "a3", "b3", "c3",
                              "d3", "e3", "f3", "a4", "b4", "c4", "d4", "e4", "f4", "a5", "b5", "c5", "d5", "e5", "f5"]:
            user_in = input("type a position a-e 1-5")
        while user_in not in c_available and user_in not in computer_boat:  # while the users choice is not in the computer available positions and it is not in the computer boat list
            user_in = input("your position is taken \n type a position a-e 1-5")

        if user_in in computer_boat:  # if the users position is in the computer boars list
            print(computer_boat)
            computer_boat.remove(user_in)  # remove the boat from the computers list
            place_mark(com_board, "💥", user_in)  # places Hit mark on board
            u_win += 1
        elif user_in not in computer_boat:  # if the users input is not in the boat list
            c_available.remove(user_in)  # remove the position from the available positions
            place_mark(com_board, "💧", user_in)  # place mark on
        print(
            "==============================================================================================\nComputer board")
        print_b(com_board)
        # ============================================================================================
        pos = random.choice(u_available)  # sets position to a random position in u_available
        if pos in u_boat:  # if the position hit a users boat
            place_mark(use_board, "💥", pos)
            u_boat.remove(pos)  # remove the boat from the users boat list
            c_win += 1
        elif pos not in u_boat:  # if the position missed the users boats
            place_mark(use_board, "💧", pos)
            u_available.remove(pos)  # remove the position from U_available
        print(
            "==============================================================================================\nYour board")
        print_b(use_board)
        counter += 1
    if c_win > u_win:  # if the computer hit more boats then the user
        print("computer wins")
    elif u_win > c_win:  # if the user hit more boats then the computer
        print("User win")
    elif u_win == c_win:  # if the the user and computer hit the same amount of boats
        print("Tie")


if __name__ == "__main__":
    main()
