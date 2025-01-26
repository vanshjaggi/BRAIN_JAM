#Prototype_2.0

#VANSH JAGGI

#Project 2k20-2k21

#VOCABULARY QUIZ WITH PERMANENT STORAGE 


#IMPORTING MODULES
import os
import random
import csv
import time

ini=0  #INITIALISING

if((os.path.isfile('VQUIZ_RECORDS.csv')) is True):
        B1=open('VQUIZ_RECORDS.csv','a+')
        B1.close
        FileExist=True
else:
        B1=open('VQUIZ_RECORDS.csv','w+')
        B1.close
        FileExist=False

#MAIN LOOP
while True:
        abc=os.system('cls')
        mark1=0
        mark2=0
        # HEADING WITH PRINT STATEMENTS 
        print()
        print(""" __      ______   _____          ____  _    _ _               _______     __   ____  _    _ _____ ______
 \ \    / / __ \ / ____|   /\   |  _ \| |  | | |        /\   |  __ \ \   / /  / __ \| |  | |_   _|___  /
  \ \  / / |  | | |       /  \  | |_) | |  | | |       /  \  | |__) \ \_/ /  | |  | | |  | | | |    / / 
   \ \/ /| |  | | |      / /\ \ |  _ <| |  | | |      / /\ \ |  _  / \   /   | |  | | |  | | | |   / /  
    \  / | |__| | |____ / ____ \| |_) | |__| | |____ / ____ \| | \ \  | |    | |__| | |__| |_| |_ / /__ 
     \/   \____/ \_____/_/    \_\____/ \____/|______/_/    \_\_|  \_\ |_|     \___\_\\____/|_____/_____|
                                                                                                        
                                                                                                        """)
        print()
        print("""   _   _   _   _     _   _   _   _  
  / \ / \ / \ / \   / \ / \ / \ / \ 
 ( M | A | I | N ) ( M | E | N | U )
  \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/

  
        1 . Play Quiz
        2 . Leaderboard
        3 . Exit """)
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
                print(""" __      ______   _____          ____  _    _ _               _______     __   ____  _    _ _____ ______
 \ \    / / __ \ / ____|   /\   |  _ \| |  | | |        /\   |  __ \ \   / /  / __ \| |  | |_   _|___  /
  \ \  / / |  | | |       /  \  | |_) | |  | | |       /  \  | |__) \ \_/ /  | |  | | |  | | | |    / / 
   \ \/ /| |  | | |      / /\ \ |  _ <| |  | | |      / /\ \ |  _  / \   /   | |  | | |  | | | |   / /  
    \  / | |__| | |____ / ____ \| |_) | |__| | |____ / ____ \| | \ \  | |    | |__| | |__| |_| |_ / /__ 
     \/   \____/ \_____/_/    \_\____/ \____/|______/_/    \_\_|  \_\ |_|     \___\_\\____/|_____/_____|
                                                                                                        
                                                                                                        """)
                print()
                Name=input("Enter Your Name :- ")
                size=len(Name)
                cls=os.system('cls')
                print()
                print("""  ___ ___ ___ ___ ___ ___ _   _ _  _______   __  _    _____   _____ _     
 |   \_ _| __| __|_ _/ __| | | | ||_   _\ \ / / | |  | __\ \ / / __| |    
 | |) | || _|| _| | | (__| |_| | |__| |  \ V /  | |__| _| \ V /| _|| |__  
 |___/___|_| |_| |___\___|\___/|____|_|   |_|   |____|___| \_/ |___|____| 
                                                                          """)
                print()
                print("1  -  Mains")
                print("2  -  Advanced")
                print("\t\t**recommended to start with the Mains level !")
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
                        Maingiven=True
                else:
                        Maingiven=False                        
                if(x=='2'):
                        Advancegiven=True
                        mark1="Not Attempted"
                else:
                        Advancegiven=False
                if(x=='1'):
                        
                        cls=os.system('cls')

                        print(""" __  __    __    ____  _  _  ___    __    ____  _  _  ____  __   
(  \/  )  /__\  (_  _)( \( )/ __)  (  )  ( ___)( \/ )( ___)(  )  
 )    (  /(__)\  _)(_  )  ( \__ \   )(__  )__)  \  /  )__)  )(__ 
(_/\/\_)(__)(__)(____)(_)\_)(___/  (____)(____)  \/  (____)(____)""")
                        print()
                        mark1=0
                        print("You have taken the Mains level Vocabulay quiz !")
                        print()
                        print("RULES FOR THE QUIZ :\n\t\t*read carefully \n\n  1. All questions should be attempted for better analysis \n  2.There will be only 5 questions in the quiz \n  3.(+4) marks for every correct answer and (0) for every incorrect answer.\n  4.Answers should in a single character *in the format (A,B,C,D) \n")
                        xyz=input("PRESS ENTER FOR THE QUIZ TO START !")
                        print()

                        #Quiz base easy

                        a="Something of interest or importance \n  A - Perception \n  B - Fib \n  C - Concern \n  D - Brand"
                        b="A pesron with excessive zeal \n  A - Building\n  B - Poseur\n  C - Hypocrisy\n  D - Fanatic"
                        c="An excessive abundance \n  A - Altruism\n  B - Hubbub\n  C - Plethora\n  D - Camaraderie"
                        d="The central point on which a mechanism turns \n  A - Pivot\n  B - Ocean\n  C - Brood\n  D - Hubris"
                        e="Peaceful and calm \n  A - Tranquil\n  B - Ostentatious\n  C - Jejune\n  D - Lackadaisical"
                        f="Mental awareness\n  A - Noun\n  B - Consciousness\n  C - Bureaucracy\n  D - Kudzu"
                        g="Oily or greasy\n  A - Condescending\n  B - Oleaginous\n  C - Ordinary\n  D - Festooned"
                        h="To change words from one language to another \n  A - Finagle\n  B - Translate\n  C - Hope\n  D - Illuminate"
                        i="To write down something that is spoken\n  A - Exonerate\n  B - Alleviate\n  C - Kindle\n  D - Transcribe"
                        j="To want something to happen\n  A - Mock\n  B - Hope\n  C - Nullify\n  D - Plummet"
                        QUESTIONS=[a,b,c,d,e,f,g,h,i,j,'k']
                        ANSWERS=['C','D','C','A','A','B','B','B','D','B']

                        z=10
                        QUESTION1=QUESTIONS
                        ANSWER1=ANSWERS
                        for k in range(1,6):
                                i=random.randrange(0,z)
                                print("QUESTION-",k,'-',QUESTION1[i],'\n')
                                ans=input("Enter your answer :- ")
                                ans=ans.capitalize()
                                if(ans==ANSWER1[i]):
                                        print("CORRECT ANSWER")
                                        mark1=mark1+4
                                else:
                                        print("INCORRECT ANSWER \n \nThe Correct answer is :- ",ANSWER1[i],)
                                QUESTION1.pop(i)
                                ANSWER1.pop(i)

                                z=z-1
                                print("Score=",mark1,'\n\n')
                        print("Your total score is",mark1,"out of 20",'\n\n\n')
                        
                        m=input("If you wish to continue with the Advanced level press (2) else press enter : ")
                        print()
                        print()
                        if(m!='2'):
                                print("Congratulations",Name,",\nYou have completed the Mains level of the vocabulary quiz!\n\n\n")
                                mark2="Not attempted."
                        
                if(x=='2' or m=='2'):
                        Advancegiven=True

                        hjwgxw=os.system('cls')

                        print("""   __    ____  _  _  __    _  _  ___  ____    __    ____  _  _  ____  __   
  /__\  (  _ \( \/ )/__\  ( \( )/ __)( ___)  (  )  ( ___)( \/ )( ___)(  )  
 /(__)\  )(_) )\  //(__)\  )  (( (__  )__)    )(__  )__)  \  /  )__)  )(__ 
(__)(__)(____/  \/(__)(__)(_)\_)\___)(____)  (____)(____)  \/  (____)(____)""")
                        print("You have taken the Advanced level vocabulary quiz !")
                        mark2=0
                        print()
                        print("RULES FOR THE QUIZ :\n\t\t*read carefully \n  1. All questions should be attempted for better analysis \n  2.There will be only 5 questions in the quiz \n  3.(+4) marks for every correct answer, (-1) for every incorrect answer and (0) marks for not attempted.\n  4.Answers should in a single character *in the format (A,B,C,D)\n")
                        xyz=input("PRESS ENTER FOR THE QUIZ TO START !")
                        print()
                        
                        #Quiz base hard
                        
                        a="The sound of two vowels in one syllable\n  A - Diphthong\n  B - Vexillologist\n  C - Mugwump\n  D - Billingsgate"
                        b="Not clearly stated\n  A - Ludic\n  B - Catawampus\n  C - Vague\n  D - Scabrous"
                        c="A term of endearment for a young boy\n  A - Boychick\n  B - Empathy\n  C - Bristle\n  D - Preamble"
                        d="To be indecisive\n A - Excuplate\n  B - Dither\n  C - Absolve\n  D - Topple"
                        e="A primate's big toe\n  A - Hallux\n  B - Hangar\n  C - Filament\n  D - Bobolink"
                        f="Excessively sentimental\n  A - Omnious\n  B - Lazy\n  C - Important\n  D - Saccharine"
                        g="Relating to a river bank\n  A - Riparian\n  B - Crepuscular\n  C - Rambunctious\n  D - Condescending"
                        h="To hit forcefully\n  A - Burnish\n  B - Bumfuzzle\n  C - Sock\n  D - Whelm"
                        i="Unshakeable\n  A - Provocative\n  B - Adamant\n  C - Timorous\n  D - Prudent"
                        j="Excessive and unnecessary\n  A - Immoderate\n  B - Reticent\n  C - Superfluous\n  D - Preeminent"
                        QUESTIONS=[a,b,c,d,e,f,g,h,i,j,'k']
                        ANSWERS=['A','C','A','B','A','D','A','C','B','C']

                        z=10
                        QUESTION2=QUESTIONS
                        ANSWER2=ANSWERS
                        for k in range(1,6):
                                i=random.randrange(0,z)
                                print("QUESTION-",k,'-',QUESTION2[i],'\n')
                                ans=input("Enter your answer :- ")
                                ans=ans.capitalize()
                                if(ans==ANSWER2[i]):
                                        print("CORRECT ANSWER")
                                        mark2=mark2+4
                                elif(ans==""):
                                        mark2=mark2+0
                                else:
                                        print("INCORRECT ANSWER \n \nThe Correct answer is :- ",ANSWER2[i],)
                                        mark2=mark2-1
                                QUESTION2.pop(i)
                                ANSWER2.pop(i)
                                
                                z=z-1
                                print("Score=",mark2,'\n\n')
                        print("Your total score is",mark2,"out of 20",'\n\n\n')
                        print()
                        print()
                        if(x==2):
                                print("Congratulations",Name,",\nYou have completed the Advanced level of the vocabulary quiz\n\n\n!")
                if(x=='1' and m=='2'):
                        print("Congratulations",Name,",\nYou have completed both the levels of the vocabulary quiz!\n\n\n")
                D={"NAME":Name,"Mains Level":mark1,"Advance Level":mark2}
                if(ini==0 and FileExist==False):
                        with open('VQUIZ_RECORDS.csv','a') as B1:
                                colheadings=['NAME','Mains Level','Advance Level']
                                w=csv.DictWriter(B1,fieldnames=colheadings)
                                w.writeheader()          #CSV HEADING
                                w.writerow(D)
                else:
                        with open('VQUIZ_RECORDS.csv','a') as B1:
                                colheadings=['NAME','Mains Level','Advance Level']
                                w=csv.DictWriter(B1,fieldnames=colheadings)
                                w.writerow(D)   #SECOND ENTRY NAMES
                ini=ini+1
                P_A=input("Press Enter to go to the main menu of the quiz !")
        elif(ss==2):
                abc=os.system('cls')
                print()
                print("""██╗     ███████╗ █████╗ ██████╗ ███████╗██████╗ ██████╗  ██████╗  █████╗ ██████╗ ██████╗ 
██║     ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔══██╗
██║     █████╗  ███████║██║  ██║█████╗  ██████╔╝██████╔╝██║   ██║███████║██████╔╝██║  ██║
██║     ██╔══╝  ██╔══██║██║  ██║██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██║██╔══██╗██║  ██║
███████╗███████╗██║  ██║██████╔╝███████╗██║  ██║██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
                                                                                         """)
                print("NAME \t\t Mains Level \t\t Advance Level")
                if(ini==0 and FileExist==False):
                        print("No one has played this game till now !")
                        print()
                else:
                        with open('VQUIZ_RECORDS.csv','r') as B1:
                                r=csv.DictReader(B1)
                                for row in r:
                                        print(row['NAME'],'\t\t',row['Mains Level'],'\t\t\t',row['Advance Level'])
                print()
                print()
                input("Press enter to get back to the Main Menu (VOCABULARY QUIZ)!")
                abc=os.system('cls')
        elif(ss==3):
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


                
                
        


                         






        
