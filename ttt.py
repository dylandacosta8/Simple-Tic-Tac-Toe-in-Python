# TIC TAC TOE Simple
player_mat = ['0','1','2',
              '3','4','5',
              '6','7','8']

gameon = True

def player1(gameon,player_mat):
    wincondition(gameon,player_mat)
    print(player_mat)
    while gameon:
        p1_choice= input("||PLAYER 1||Enter the position you want to replace with X: ")

        if p1_choice.isdigit():
            p1_choice_int= int(p1_choice)
            if p1_choice_int in range(0,9):
                if player_mat[p1_choice_int] != 'O' and player_mat[p1_choice_int] != 'X':
                    player_mat[p1_choice_int] = 'X'
                    print(player_mat)
                    wincondition(gameon,player_mat)
                    leave(gameon)
                    player2(gameon,player_mat)
                else:
                    print("Please select valid Slot!")
                    player1(gameon,player_mat)
            else:
                print("Value out of Range:")
                player1(gameon,player_mat)
        else:
            print("Invalid Input")

def player2(gameon,player_mat):
    wincondition(gameon,player_mat)
    while gameon:
        p2_choice= input("||PLAYER 2||Enter the position you want to replace with O: ")

        if p2_choice.isdigit():
            p2_choice_int= int(p2_choice)
            if p2_choice_int in range(0,9):
                if player_mat[p2_choice_int] != 'O' and player_mat[p2_choice_int] != 'X':
                    player_mat[p2_choice_int] = 'O'
                    print(player_mat)
                    wincondition(gameon,player_mat)
                    leave(gameon)
                    player1(gameon,player_mat)
                else:
                    print("Please select valid Slot!")
                    player2(gameon,player_mat)
            else:
                print("Value out of Range:")
                player2(gameon,player_mat)
        else:
            print("Invalid Input")

            
def leave(gameon):
    if gameon==True:
        status=input("Do you want to continue? Y or N: ")
        if status not in ['Y','N','y','n']:
            print("Invalid Input")
            leave(gameon)
        elif status == 'Y' or status == 'y':
            gameon = True
        else:
            gameon= False

def wincondition(gameon,player_mat):
    if player_mat[0]==player_mat[1]==player_mat[2] or player_mat[3]==player_mat[4]==player_mat[5] or player_mat[6]==player_mat[7]==player_mat[8] or player_mat[0]==player_mat[3]==player_mat[6] or player_mat[1]==player_mat[4]==player_mat[7] or player_mat[2]==player_mat[5]==player_mat[8] or player_mat[0]==player_mat[4]==player_mat[8] or player_mat[2]==player_mat[4]==player_mat[6]:
        print("You have won!")
        exit()
    else:
        gameon=True
    
def main():
    print("Welcome to Tic Tac Toe:")
    player1(gameon,player_mat)

main()