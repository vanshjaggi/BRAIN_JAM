#TIC TAC TOE
#SWOYAM SAHOO
#PROJECT BRAIN JAM (2k20-2k21)


#importing modules
import os
import csv
import time
import random

#DEFINING GAME
tic={"1":" ","2":" ","3":" ",
     "4":" ","5":" ","6":" ",
     "7":" ","8":" ","9":" "}
keys=[]
for key in tic:
    keys.append(key)

def main(board):
    print('          ',board["1"]+" | "+board["2"]+" | "+board["3"])
    print('          ',"- + - + -")
    print('          ',board["4"]+" | "+board["5"]+" | "+board["6"])
    print('          ',"- + - + -")
    print('          ',board["7"]+" | "+board["8"]+" | "+board["9"])
def game(PLAY_1,PLAY_2):
    x="X"
    TURN=PLAY_1
    o=0
    for i in range(9):
        main(tic)
        print("TURN : ",TURN[0],'\nSYMBOL : ',TURN[1])
        while 1:
            try:
                pos=int(input("Make your move : "))
            except ValueError:
                print("Refer to the game grid given below to play the game !")
                print("          - - - - - - - - - - - - ")
                print("                1 | 2 | 3")
                print("                - + - + -")
                print("                4 | 5 | 6")
                print("                - + - + -")
                print("                7 | 8 | 9")
                print("          - - - - - - - - - - - -  \n")
            else:
                break
        if(pos>9):
            print("No such place exists.")
            continue
        if(tic[str(pos)]==" "):
            tic[str(pos)]=x
            o=o+1
            k=os.system('cls')
            print()
            print(""".___________.__    ______    .___________.    ___       ______    .___________. ______    _______ 
|           |  |  /      |   |           |   /   \     /      |   |           |/  __  \  |   ____|
`---|  |----|  | |  ,----'   `---|  |----`  /  ^  \   |  ,----'   `---|  |----|  |  |  | |  |__   
    |  |    |  | |  |            |  |      /  /_\  \  |  |            |  |    |  |  |  | |   __|  
    |  |    |  | |  `----.       |  |     /  _____  \ |  `----.       |  |    |  `--'  | |  |____ 
    |__|    |__|  \______|       |__|    /__/     \__\ \______|       |__|     \______/  |_______|
                                                                                                  """)
            print()
        else:
            print("the place is already filled.")
            print()
            continue
        if(o>=5):
            if(tic["1"]==tic["4"]==tic["7"]==x or tic["2"]==tic["5"]==tic["8"]==x or tic["3"]==tic["6"]==tic["9"]==x or tic["1"]==tic["5"]==tic["9"]==x or tic["3"]==tic["5"]==tic["7"]==x or tic["1"]==tic["2"]==tic["3"]==x or tic["4"]==tic["5"]==tic["6"]==x or tic["7"]==tic["8"]==tic["9"]==x):
                global WINNERR
                global WINNER
                main(tic)
                print()
                print("* * G a M e   O v E r * *")
                print()
                WINNERR=True
                WINNER=TURN[0]
                print(TURN[0],'(',TURN[1],') '," WON!!")
                break
        if(o==9):
            global gamedraw
            global GAME_DRAW
            gamedraw=True
            main(tic)
            print()
            GAME_DRAW="DRAW GAME"
            print("* * G a M e   D r A w * *")

        if(x=="X"):
            TURN=PLAY_2
            x="O"
        else:
            TURN=PLAY_1
            x="X"



#REFRSHING/WRITING THE CSV FILE
if((os.path.isfile('TICTACTOE_RECORDS.csv')) is True):
    D1=open('TICTACTOE_RECORDS.csv','a+')
    D1.close
    FileExist=True
else:
    D1=open('TICTACTOE_RECORDS.csv','w+')
    colheadings=['GAME CODE','PLAYER 1','PLAYER 2','STATUS']
    w=csv.DictWriter(D1,fieldnames=colheadings)
    w.writeheader()          #CSV HEADING
    D1.close
    FileExist=False
ini=0

#MAIN LOOP OF THE GAME
while 1:
    cls=os.system('cls')
    #HEADING PRINT
    print()
    print(""".___________.__    ______    .___________.    ___       ______    .___________. ______    _______ 
|           |  |  /      |   |           |   /   \     /      |   |           |/  __  \  |   ____|
`---|  |----|  | |  ,----'   `---|  |----`  /  ^  \   |  ,----'   `---|  |----|  |  |  | |  |__   
    |  |    |  | |  |            |  |      /  /_\  \  |  |            |  |    |  |  |  | |   __|  
    |  |    |  | |  `----.       |  |     /  _____  \ |  `----.       |  |    |  `--'  | |  |____ 
    |__|    |__|  \______|       |__|    /__/     \__\ \______|       |__|     \______/  |_______|
                                                                                                  """)
    print()
    if(ini==0):
        # MAIN MENU
        print("""   _   _   _   _     _   _   _   _  
  / \ / \ / \ / \   / \ / \ / \ / \ 
 ( M ( A ( I ( N ) ( M ( E ( N ( U )
  \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ """)
        print()
        print("""    1 . PLAY
    2 . RULES
    3 . LEADERBOARD
    4 . EXIT""")
    else:
        print("""    1 . PLAY AGAIN
    2 . RULES
    3 . LEADERBOARD
    4 . EXIT""")
    while 1:
        try:
            mm=int(input("Choose a number from the given main menu : "))
        except ValueError:
            print("Only integers allowed ! ! !")
        else:
            break
    cls=os.system('cls')
    if(mm==2):
            # RULES FOR THE GAME 
            print()
            print("""██████╗ ██╗   ██╗██╗     ███████╗███████╗
██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
██████╔╝██║   ██║██║     █████╗  ███████╗
██╔══██╗██║   ██║██║     ██╔══╝  ╚════██║
██║  ██║╚██████╔╝███████╗███████╗███████║
╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝""")
            print()
            print("""The Rules of the Game are as follows :-""")
            print()
            print("     1 . Player 1 is X and Player 2 is O.\n     2 . The first player to get 3 of his/her mark in the row(up, down, across, or diagnally) is the winner.\n     3 . When all the 9 grids are filled, the game is over. \n     4 . The grid should be filled with respect to the number in the grid. The grid address are as follows : ")
            print("          - - - - - - - - - - - - ")
            print("                1 | 2 | 3")
            print("                - + - + -")
            print("                4 | 5 | 6")
            print("                - + - + -")
            print("                7 | 8 | 9")
            print("          - - - - - - - - - - - -  \n")
            input("Press enter to get back to the main menu !")
            cls=os.system('cls')
    elif(mm==3):
            #LEADERBOARD
            #READING DATA FROM THE CSV FILE !!!
            print("""██╗     ███████╗ █████╗ ██████╗ ███████╗██████╗ ██████╗  ██████╗  █████╗ ██████╗ ██████╗ 
██║     ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔══██╗
██║     █████╗  ███████║██║  ██║█████╗  ██████╔╝██████╔╝██║   ██║███████║██████╔╝██║  ██║
██║     ██╔══╝  ██╔══██║██║  ██║██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██║██╔══██╗██║  ██║
███████╗███████╗██║  ██║██████╔╝███████╗██║  ██║██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
                                                                                         """)
            print()
            k=1
            if(ini==0 and FileExist==False):
                    print("No one has played this game till now !")
                    print()
            else:
                print('GAME CODE','\t\t','PLAYER 1','\t\t','PLAYER 2','\t\t\t','STATUS')
                with open('TICTACTOE_RECORDS.csv','r') as D1:
                    r=csv.DictReader(D1)
                    for row in r:
                        print(row['GAME CODE'],'\t\t\t',row['PLAYER 1'],'\t\t\t',row['PLAYER 2'],'\t\t\t',row['STATUS'])
            input("Press enter to get back to the main menu !")
            cls=os.system('cls')
    elif(mm==4):
            print()
            print()
            print()
            #EXIT OPTION FROM THE MAIN MENU 
            print("""    )    )  (             )   )             )       (       (            )  
 ( /( ( /(  )\ )       ( /(( /(          ( /(  (    )\ )    )\ )      ( /(  
 )\()))\())(()/((      )\())\())    (    )\()) )\  (()/(   (()/(   (  )\()) 
((_)\((_)\  /(_))\    ((_)((_)\     )\  ((_)((((_)( /(_))   /(_))  )\((_)\  
 _((_) ((_)(_))((_)  __ ((_)((_) _ ((_)  _((_)\ _ )(_))_   (_))__ ((_)_((_) 
| || |/ _ \| _ | __| \ \ / / _ \| | | | | || (_)_\(_|   \  | |_| | | | \| | 
| __ | (_) |  _| _|   \ V | (_) | |_| | | __ |/ _ \ | |) | | __| |_| | .` | 
|_||_|\___/|_| |___|   |_| \___/ \___/  |_||_/_/ \_\|___/  |_|  \___/|_|\_| """)
            print()
            start_time=time.time()
            stopwatch=0
            while True :
                    timer =time.time()-start_time
                    if(timer>3):
                            break
            break
    elif(mm==1):
            ini=ini+1
            print()
            print(""".___________.__    ______    .___________.    ___       ______    .___________. ______    _______ 
|           |  |  /      |   |           |   /   \     /      |   |           |/  __  \  |   ____|
`---|  |----|  | |  ,----'   `---|  |----`  /  ^  \   |  ,----'   `---|  |----|  |  |  | |  |__   
    |  |    |  | |  |            |  |      /  /_\  \  |  |            |  |    |  |  |  | |   __|  
    |  |    |  | |  `----.       |  |     /  _____  \ |  `----.       |  |    |  `--'  | |  |____ 
    |__|    |__|  \______|       |__|    /__/     \__\ \______|       |__|     \______/  |_______|
                                                                                                  """)
            print()
            # COMPLETE GAME CODE
            #GAME CODE
            cod=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']
            GAME_CODE=""
            for i in range(0,6):
                GAME_CODE=GAME_CODE+cod[random.randint(0,len(cod)-1)]
                
            #PLAYERS NAME
            while 1:
                PLAYER_1=input("Enter  the name of FIRST player : ")
                if(PLAYER_1==""):
                    print()
                    print("Please enter a  name !")
                    continue
                else:
                    break
            PLAYER_1=PLAYER_1.capitalize()
            while 1:
                PLAYER_2=input("Enter  the name of SECOND player : ")
                if(PLAYER_2==""):
                    print()
                    print("Please enter a  name !")
                    continue
                else:
                    break
            PLAYER_2=PLAYER_2.capitalize()
            PLAY_1=[PLAYER_1,'X']
            PLAY_2=[PLAYER_2,'O']
            print()
            print("YOUR GAME CODE IS : ",GAME_CODE)
            print()
            print(PLAY_1[0],' gets ',PLAY_1[1])
            print(PLAY_2[0],' gets ',PLAY_2[1])
            print()
            print("Please play accordingly !")
            print()
            input("Press Enter to continue !")
            cls=os.system('cls')
            print()
            print(""".___________.__    ______    .___________.    ___       ______    .___________. ______    _______ 
|           |  |  /      |   |           |   /   \     /      |   |           |/  __  \  |   ____|
`---|  |----|  | |  ,----'   `---|  |----`  /  ^  \   |  ,----'   `---|  |----|  |  |  | |  |__   
    |  |    |  | |  |            |  |      /  /_\  \  |  |            |  |    |  |  |  | |   __|  
    |  |    |  | |  `----.       |  |     /  _____  \ |  `----.       |  |    |  `--'  | |  |____ 
    |__|    |__|  \______|       |__|    /__/     \__\ \______|       |__|     \______/  |_______|
                                                                                                  """)
            print()
            tic={"1":" ","2":" ","3":" ",
                   "4":" ","5":" ","6":" ",
                   "7":" ","8":" ","9":" "}
            keys=[]
            for key in tic:
                keys.append(key)
            try:
                game(PLAY_1,PLAY_2)
            except:
                print("SOME UNIDENTIFIED ERROR OCCURED !\nTRY BACK LATER!")
                input("Press Enter to get back to the main menu")
                continue
            try:
                if(WINNERR==True):
                    RESULT={'GAME CODE':GAME_CODE,'PLAYER 1':PLAYER_1,'PLAYER 2':PLAYER_2,'STATUS':('WINNER IS '+WINNER)}
            except Exception:
                RESULT={'GAME CODE':GAME_CODE,'PLAYER 1':PLAYER_1,'PLAYER 2':PLAYER_2,'STATUS':GAME_DRAW}
            input("Press Enter to get back to the main menu !")
            with open('TICTACTOE_RECORDS.csv','a') as D1:
                colheadings=['GAME CODE','PLAYER 1','PLAYER 2','STATUS']
                w=csv.DictWriter(D1,fieldnames=colheadings)
                w.writerow(RESULT)
    else:
            #INVALID INPUT (EXCEPTION)
            print("INVALID INPUT !\nPlease try again !")
