import random
def print_b(board):
    '''
    :function prints board
    :param board: board array
    :return:
    '''
    for row in range(0, 3):                             # print each vaule in the broad array
        for col in range(0, 3):
            print(board[row][col], end=" ")
        print("")
def player_point(player_pos,mark_type,board):
    '''
    :param player_pos: the position of a player int (1-9)
    :param mark_type: X or O weather computer or user
    :param board: board array
    :return: boards with a mark
    '''
    if player_pos == 1:
        board[0][0]=mark_type
    if player_pos == 2:
        board[0][1]=mark_type
    if player_pos == 3:
        board[0][2]=mark_type
    if player_pos == 4:
        board[1][0]=mark_type
    if player_pos == 5:
        board[1][1]=mark_type
    if player_pos == 6:
        board[1][2]=mark_type
    if player_pos == 7:
        board[2][0]=mark_type
    if player_pos == 8:
        board[2][1]=mark_type
    if player_pos == 9:
        board[2][2]=mark_type
    return board
def user_pos(list,player_list):
    '''
    :param list:master list
    :param player_list: player list ether computer list or user list
    :return: return a number 1-9
    '''
    value=False
    while value== False:
        try:
            user_pos=int(input("pick a number 1-9\n"))
            value=True
        except:
            print("invaild aswer try again")

    while user_pos not in list:                     #while the users_pos is not in the master list
        print("Position is taken try again")
        user_pos = int(input())                     #ask again
    if user_pos in list:                            #if the users poition is in the master list
        player_list.append(user_pos)                #add the player position to player list
        list.remove(user_pos)                       # remove the player position from the players list
    return user_pos
def comp_pos(list,player_list):
    computer_choice = random.choice(list)               #computer choice is equal to a random number in the master list
    player_list.append(computer_choice)                 #add the computer choice to computers list
    list.remove(computer_choice)                        # remove the computers choice from the master list
    return computer_choice
def win(player_list):
    if (1 in player_list and 2 in player_list and 3 in player_list ) or (4 in player_list and 5 in player_list  and 6 in player_list) or (7 in player_list and 8 in player_list and 9 in player_list in player_list )or (1 in player_list and 4 in player_list and 7 in player_list )or (2 in player_list and 5 in player_list and 8 in player_list )or (3 in player_list and 6 in player_list and 9 in player_list )or (1 in player_list and 5 in player_list and 9 in player_list) or (3 in player_list and 5 in player_list and 7 in player_list):  #if player list has wining vaules in it
        winner=True# winner = true
        return winner
def main():
    board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]                 # board array
    master_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]                                   #list of available positions
    user_places = []                                                            #list of places user has picked
    comp_places = []                                                            #list of places computer has picked
    while len(master_list) != 0:                                                #while there are still positions in master list
        board=player_point(user_pos(master_list,user_places),"X", board)        #add the users postion by calling on funtion user_pos inside of funtion player point
        if win(user_places) == True:
            print_b(board)                                                      #call on funtion print board
            print("user_wins")
            break
        if len(master_list) !=0:
            board=player_point(comp_pos(master_list, comp_places),"O", board)
        print_b(board)
        if win(comp_places) == True:
            print("computer wins")
            break
    looper_input=input("do you want to play again \nif so type 'yes'\n if not\n type anything to end loop")
    if looper_input== "yes":
        main()
if __name__ == "__main__":
    main()