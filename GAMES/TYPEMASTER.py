#TypeMaster1.0

#Project 2k20-2k21

#SWOYAM SAHOO

#TYPE MASTER WITH PERMANENT STORAGE 


#IMPORTING MODULES
import os
import random
import csv
import time

#DEFINING THE GAME HARD
#------------------------------------------HARD----------------------------------


def hard():
    LEVEL="BRING IT ON"
    print("""  ____  _____  _____ _   _  _____   _____ _______    ____  _   _ 
 |  _ \|  __ \|_   _| \ | |/ ____| |_   _|__   __|  / __ \| \ | |
 | |_) | |__) | | | |  \| | |  __    | |    | |    | |  | |  \| |
 |  _ <|  _  /  | | | . ` | | |_ |   | |    | |    | |  | | . ` |
 | |_) | | \ \ _| |_| |\  | |__| |  _| |_   | |    | |__| | |\  |
 |____/|_|  \_\_____|_| \_|\_____| |_____|  |_|     \____/|_| \_|
                                                                 
                                                                 """)
    print("You have selected the Bring it on level for Type master !")
    print()
    print()
    words=["PLEASE TAKE YOUR DOG OSLO OUT FOR A WALK","WHAT A BEAUTIFUL DAY IT IS ON THE BEACH","THE BROWN FAMILY DECIDED TO GO TO THE AMUSMENT PARK","FRIENDS ARE FLOWERS IN THE GARDEN OF LIFE","THE SQUEAKY WHEEL GETS THE GREASE","CAUGHT BETWEEN A ROCK AND A HARD PLACE"," JUST STAYING ONE DAY AHEAD OF YESTERDAY","WHATEVER YOU ARE TODAY BE A GOOD ONE"]
    mark=[]
    l=[1,2,3,4,5,6,7,8]
    #ERROR CHECK
    error=0
    #-----------
    print("You will get 8 sentences.")
    
    y=input("press enter when you are ready")
    abc=os.system('cls')
    
    for i in range(8):
        print("""  ____  _____  _____ _   _  _____   _____ _______    ____  _   _ 
 |  _ \|  __ \|_   _| \ | |/ ____| |_   _|__   __|  / __ \| \ | |
 | |_) | |__) | | | |  \| | |  __    | |    | |    | |  | |  \| |
 |  _ <|  _  /  | | | . ` | | |_ |   | |    | |    | |  | | . ` |
 | |_) | | \ \ _| |_| |\  | |__| |  _| |_   | |    | |__| | |\  |
 |____/|_|  \_\_____|_| \_|\_____| |_____|  |_|     \____/|_| \_|
                                                                 
                                                                 """)
        print("You have selected the Bring it on level for Type master !")
        print()

        #TO RANDOMIZE THE ORDER
        f=random.choice(l)
        #----------------------
        uy=words[f-1]
        print(uy)
        l.remove(f)
        starttime=time.time()
        x=input("")
        timer=int(time.time()-starttime)
        mark.append(timer)
        if(x.upper()!=uy):
            error=error+1
        cls=os.system('cls')
    print("You took:")
    for i in mark:
        print(i,",", end="")
    print("seconds respectively")
    print()
    s=0
    for i in mark:
        s=s+i
    average=int(s/8)
    point=0
    print("Your average time was: ",average)
    print("Number of errors committed are ",error)
    if(average<=7):
        if(error==0):
            point=100
        else:
            point=90-(5*error)
    elif(average>7 and average<=13):
        if(error==0):
            point=80
        else:
            point=70-(5*error)
    elif(average>14 and average<=20):
        if(error==0):
            point=60
        else:
            point=50-(5*error)
    elif(average>20 and average<=26):
        if(error==0):
            point=40
        else:
            point=30-(5*error)
    elif(average>26 and average<=32):
        if(error==0):
            point=20
        else:
            point=10-(5*error)
    elif(average>32):
        if(error==0):
            point=0
        else:
            point=0-(5*error)        
    print("Your total score is: ",point)
    #-----------WRITING IN A CSV FILE-----------------
    d={'NAME':name,'LEVEL':LEVEL,'AVERAGE TIME':average,'ERRORS':error,'POINTS':point}
    with open('TYPEMASTER_RECORDS.csv','a') as f:
        colheading=['NAME','LEVEL','AVERAGE TIME','ERRORS','POINTS']
        w=csv.DictWriter(f,fieldnames=colheading)
        w.writerow(d)
    #---------------------------------------------------

    input("Press Enter to get back to the main menu !")
#-----------------------------EASY-----------------------------------------------


        
def easy():
    LEVEL="BEGINNERS"
    print("""  ____  ______ _____ _____ _   _ _   _ ______ _____   _____ 
 |  _ \|  ____/ ____|_   _| \ | | \ | |  ____|  __ \ / ____|
 | |_) | |__ | |  __  | | |  \| |  \| | |__  | |__) | (___  
 |  _ <|  __|| | |_ | | | | . ` | . ` |  __| |  _  / \___ \ 
 | |_) | |___| |__| |_| |_| |\  | |\  | |____| | \ \ ____) |
 |____/|______\_____|_____|_| \_|_| \_|______|_|  \_\_____/ 
                                                            
                                                            """)
    print("You have selected the beginners level for Type master !")
    
    words=["THIS IS A POSTER","THE CAT STRECHED","RAJ MADE A PICTURE","OPEN THE JAR","READ THE DIRECTIONS","HE WAS EATING","THIS WORLD IS CRUEL","DO NOT GO ANYWHERE"]
    mark=[]
    l=[1,2,3,4,5,6,7,8]
    #ERROR CHECK
    error=0
    #-----------
    print("You will get 8 sentences.")
    
    y=input("press enter when you are ready")
    cls=os.system('cls')
    for i in range(8):
        print("""  ____  ______ _____ _____ _   _ _   _ ______ _____   _____ 
 |  _ \|  ____/ ____|_   _| \ | | \ | |  ____|  __ \ / ____|
 | |_) | |__ | |  __  | | |  \| |  \| | |__  | |__) | (___  
 |  _ <|  __|| | |_ | | | | . ` | . ` |  __| |  _  / \___ \ 
 | |_) | |___| |__| |_| |_| |\  | |\  | |____| | \ \ ____) |
 |____/|______\_____|_____|_| \_|_| \_|______|_|  \_\_____/ 
                                                            
                                                            """)
        print("You have selected the beginners level for Type master !")
        #TO RANDOMIZE THE ORDER
        f=random.choice(l)
        #----------------------
        uy=words[f-1]
        print(uy)
        l.remove(f)
        starttime=time.time()
        x=input("")
        timer=int(time.time()-starttime)
        mark.append(timer)
        if(x.upper()!=uy):
            error=error+1
        cls=os.system('cls')
    print("You took:")
    for i in mark:
        print(i,",", end="")
    print("seconds respectively")
    print()
    s=0
    for i in mark:
        s=s+i
    average=int(s/8)
    point=0
    print("Your average time was: ",average)
    print("Number of errors committed are ",error)
    if(average<=3):
        if(error==0):
            point=100
        else:
            point=90-(5*error)
    elif(average>3 and average<=6):
        if(error==0):
            point=80
        else:
            point=70-(5*error)
    elif(average>6 and average<=9):
        if(error==0):
            point=60
        else:
            point=50-(5*error)
    elif(average>9 and average<=13):
        if(error==0):
            point=40
        else:
            point=30-(5*error)
    elif(average>14 and average<=17):
        if(error==0):
            point=20
        else:
            point=10-(5*error)
    elif(average>17):
        if(error==0):
            point=0
        else:
            point=0-(5*error)        
    print("Your total score is: ",point)
    #-----------WRITING IN A CSV FILE-----------------
    d={'NAME':name,'LEVEL':LEVEL,'AVERAGE TIME':average,'ERRORS':error,'POINTS':point}
    with open("TYPEMASTER_RECORDS.csv","a") as f:
        colheading=['NAME','LEVEL','AVERAGE TIME','ERRORS','POINTS']
        w=csv.DictWriter(f,fieldnames=colheading)
        w.writerow(d)
    #---------------------------------------------------
    print("If you wish to continue to the hard level, press(2)")
    opopo=input("")
    cls=os.system('cls')
    if(opopo=="2"):
        hard()

        
#--------------------------------------------------------------------------




ini=0  #INITIALISING

if((os.path.isfile('TYPEMASTER_RECORDS.csv')) is True):
        A1=open('TYPEMASTER_RECORDS.csv','a+')
        A1.close
        FileExist=True
else:
    with open("TYPEMASTER_RECORDS.csv","w+") as f:
        colheading=['NAME','LEVEL','AVERAGE TIME','ERRORS','POINTS']
        w=csv.DictWriter(f,fieldnames=colheading)
        w.writeheader()    
    FileExist=False


#MAIN LOOP
while True:
        abc=os.system('cls')
        mark1=0
        mark2=0
        # HEADING WITH PRINT STATEMENTS 
        print()
        print("""._______________    ____ .______    _______    .___  ___.      ___           _______.___________._______ .______         
|           \   \  /   / |   _  \  |   ____|   |   \/   |     /   \         /       |           |   ____||   _  \        
`---|  |----`\   \/   /  |  |_)  | |  |__      |  \  /  |    /  ^  \       |   (----`---|  |----|  |__   |  |_)  |       
    |  |      \_    _/   |   ___/  |   __|     |  |\/|  |   /  /_\  \       \   \       |  |    |   __|  |      /        
    |  |        |  |     |  |      |  |____    |  |  |  |  /  _____  \  .----)   |      |  |    |  |____ |  |\  \----.   
    |__|        |__|     | _|      |_______|   |__|  |__| /__/     \__\ |_______/       |__|    |_______|| _| `._____|   
                                                                                                                         """)
        print()
        print("""   _   _   _   _     _   _   _   _  
  / \ / \ / \ / \   / \ / \ / \ / \ 
 ( M | A | I | N ) ( M | E | N | U )
  \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/

  
        1 . Play Quiz
        2 . How to play ? (Rules !)
        3 . Leaderboard
        4 . Exit """)
        print()
        while 1:
                try:
                        ss=int(input("Enter the desired option from the main menu :- "))
                except ValueError:
                        print("You can only enter integer value from the given main menu !\nTry Again !")
                else:
                        break
        if(ss==1):
                cls=os.system('cls')
                print()
                print("""._______________    ____ .______    _______    .___  ___.      ___           _______.___________._______ .______         
|           \   \  /   / |   _  \  |   ____|   |   \/   |     /   \         /       |           |   ____||   _  \        
`---|  |----`\   \/   /  |  |_)  | |  |__      |  \  /  |    /  ^  \       |   (----`---|  |----|  |__   |  |_)  |       
    |  |      \_    _/   |   ___/  |   __|     |  |\/|  |   /  /_\  \       \   \       |  |    |   __|  |      /        
    |  |        |  |     |  |      |  |____    |  |  |  |  /  _____  \  .----)   |      |  |    |  |____ |  |\  \----.   
    |__|        |__|     | _|      |_______|   |__|  |__| /__/     \__\ |_______/       |__|    |_______|| _| `._____|   
                                                                                                                         """)
                print()
                name=input("Enter Your Name :- ")
                size=len(name)
                cls=os.system('cls')
                print()
                print("""  ___ ___ ___ ___ ___ ___ _   _ _  _______   __  _    _____   _____ _     
 |   \_ _| __| __|_ _/ __| | | | ||_   _\ \ / / | |  | __\ \ / / __| |    
 | |) | || _|| _| | | (__| |_| | |__| |  \ V /  | |__| _| \ V /| _|| |__  
 |___/___|_| |_| |___\___|\___/|____|_|   |_|   |____|___| \_/ |___|____| 
                                                                          """)
                print()
                print("1  -  BEGINNERS")
                print("2  -  BRING IT ON")
                print("\t\t**recommended to start with the  !")
                print()
                x=input("Select the number of difficulty level as per the menu given :- ")
                print()
                if(x!='1' and x!='2'):
                        while True:
                                print("Please enter a valid value !")
                                x=input("Select the number of difficulty level as per the menu given :- ")
                                print()
                                if(x=='1' or x=='2'):
                                        break
                if(x=='1'):
                        BEGINNERS_given=True
                else:
                        BEGINNERS_given=False                        
                if(x=='2'):
                        BRING_IT_ON_given=True
                        mark1="Not Attempted"
                else:
                        BRING_IT_ON_given=False
                if(x=='1'):
                        
                        cls=os.system('cls')
                        easy()
                                              
                if(x=='2'):
                        BRING_IT_ON_given=True

                        hjwgxw=os.system('cls')
                        hard()  
                
        elif(ss==2):
                abc=os.system('cls')
                print()
                print("""██████╗ ██╗   ██╗██╗     ███████╗███████╗
██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
██████╔╝██║   ██║██║     █████╗  ███████╗
██╔══██╗██║   ██║██║     ██╔══╝  ╚════██║
██║  ██║╚██████╔╝███████╗███████╗███████║
╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝
                                         """)
                print("""

    1 . Typemaster is an interactive time restrained game, the more time you take the more points you lose.
    2 . You will have to type the given sentences as fast as you can.
    3 . Your time taken to write a total of 8 sentences will be calculated along with the errors you make and scores will be given on the basis of that out of 100.""")
                input("Press Enter to get back the main menu (TYPE MASTER)!")
        elif(ss==3):
                abc=os.system('cls')
                print()
                print("""██╗     ███████╗ █████╗ ██████╗ ███████╗██████╗ ██████╗  ██████╗  █████╗ ██████╗ ██████╗ 
██║     ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔══██╗
██║     █████╗  ███████║██║  ██║█████╗  ██████╔╝██████╔╝██║   ██║███████║██████╔╝██║  ██║
██║     ██╔══╝  ██╔══██║██║  ██║██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██║██╔══██╗██║  ██║
███████╗███████╗██║  ██║██████╔╝███████╗██║  ██║██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
                                                                                         """)
                print("NAME\t          LEVEL\t\t    AVG TIME      \tERROR\t\tPOINTS")
                with open('TYPEMASTER_RECORDS.csv','r+') as f:
                        r=csv.DictReader(f)
                        for row in r:
                            print(row['NAME'],"    \t",row['LEVEL'],"\t\t",row['AVERAGE TIME'],"\t\t",row['ERRORS'],"\t\t",row['POINTS'])
                print()
                input("Press enter to get back to the Main Menu !")
                abc=os.system('cls')
        elif(ss==4):
                cls=os.system('cls')
                print()
                print()
                print()
                print("""  _   _     U  ___ u  ____   U _____ u      __   __   U  ___ u   _   _       _   _      _      ____         _____    _   _   _   _     
 |'| |'|     \/"_ \/U|  _"\ u\| ___"|/      \ \ / /    \/"_ \/U |"|u| |     |'| |'| U  /"\  u |  _"\       |" ___|U |"|u| | | \ |"|    
/| |_| |\    | | | |\| |_) |/ |  _|"         \ V /     | | | | \| |\| |    /| |_| |\ \/ _ \/ /| | | |     U| |_  u \| |\| |<|  \| |>   
U|  _  |u.-,_| |_| | |  __/   | |___        U_|"|_u.-,_| |_| |  | |_| |    U|  _  |u / ___ \ U| |_| |\    \|  _|/   | |_| |U| |\  |u   
 |_| |_|  \_)-\___/  |_|      |_____|         |_|   \_)-\___/  <<\___/      |_| |_| /_/   \_\ |____/ u     |_|     <<\___/  |_| \_|    
 //   \\       \\    ||>>_    <<   >>     .-,//|(_       \\   (__) )(       //   \\  \\    >>  |||_        )(\\,- (__) )(   ||   \\,-. 
(_") ("_)     (__)  (__)__)  (__) (__)     \_) (__)     (__)      (__)     (_") ("_)(__)  (__)(__)_)      (__)(_/     (__)  (_")  (_/  
                                                                                                                                       """)
                print()
                start_time=time.time()
                stopwatch=0
                while True :
                        timer =time.time()-start_time
                        if(timer>3):
                                break
                break
        else:
                #INVALID INPUT (EXCEPTION)
                print("INVALID INPUT !\nPlease try again.")

