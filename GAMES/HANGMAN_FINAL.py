#VANSH JAGGI

#HANGMAN

#PROJECT BRAIN JAM (2k20-2k21)

#  DRAWINGS FOR HANGMAN 
def man(k):
        drawing=[
                """
                ___________          ____________
                |          |        /            |  
                |          O       <  * *DEAD* * | 
                |       /  |  \\     \____________|
                |      /   |   \\
                |         / \\
                |        /   \\
                |""",
                """
                ___________          ____________
                |          |        /            |  
                |          O       < ! SAVE ME ! | 
                |       /  |  \\     \____________|
                |      /   |   \\
                |         / \\
                |        /   
                |""",
                """
                ___________
                |          |
                |          O
                |       /  |  \\
                |      /   |   \\
                |         / 
                |        /
                |""",
                """
                ___________
                |          |
                |          O
                |       /  |  \\
                |      /   |   \\
                |         /
                |        
                |""",
                """
                ___________
                |          |
                |          O
                |       /  |  \\
                |      /   |   \\
                |       
                |       
                |""",
                """
                ___________
                |          |
                |          O
                |       /  |  \\
                |      /   | 
                |    
                |    
                |""",
                """
                ___________
                |          |
                |          O
                |       /  |  
                |      /   |  
                |        
                |        
                |""",
                """
                ___________
                |          |
                |          O
                |       /  | 
                |          | 
                |        
                |        
                |""",
                """
                ___________
                |          |
                |          O
                |          | 
                |          |
                |      
                |      
                |""",
                """
                ___________
                |          |
                |          O
                |          | 
                |
                |
                |
                |""",
                """
                ___________
                |          |
                |          O
                |            
                |             
                |         
                |        
                |
                """]
        print(drawing[k])
#IMPORTING MODULES 
import os
import random
import csv
import time
ini=0

# REFRESHING/WRITING THE CSV FILE
if((os.path.isfile('HANGMAN_RECORDS.csv')) is True):
        C1=open('HANGMAN_RECORDS.csv','a+')
        C1.close
        FileExist=True
else:
        C1=open('HANGMAN_RECORDS.csv','w+')
        C1.close
        FileExist=False
#MAIN LOOP OF THE GAME
while 1:
    cls=os.system('cls')
    #HEADING (PRINT STATEMENTS )
    print()
    print(""" __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __. 
|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  | 
|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  | 
|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  | 
|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   | 
|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__| """)
    print()
    print("- - - - - Guess the word before your man gets hung! - - - - -")
    print()
    if(ini==0):
            #MAIN MENU FOR HANGMAN 
            print("""   _   _   _   _     _   _   _   _  
  / \ / \ / \ / \   / \ / \ / \ / \ 
 ( M | A | I | N ) ( M | E | N | U )
  \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/
  
    1 . PLAY
    2 . RULES
    3 . LEADERBOARD
    4 . EXIT""")
    else:  #SECOND GAME 
                    print("""   _   _   _   _     _   _   _   _  
  / \ / \ / \ / \   / \ / \ / \ / \ 
 ( M | A | I | N ) ( M | E | N | U )
  \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/
  
    1 . PLAY AGAIN
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
            print("""The Rules of the Game are as follows :-
            1 . It's an easy game of guessing the word.
            2 . You will have to make guesses.
            3 . Only 10 incorrect attempts will be accepted else your man will be hanged .""")
            print()
            input("Press enter to get back to the main menu (Hangman)!")
            cls=os.system('cls')
    elif(mm==1):
            #PLAYING GAME AND WRITING RECORDS IN THE CSV FILE !
                    #MAIN GAME 
                    print()
                    print(""" __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __. 
|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  | 
|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  | 
|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  | 
|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   | 
|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__| """)
                    print()
                    print("- - - - - Guess the word before your man gets hung! - - - - -")
                    print()
                    NAME=input("Enter Your Name : ")
                    print()
                    tries=10
                    print()
                    #WORDLIST
                    WORDS=["CUSTOMS","FRACTIOUS","HOMAGE","CUPIDITY","RUMINATE","DIFFIDENT","INEXORABLE","KINDLE","MAGNANIMOUS","OSTENTATIOUS","ARCHAELOGY","FACILITATE"]
                    #HINTS FOR WORDS WITH SAME INDEXES
                    HINTS=["Taxes on import","Unruly, bad-tempered, irritable","Honour or respect demonstrated publically, tribute","Greed, great or excessive desire for possessions","To think deeply","Lacking confidence","Relentless","To incite, inflame","High-minded, Generous or forgiving others","Pretentious","The study of material evidence of past human life","To make less difficult"]
                    no=random.randrange(0,12)      #RANDOM NUMBER
                    guessed=False
                    word=WORDS[no]
                    hint=HINTS[no]
                    wc="_"*len(word)
                    guessed_letters=[]
                    guessed_words=[]
                    print()
                    print("Let's Play ! ! !")
                    man(tries)
                    print(wc)
                    
                    while guessed==False and tries>0:
                            print()
                            print("Hint : ",hint)
                            guess=input("Guess a letter or word : ").upper()
                            if(len(guess)==1 and guess.isalpha()):
                                    if(guess in guessed_letters):
                                            print("Already guessed the letter ! ! !")
                                    elif(guess not in word):
                                            print(guess," is not in the word !")
                                            tries=tries-1
                                            guessed_letters.append(guess)
                                    else: 
                                            print("Good Job !\n",guess," is in the word.")
                                            guessed_letters.append(guess)
                                            wordaslist=[]
                                            for i in wc:
                                                    wordaslist.append(i)
                                            for i in word:
                                                    if(guess==i):
                                                            for k in range(0,len(wordaslist)):
                                                                    if(word[k]==guess):
                                                                            wordaslist[k]=word[k]
                                            wc="".join(wordaslist)
                                            if("_"not in wc):
                                                    guessed=True
                            elif(len(guess)==len(word) and guess.isalpha()):
                                    if(guess in guessed_letters):
                                            print("Already guessed the word ! ! !")
                                    elif(guess!=word):
                                            print(guess," is not in the word !")
                                            tries=tries-1
                                            guessed_words.append(guess)
                                    else:
                                            guessed = True
                                            wc=word
                            else:
                                    print("Not a valid guess.")
                            man(tries)
                            print(wc)
                            print()
                    if(guessed==True):    #Final check to the word 
                            print("Congratulations, you guessed the word !\nYOU WIN ! ! ! \n")
                            win=True
                    else:
                            print("You ran out of tries. The word was ",word,"\nBetter luck next time !")
                            win=False
                    #SCORING
                    if(win==True):
                            D={'NAME':NAME,'SCORE':10}
                    else:
                            D={'NAME':NAME,'SCORE':0}
                    #WRITING INTO THE CSV FILE
                    if(ini==0 and FileExist==False):
                            with open('HANGMAN_RECORDS.csv','a') as C1:
                                    colheadings=['NAME','SCORE']
                                    w=csv.DictWriter(C1,fieldnames=colheadings)
                                    w.writeheader()          #CSV HEADING
                                    w.writerow(D)
                    else:
                            with open('HANGMAN_RECORDS.csv','a') as C1:
                                    colheadings=['NAME','SCORE']
                                    w=csv.DictWriter(C1,fieldnames=colheadings)
                                    w.writerow(D)   #SECOND ENTRY NAMES
                    C1.close()
                    ini=ini+1
                    input("Press Enter to get back to the game menu !")
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
            print("NAME\t\tSCORE")
            print()
            k=1
            if(ini==0 and FileExist==False):
                    print("No one has played this game till now !")
                    print()
            else:
                    with open('HANGMAN_RECORDS.csv','r') as C1:
                            r=csv.DictReader(C1)
                            for row in r:
                                    print(row['NAME'],'\t\t',row['SCORE'])
            input("Press enter to get back to the main menu (Hangman)!")
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
            while True :
                    timer =time.time()-start_time
                    if(timer>3):
                            break
            break
    else:
            #INVALID INPUT (EXCEPTION)
            print("INVALID INPUT !\nPlease try again.")
         
 







