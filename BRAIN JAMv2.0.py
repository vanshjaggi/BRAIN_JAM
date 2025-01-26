# MAIN PAGE --------------- BRAIN JAM

#PROJECT 2k20-2k21

#IMPORTING MODULES
#=======================================================================================================================================
import os
from tkinter import *
import csv
import subprocess
#=======================================================================================================================================
#LOGIN PASSWORD
USERNAME=['VANSH@BJ.com']
PASSWORD=['vansh4123']
def SCREEN_EXIT(SCREEN):
        SCREEN.destroy()
#=======================================================================================================================================
path=os.getcwd()
#DEFINING FUNCTIONS
#=======================================================================================================================================
#=======================================================================================================================================
#CALLING ALL GAMES                                        GAME MENU
#=======================================================================================================================================
#=======================================================================================================================================
def Call_GAMEMENU():
        GAME_MENU= Tk()
        GAME_MENU.geometry('445x520')
        GAME_MENU.minsize(445,520)
        GAME_MENU.maxsize(445,520)
        GAME_MENU.title('GAME MENU')
        GAME_MENU.iconbitmap(path+'\\IMAGES\\favicon.ico')


        
        label=Label(GAME_MENU, text="",pady=40)
        label.grid(row=0,column=0)
        HEADING=Button(GAME_MENU,text="|         GAME MENU          |",font=('Product Sans',25),fg = 'yellow',bg='red', padx=73.5, pady=20)
        HEADING.place(relx = 0.5, anchor='n')


        HANGMAN=Button(GAME_MENU,text="HANGMAN",command=Call_HANGMAN, padx=73.5, pady=77)
        HANGMAN.grid(row=1,column=0)#HANGMAN BUTTON
        VOCABQUIZ=Button(GAME_MENU,text="VOCAB QUIZ", command=Call_VOCABQUIZ, padx=73.5, pady=77)
        VOCABQUIZ.grid(row=1,column=1)#VOCAB QUIZ
        TICTACTOE=Button(GAME_MENU,text="TIC TAC TOE", command=Call_TIC_TAC_TOE, padx=72, pady=77)
        TICTACTOE.grid(row=2,column=0)#TIC TAC TOE
        TYPEMASTER=Button(GAME_MENU,text="TYPE MASTER", command=Call_TYPEMASTER, padx=72, pady=77,)
        TYPEMASTER.grid(row=2, column=1)#TYPE MASTER
        BACK_BUTTON=Button(GAME_MENU,text="BACK TO THE MAIN MENU",command=lambda:SCREEN_EXIT(GAME_MENU), padx=146.5, pady=20,bg='light blue')
        BACK_BUTTON.grid(row=3, columnspan=2)#BACK BUTTON




        GAME_MENU.mainloop()

def Call_HANGMAN():
    path = os.getcwd()
    print(f"Current working directory: {path}")
    
    # Construct the full path to the Hangman file
    hangman_path = os.path.join(path, "GAMES", "HANGMAN_FINAL.py")
    
    # Check if the file exists
    if not os.path.exists(hangman_path):
        print(f"File not found: {hangman_path}")
        return

    # Use subprocess to run the script
    try:
        cmd = f'python "{hangman_path}"'
        subprocess.call(cmd, shell=True)  # Use shell=True to handle spaces in paths
    except Exception as e:
        print(f"Error running Hangman: {e}")
def Call_VOCABQUIZ():
    path = os.getcwd()
    vocab_quiz_path = os.path.join(path, "GAMES", "PROTOTYPE_2.0.py")
    try:
        if os.path.exists(vocab_quiz_path):
            cmd = f'python "{vocab_quiz_path}"'
            subprocess.call(cmd, shell=True)
        else:
            print(f"File not found: {vocab_quiz_path}")
    except Exception as e:
        print()
        print("GAME UNDER MAINTENANCE! TRY BACK LATER.")
        print(f"Error: {e}")

def Call_TIC_TAC_TOE():
    path = os.getcwd()
    tic_tac_toe_path = os.path.join(path, "GAMES", "TIC_TAC_TOE.py")
    try:
        if os.path.exists(tic_tac_toe_path):
            cmd = f'python "{tic_tac_toe_path}"'
            subprocess.call(cmd, shell=True)
        else:
            print(f"File not found: {tic_tac_toe_path}")
    except Exception as e:
        print()
        print("GAME UNDER MAINTENANCE! TRY BACK LATER.")
        print(f"Error: {e}")

def Call_TYPEMASTER():
    path = os.getcwd()
    typemaster_path = os.path.join(path, "GAMES", "TYPEMASTER.py")
    try:
        if os.path.exists(typemaster_path):
            cmd = f'python "{typemaster_path}"'
            subprocess.call(cmd, shell=True)
        else:
            print(f"File not found: {typemaster_path}")
    except Exception as e:
        print()
        print("GAME UNDER MAINTENANCE! TRY BACK LATER.")
        print(f"Error: {e}")
#=======================================================================================================================================
#=======================================================================================================================================
#LEADERBOARD SCREEN COMPLETE CODE
#=======================================================================================================================================
#=======================================================================================================================================
def LEADERBOARD_SCREEN():
        LEADERBOARD_SCREEN=Tk()
        LEADERBOARD_SCREEN.geometry('444x562')
        LEADERBOARD_SCREEN.title('LEADERBOARD')
        LEADERBOARD_SCREEN.iconbitmap(path+'\\IMAGES\\favicon.ico')

        label=Label(LEADERBOARD_SCREEN, text="            ",pady=60)
        label.grid(row=0,column=0)#label for better placing

        HEADING=Button(LEADERBOARD_SCREEN,text="L E A D E R B O A R D",font=('Elephant',20),fg = 'white',bg='#eebb4d', padx=73.5, pady=40)
        HEADING.place(relx = 0.5, anchor='n')

        HANGMAN=Button(LEADERBOARD_SCREEN,text="HANGMAN", padx=73.5, pady=77,command=HANGMAN_RECORDS)
        HANGMAN.grid(row=1,column=0)#HANGMAN BUTTON
        VOCABQUIZ=Button(LEADERBOARD_SCREEN,text="VOCAB QUIZ", padx=73.5, pady=77,command=VOACABQUIZ_RECORDS)
        VOCABQUIZ.grid(row=1,column=1)#VOCAB QUIZ
        TICTACTOE=Button(LEADERBOARD_SCREEN,text="TIC TAC TOE", padx=72, pady=77,command=TICTACTOE_RECORDS)
        TICTACTOE.grid(row=2,column=0)#TIC TAC TOE
        TYPEMASTER=Button(LEADERBOARD_SCREEN,text="TYPE MASTER", padx=72, pady=77,command=TYPEMASTER_RECORDS)
        TYPEMASTER.grid(row=2, column=1)#TYPE MASTER
        BACK_BUTTON=Button(LEADERBOARD_SCREEN,text="BACK TO THE MAIN MENU",command=lambda:SCREEN_EXIT(LEADERBOARD_SCREEN), padx=146.5, pady=20,bg='light blue')
        BACK_BUTTON.grid(row=3, columnspan=2)#BACK BUTTON

        
        
        LEADERBOARD_SCREEN.mainloop()
def HANGMAN_RECORDS():
        hangrec=Tk()
        hangrec.title('HANGMAN RECORDS')
        hangrec.iconbitmap(path+'\\IMAGES\\favicon.ico')

        
        LB1=Listbox(hangrec, width = 30, bg = 'azure')
        LB2=Listbox(hangrec, width = 25, bg = 'azure')
        LB=Listbox(hangrec, width = 5, bg = 'azure')
        try:
            with open('HANGMAN_RECORDS.csv','r') as C1:
                r=csv.DictReader(C1)
                ini=1
                for row in r:
                        LB1.insert(ini,'                       '+row['NAME'])
                        LB2.insert(ini,'                        '+row['SCORE'])
                        LB.insert(ini,'    '+str(ini))
                        ini=ini+1
                if(ini==1):
                        LB.insert(1,"NO       ")
                        LB1.insert(1,"RECORDS         ")
                        LB2.insert(1,"FOUND          ")
        except:
            LB.insert(1,"NO       ")
            LB1.insert(1,"RECORDS         ")
            LB2.insert(1,"FOUND          ")
                
        LABEL=Label(hangrec,text='S.No.').grid(row=1,column=0)
        LABEL=Label(hangrec,text='NAME').grid(row=1,column=1)
        LABEL=Label(hangrec,text='SCORE').grid(row=1,column=2)
        LB1.grid(row=2,column=1)
        LB2.grid(row=2,column=2)
        LB.grid(row=2,column=0)
        LABEL=Label(hangrec,text="""HANGMAN RECORDS""",font=('Elephant',20),fg='red').grid(row=0,columnspan=3)
        LABEL=Label(hangrec,text="",font=('Elephant',20)).grid(row=3,columnspan=3)#for better placing
        BACK_BUTTON=Button(hangrec,text="BACK TO THE LEADERBOARD MENU",command=lambda:SCREEN_EXIT(hangrec), padx=90, pady=20,bg='light blue')
        BACK_BUTTON.grid(row=4, columnspan=3)#BACK BUTTON

        hangrec.mainloop()
def TICTACTOE_RECORDS():
        ticrec=Tk()
        ticrec.title('TIC-TAC-TOE RECORDS')
        ticrec.iconbitmap(path+'\\IMAGES\\favicon.ico')
        LB3=Listbox(ticrec, width = 30, bg = 'azure')
        LB1=Listbox(ticrec, width = 30, bg = 'azure')
        LB2=Listbox(ticrec, width = 30, bg = 'azure')
        LB=Listbox(ticrec, width = 30, bg = 'azure')
        try:
                with open('TICTACTOE_RECORDS.csv','r') as D1:
                        r=csv.DictReader(D1)
                        ini=1
                        for row in r:
                                LB1.insert(ini,'                      '+row['PLAYER 1'])
                                LB3.insert(ini,'                 '+row['STATUS'])
                                LB2.insert(ini,'                      '+row['PLAYER 2'])
                                LB.insert(ini,'                      '+row['GAME CODE'])
                                ini=ini+1
                        if(ini==1):
                                LB.insert(1,"NO       ")
                                LB1.insert(1,"RECORDS         ")
                                LB2.insert(1,"FOUND          ")
                                LB3.insert(1,"!!!           ")
        except:
                LB.insert(1,"NO       ")
                LB1.insert(1,"RECORDS         ")
                LB2.insert(1,"FOUND          ")
                LB3.insert(1,"!!!           ")
        LABEL=Label(ticrec,text='GAME CODE').grid(row=1,column=0)
        LABEL=Label(ticrec,text='STATUS').grid(row=1,column=3)
        LABEL=Label(ticrec,text='PLAYER 1').grid(row=1,column=1)
        LABEL=Label(ticrec,text='PLAYER 2').grid(row=1,column=2)
        LB1.grid(row=2,column=1)
        LB3.grid(row=2,column=3)
        LB2.grid(row=2,column=2)
        LB.grid(row=2,column=0)
        LABEL=Label(ticrec,text="""TIC-TAC-TOE RECORDS""",font=('Elephant',20),fg='red').grid(row=0,columnspan=4)
        LABEL=Label(ticrec,text="",font=('Elephant',20)).grid(row=3,columnspan=4)
        BACK_BUTTON=Button(ticrec,text="BACK TO THE LEADERBOARD MENU",command= lambda:SCREEN_EXIT(ticrec), padx=270, pady=20,bg='light blue')
        BACK_BUTTON.grid(row=4, columnspan=4)#BACK BUTTON

        ticrec.mainloop()
def TYPEMASTER_RECORDS():
        typerec=Tk()
        typerec.title('TYPEMASTER RECORDS')
        typerec.iconbitmap(path+'\\IMAGES\\favicon.ico')
        LB4=Listbox(typerec, width = 30, bg = 'azure')
        LB3=Listbox(typerec, width = 30, bg = 'azure')
        LB1=Listbox(typerec, width = 30, bg = 'azure')
        LB2=Listbox(typerec, width = 30, bg = 'azure')
        LB=Listbox(typerec, width = 30, bg = 'azure')
        try:
                with open('TYPEMASTER_RECORDS.csv','r') as D1:
                        r=csv.DictReader(D1)
                        ini=1
                        for row in r:
                                LB1.insert(ini,'                   '+row['LEVEL'])
                                LB3.insert(ini,'                            '+row['ERRORS'])
                                LB2.insert(ini,'                          '+row['AVERAGE TIME'])
                                LB.insert(ini,'                         '+row['NAME'])
                                LB4.insert(ini,'                           '+row['POINTS'])
                                ini=ini+1
                        if(ini==1):
                                LB1.insert(1,"NO       ")
                                LB2.insert(1,"REOCRDS         ")
                                LB3.insert(1,"FOUND          ")
                                LB4.insert(1,"!!!           ")
                                LB.insert(1,"!!!")
        except:
                LB1.insert(1,"NO       ")
                LB2.insert(1,"REOCRDS         ")
                LB3.insert(1,"FOUND          ")
                LB4.insert(1,"!!!           ")
                LB.insert(1,"!!!")
        LABEL=Label(typerec,text='NAME').grid(row=1,column=0)
        LABEL=Label(typerec,text='ERRORS').grid(row=1,column=3)
        LABEL=Label(typerec,text='LEVEL').grid(row=1,column=1)
        LABEL=Label(typerec,text='AVERAGE TIME').grid(row=1,column=2)
        LABEL=Label(typerec,text='POINTS').grid(row=1,column=4)
        LB1.grid(row=2,column=1)
        LB3.grid(row=2,column=3)
        LB2.grid(row=2,column=2)
        LB.grid(row=2,column=0)
        LB4.grid(row=2,column=4)
        LABEL=Label(typerec,text="""TYPEMASTER RECORDS""",font=('Elephant',20),fg='red').grid(row=0,columnspan=5)
        LABEL=Label(typerec,text="",font=('Elephant',20)).grid(row=3,columnspan=5)
        BACK_BUTTON=Button(typerec,text="BACK TO THE LEADERBOARD MENU",command= lambda:SCREEN_EXIT(typerec), padx=370, pady=20,bg='light blue')
        BACK_BUTTON.grid(row=4, columnspan=5)#BACK BUTTON

        typerec.mainloop()
def VOACABQUIZ_RECORDS():
        VOCABrec=Tk()
        VOCABrec.title('VOCABULARY QUIZ RECORDS')
        VOCABrec.iconbitmap(path+'\\IMAGES\\favicon.ico')
        LB1=Listbox(VOCABrec, width = 30, bg = 'azure')
        LB2=Listbox(VOCABrec, width = 30, bg = 'azure')
        LB=Listbox(VOCABrec, width = 30, bg = 'azure')
        try:
                with open('VQUIZ_RECORDS.csv','r') as D1:
                        r=csv.DictReader(D1)
                        ini=1
                        for row in r:
                                LB1.insert(ini,'                         '+row['Mains Level'])
                                LB2.insert(ini,'                    '+row['Advance Level'])
                                LB.insert(ini,'                    '+row['NAME'])
                                ini=ini+1
                        if(ini==1):
                                LB.insert(1,"NO       ")
                                LB1.insert(1,"REOCRDS         ")
                                LB2.insert(1,"FOUND          ")
        except:
                LB.insert(1,"NO       ")
                LB1.insert(1,"REOCRDS         ")
                LB2.insert(1,"FOUND          ")
        LABEL=Label(VOCABrec,text='NAME').grid(row=1,column=0) 
        LABEL=Label(VOCABrec,text='Mains Level').grid(row=1,column=1)
        LABEL=Label(VOCABrec,text='Advance Level').grid(row=1,column=2)
        LB1.grid(row=2,column=1)
        LB2.grid(row=2,column=2)
        LB.grid(row=2,column=0)
        LABEL=Label(VOCABrec,text="""VOCABULARY QUIZ RECORDS""",font=('Elephant',20),fg='red').grid(row=0,columnspan=5)
        LABEL=Label(VOCABrec,text="",font=('Elephant',20)).grid(row=3,columnspan=5)
        BACK_BUTTON=Button(VOCABrec,text="BACK TO THE LEADERBOARD MENU",command= lambda:SCREEN_EXIT(VOCABrec), padx=180, pady=20,bg='light blue')
        BACK_BUTTON.grid(row=4, columnspan=5)#BACK BUTTON

        VOCABrec.mainloop()
#=======================================================================================================================================
#=======================================================================================================================================
#LOGIN BUTTON AND ALL ITS FUNTIONS 
#=======================================================================================================================================
#=======================================================================================================================================
def LOGIN_SCREEN():
        LOGIN=Tk()
        LOGIN.title('LOGIN')
        LOGIN.iconbitmap(path+'\\IMAGES\\favicon.ico')

        USERNAME_ASK=Label(LOGIN,text="Enter User Name :").grid(row=0,column=0)
        PASSWORD_ASK=Label(LOGIN,text="Enter Password :").grid(row=1,column=0)
        Data_UserNameEnterStore=StringVar()
        Data_PasswordEnterStore=StringVar()
        Data_UserNameEnter=Entry(LOGIN,width=50,textvariable=Data_UserNameEnterStore)
        Data_UserNameEnter.grid(row=0,column=1,columnspan=1,padx=50)
        Data_PasswordEnter=Entry(LOGIN,show="*",width=50,textvariable=Data_PasswordEnterStore)
        Data_PasswordEnter.grid(row=1,column=1,columnspan=1,padx=50)
        def LOGIN_FUNCTION():
                USERNAMEinput=Data_UserNameEnter.get()
                PASSWORDinput=Data_PasswordEnter.get()
                if(USERNAMEinput in USERNAME and PASSWORDinput in PASSWORD):
                        LOGIN.destroy()
                        AFTER_LOGIN()
                else:
                        label=Label(LOGIN,text="incorrect password or username",fg='red')
                        label.grid(row=2,column=0)
                print(USERNAMEinput,PASSWORDinput)

        
        LOGINBUTTON=Button(LOGIN,text="LOGIN",command=LOGIN_FUNCTION,fg='blue')
        LOGINBUTTON.grid(row=2,column=1)
        LOGIN.mainloop()
        
def AFTER_LOGIN():
        MAIN_SCREEN1=Tk()
        MAIN_SCREEN1.geometry('400x540')
        MAIN_SCREEN1.minsize(400,540)
        MAIN_SCREEN1.maxsize(400,540)
        MAIN_SCREEN1.title('SERVER')
        MAIN_SCREEN1.iconbitmap(path+"\\IMAGES\\favicon.ico")
        

        label=Label(MAIN_SCREEN1, text="",pady=50)
        label.pack() 
        HEADING=Button(MAIN_SCREEN1,text="|LEADERBOARD MAINTAINANCE|",font=('Product Sans',18),fg = 'white',bg='#ffa36c', padx=73.5, pady=20)
        HEADING.place(relx = 0.5, anchor='n')
        
        
        label2=Label(MAIN_SCREEN1,text="=============================================================",pady=10)
        label2.pack()
        
        #BUTTONS
        modify=Button(MAIN_SCREEN1,text="MODIFICATION",command=modifying, padx=130, pady=20,bg='#91d18b', fg="white")
        modify.pack()
        label=Label(MAIN_SCREEN1, text="            ")
        label.pack()
        delete=Button(MAIN_SCREEN1,text="DELETE ALL RECORDS",command=deleteall, padx=115,pady=20,bg='#91d18b', fg="white")
        delete.pack()
        label=Label(MAIN_SCREEN1, text="            ")
        label.pack()
        delete2=Button(MAIN_SCREEN1,text="DELETE SPECIFIC RECORDS",command=delspc, padx=101.5 , pady=20, bg='#91d18b', fg="white")
        delete2.pack()
        label=Label(MAIN_SCREEN1, text="            ", pady=30)
        label.pack()
        EXIT=Button(MAIN_SCREEN1,text="back",pady=20, command=lambda:SCREEN_EXIT(MAIN_SCREEN1),bg='light blue',padx=180)
        EXIT.pack()
        


        MAIN_SCREEN1.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------
#MODIFYING A RECORD
def modifying():
        ms=Tk()
        ms.title('MODIFY A RECORD')
        ms.iconbitmap(path+"\\IMAGES\\favicon.ico")
        
        LABEL=Label(ms,text="""MODIFY A RECORD""",font=('Elephant',20),fg='red').grid(row=0,columnspan=2)
        label=Label(ms,text="Which game's record do you wish to edit: ")
        label.grid(row=1,column=0)
        choices=["HANGMAN","VOCAB QUIZ","TIC TAC TOE","TYPE MASTER"]
        mkvar = StringVar(ms)
        popupMenu = OptionMenu(ms, mkvar, *choices)
        popupMenu.grid(row=1,column=1)


        def okie(ms):
                options1=[]
                if(mkvar.get()=="HANGMAN"):
                        ini=1
                        try:
                                with open('HANGMAN_RECORDS.csv','r') as C1:
                                        r=csv.DictReader(C1)
                                        lmn=1
                                        for row in r:
                                                options1.append(str(str(lmn)+' .   '+row['NAME']+'   :   '+row['SCORE']))
                                                lmn=lmn+1
                                        if(lmn==1):
                                                options1.append("NO RECORDS FOUND !") 
                        except:
                                options1.append("NO RECORDS FOUND !")
                        pkvar=StringVar(ms)
                        popmenu=OptionMenu(ms, pkvar,  *options1)
                        popmenu.grid(row=3,column=1)
                        label=Label(ms, text="Which record do you want to edit :").grid(row=3,column=0)
                        def lk(ms):
                                fields=["NAME","SCORE"]
                                ikvar=StringVar(ms)
                                f=Label(ms,text="Whcih field do you wish to edit: ").grid(row=5,column=0)
                                popmenu1=OptionMenu(ms,ikvar, *fields).grid(row=5,column=1)
                                def qwe(ms):
                                        label=Label(ms,text="NEW "+ ikvar.get()+" :").grid(row=7,column=0)
                                        okvar=StringVar(ms)
                                        change=Entry(ms,width=50,textvariable=okvar).grid(row=7,column=1)
                                        def poo(ms):
                                                TEMP=[]
                                                try:    
                                                        with open('HANGMAN_RECORDS.csv','r') as C1:
                                                                r=csv.DictReader(C1)
                                                                for row in r:
                                                                        TEMP.append(row)
                                                        C1=open('HANGMAN_RECORDS.csv','w')
                                                        colheadings=['NAME','SCORE']
                                                        r=csv.DictWriter(C1,fieldnames=colheadings)
                                                        r.writeheader()
                                                        C1.close
                                                        for i in pkvar.get():
                                                                if(i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0'):
                                                                        lmn=int(i)
                                                                        break
                                                        abc=1
                                                        for i in TEMP:
                                                                if(lmn != abc):
                                                                        with open('HANGMAN_RECORDS.csv','a+'):
                                                                                colheadings=['NAME','SCORE']
                                                                                r=csv.DictWriter(C1,fieldnames=colheadings)
                                                                                r.writerow(i)
                                                                else:                                                               
                                                                        i[ikvar.get()]=okvar.get()        
                                                                        with open('HANGMAN_RECORDS.csv','a+'):
                                                                                colheadings=['NAME','SCORE']
                                                                                r=csv.DictWriter(C1,fieldnames=colheadings)
                                                                                r.writerow(i)                                                                                                                                              
                                                                abc=abc+1
                                                        
                                                except:
                                                        print()
                                                ms.destroy()        
                                               
                                        op=Button(ms, text="CONFIRM CHANGE",command=lambda:poo(ms)).grid(row=8,columnspan=2)
                                g=Button(ms,text="SELECT",command=lambda:qwe(ms)).grid(row=6,columnspan=2)
                                
                                
                        go=Button(ms,text="SELECT",command=lambda:lk(ms))
                        go.grid(row=4, columnspan=2)
                elif(mkvar.get()=="VOCAB QUIZ"):
                        ini=1
                        try:
                                with open('VQUIZ_RECORDS.csv','r') as C1:
                                        r=csv.DictReader(C1)
                                        lmn=1
                                        for row in r:
                                                options1.append(str(str(lmn)+' .   '+row['NAME']+'   :   '+str(row['Mains Level'])+'   :   '+str(row['Advance Level'])))
                                                lmn=lmn+1
                                        if(lmn==1):
                                                options1.append("NO RECORDS FOUND !") 
                        except:
                                options1.append("NO RECORDS FOUND !")
                        pkvar=StringVar(ms)
                        popmenu=OptionMenu(ms, pkvar,  *options1)
                        popmenu.grid(row=3,column=1)
                        label=Label(ms, text="Which record do you want to edit :").grid(row=3,column=0)
                        def lk(ms):
                                fields=["NAME","Mains Level","Advance Level"]
                                ikvar=StringVar(ms)
                                f=Label(ms,text="Whcih field do you wish to edit: ").grid(row=5,column=0)
                                popmenu1=OptionMenu(ms,ikvar, *fields).grid(row=5,column=1)
                                def qwe(ms):
                                        label=Label(ms,text="NEW "+ ikvar.get()+" :").grid(row=7,column=0)
                                        okvar=StringVar(ms)
                                        change=Entry(ms,width=50,textvariable=okvar).grid(row=7,column=1)
                                        def poo(ms):
                                                TEMP=[]
                                                try:    
                                                        with open('VQUIZ_RECORDS.csv','r') as C1:
                                                                r=csv.DictReader(C1)
                                                                for row in r:
                                                                        TEMP.append(row)
                                                        C1=open('VQUIZ_RECORDS.csv','w')
                                                        colheadings=['NAME','Mains Level',"Advance Level"]
                                                        r=csv.DictWriter(C1,fieldnames=colheadings)
                                                        r.writeheader()
                                                        C1.close
                                                        for i in pkvar.get():
                                                                if(i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0'):
                                                                        lmn=int(i)
                                                                        break
                                                        abc=1
                                                        for i in TEMP:
                                                                if(lmn != abc):
                                                                        with open('VQUIZ_RECORDS.csv','a+'):
                                                                                colheadings=['NAME','Mains Level',"Advance Level"]
                                                                                r=csv.DictWriter(C1,fieldnames=colheadings)
                                                                                r.writerow(i)
                                                                else:                                                               
                                                                        i[ikvar.get()]=okvar.get()        
                                                                        with open('VQUIZ_RECORDS.csv','a+'):
                                                                                colheadings=['NAME','Mains Level',"Advance Level"]
                                                                                r=csv.DictWriter(C1,fieldnames=colheadings)
                                                                                r.writerow(i)                                                                                                                                              
                                                                abc=abc+1
                                                        
                                                except:
                                                        print()
                                                ms.destroy()        
                                               
                                        op=Button(ms, text="CONFIRM CHANGE",command=lambda:poo(ms)).grid(row=8,columnspan=2)
                                g=Button(ms,text="SELECT",command=lambda:qwe(ms)).grid(row=6,columnspan=2)
                                
                                
                        go=Button(ms,text="SELECT",command=lambda:lk(ms))
                        go.grid(row=4, columnspan=2)
                elif(mkvar.get()=="TIC TAC TOE"):
                        ini=1
                        try:
                                with open('TICTACTOE_RECORDS.csv','r') as C1:
                                        r=csv.DictReader(C1)
                                        lmn=1
                                        for row in r:
                                                options1.append(str(str(lmn)+' .   '+row['GAME CODE']+'   :   '+str(row['PLAYER 1'])+'   :   '+str(row['PLAYER 2'])+'   :   '+row['STATUS']))
                                                lmn=lmn+1
                                        if(lmn==1):
                                                options1.append("NO RECORDS FOUND !") 
                        except:
                                options1.append("NO RECORDS FOUND !")
                        pkvar=StringVar(ms)
                        popmenu=OptionMenu(ms, pkvar,  *options1)
                        popmenu.grid(row=3,column=1)
                        label=Label(ms, text="Which record do you want to edit :").grid(row=3,column=0)
                        def lk(ms):
                                fields=["GAME CODE","STATUS"]
                                ikvar=StringVar(ms)
                                f=Label(ms,text="Whcih field do you wish to edit: ").grid(row=5,column=0)
                                popmenu1=OptionMenu(ms,ikvar, *fields).grid(row=5,column=1)
                                def qwe(ms):
                                        label=Label(ms,text="NEW "+ ikvar.get()+" :").grid(row=7,column=0)
                                        okvar=StringVar(ms)
                                        change=Entry(ms,width=50,textvariable=okvar).grid(row=7,column=1)
                                        def poo(ms):
                                                TEMP=[]
                                                try:    
                                                        with open('TICTACTOE_RECORDS.csv','r') as C1:
                                                                r=csv.DictReader(C1)
                                                                for row in r:
                                                                        TEMP.append(row)
                                                        C1=open('TICTACTOE_RECORDS.csv','w')
                                                        colheadings=["GAME CODE","PLAYER 1","PLAYER 2","STATUS"]
                                                        r=csv.DictWriter(C1,fieldnames=colheadings)
                                                        r.writeheader()
                                                        C1.close
                                                        for i in pkvar.get():
                                                                if(i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0'):
                                                                        lmn=int(i)
                                                                        break
                                                        abc=1
                                                        for i in TEMP:
                                                                if(lmn != abc):
                                                                        with open('TICTACTOE_RECORDS.csv','a+'):
                                                                                colheadings=["GAME CODE","PLAYER 1","PLAYER 2","STATUS"]
                                                                                r=csv.DictWriter(C1,fieldnames=colheadings)
                                                                                r.writerow(i)
                                                                else:                                                               
                                                                        i[ikvar.get()]=okvar.get()        
                                                                        with open('TICTACTOE_RECORDS.csv','a+'):
                                                                                colheadings=["GAME CODE","PLAYER 1","PLAYER 2","STATUS"]
                                                                                r=csv.DictWriter(C1,fieldnames=colheadings)
                                                                                r.writerow(i)                                                                                                                                              
                                                                abc=abc+1
                                                        
                                                except:
                                                        print()
                                                ms.destroy()        
                                               
                                        op=Button(ms, text="CONFIRM CHANGE",command=lambda:poo(ms)).grid(row=8,columnspan=2)
                                g=Button(ms,text="SELECT",command=lambda:qwe(ms)).grid(row=6,columnspan=2)
                                
                                
                        go=Button(ms,text="SELECT",command=lambda:lk(ms))
                        go.grid(row=4, columnspan=2)
                elif(mkvar.get()=="TYPE MASTER"):
                        ini=1
                        try:
                                with open('TYPEMASTER_RECORDS.csv','r') as C1:
                                        r=csv.DictReader(C1)
                                        lmn=1
                                        for row in r:
                                                options1.append(str(str(lmn)+' .   '+row['NAME']+'   :   '+str(row['LEVEL'])+'   :   '+str(row['AVERAGE TIME'])+'   :   '+str(row['ERRORS'])+'   :   '+str(row['POINTS'])))
                                                lmn=lmn+1
                                        if(lmn==1):
                                                options1.append("NO RECORDS FOUND !") 
                        except:
                                options1.append("NO RECORDS FOUND !")
                        pkvar=StringVar(ms)
                        popmenu=OptionMenu(ms, pkvar,  *options1)
                        popmenu.grid(row=3,column=1)
                        label=Label(ms, text="Which record do you want to edit :").grid(row=3,column=0)
                        def lk(ms):
                                fields=["NAME","AVERAGE TIME",'ERRORS',"POINTS"]
                                ikvar=StringVar(ms)
                                f=Label(ms,text="Whcih field do you wish to edit: ").grid(row=5,column=0)
                                popmenu1=OptionMenu(ms,ikvar, *fields).grid(row=5,column=1)
                                def qwe(ms):
                                        label=Label(ms,text="NEW "+ ikvar.get()+" :").grid(row=7,column=0)
                                        okvar=StringVar(ms)
                                        change=Entry(ms,width=50,textvariable=okvar).grid(row=7,column=1)
                                        def poo(ms):
                                                TEMP=[]
                                                try:    
                                                        with open('TYPEMASTER_RECORDS.csv','r') as C1:
                                                                r=csv.DictReader(C1)
                                                                for row in r:
                                                                        TEMP.append(row)
                                                        C1=open('TYPEMASTER_RECORDS.csv','w')
                                                        colheadings=["NAME","LEVEL","AVERAGE TIME",'ERRORS',"POINTS"]
                                                        r=csv.DictWriter(C1,fieldnames=colheadings)
                                                        r.writeheader()
                                                        C1.close
                                                        for i in pkvar.get():
                                                                if(i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0'):
                                                                        lmn=int(i)
                                                                        break
                                                        abc=1
                                                        for i in TEMP:
                                                                if(lmn != abc):
                                                                        with open('TYPEMASTER_RECORDS.csv','a+'):
                                                                                colheadings=["NAME","LEVEL","AVERAGE TIME",'ERRORS',"POINTS"]
                                                                                r=csv.DictWriter(C1,fieldnames=colheadings)
                                                                                r.writerow(i)
                                                                else:                                                               
                                                                        i[ikvar.get()]=okvar.get()        
                                                                        with open('TYPEMASTER_RECORDS.csv','a+'):
                                                                                colheadings=["NAME","LEVEL","AVERAGE TIME",'ERRORS',"POINTS"]
                                                                                r=csv.DictWriter(C1,fieldnames=colheadings)
                                                                                r.writerow(i)                                                                                                                                              
                                                                abc=abc+1
                                                        
                                                except:
                                                        print()
                                                ms.destroy()        
                                               
                                        op=Button(ms, text="CONFIRM CHANGE",command=lambda:poo(ms)).grid(row=8,columnspan=2)
                                g=Button(ms,text="SELECT",command=lambda:qwe(ms)).grid(row=6,columnspan=2)
                                
                                
                        go=Button(ms,text="SELECT",command=lambda:lk(ms))
                        go.grid(row=4, columnspan=2)        
        confirm=Button(ms,text="CONFIRM",command=lambda:okie(ms))
        confirm.grid(row=2,columnspan=2)
        ms.mainloop()
#---------------------------------------------------------------------------------------------------------------------------
#DELETING COMPLETE RECORDS OF A GAME 
def deleteall():
        delete=Tk()
        delete.title("Delete all records")
        delete.iconbitmap(path+"\\IMAGES\\favicon.ico")

        LABEL=Label(delete,text="""DELETE ALL RECORDS""",font=('Elephant',20),fg='red').grid(row=0,columnspan=2)
        label=Label(delete,text="Which records do you wish to delete: ")
        label.grid(row=1,column=0)
        choices=["HANGMAN","VOCAB QUIZ","TIC TAC TOE","TYPE MASTER"]
        tkvar = StringVar(delete)
        popupMenu = OptionMenu(delete, tkvar, *choices)
        popupMenu.grid(row=1,column=1)


        def ok(delete):
                try:
                        if(tkvar.get()=="HANGMAN"):
                                os.remove('HANGMAN_RECORDS.csv')
                        elif(tkvar.get()=="VOCAB QUIZ"):
                                os.remove('VQUIZ_RECORDS.csv')
                        elif(tkvar.get()=="TIC TAC TOE"):
                                os.remove('TICTACTOE_RECORDS.csv')
                        elif(tkvar.get()=="TYPE MASTER"):
                                os.remove('TYPEMASTER_RECORDS.csv')        
                except:
                        print()
                delete.destroy()


        confirm=Button(delete,text="CONFIRM",command=lambda:ok(delete))
        confirm.grid(row=2,columnspan=2)

        delete.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------
#DELETE A SINGLE RECORD OF A GAME !!!
def delspc():
        delspc=Tk()
        delspc.title('Delete specific records')
        delspc.iconbitmap(path+"\\IMAGES\\favicon.ico")

        LABEL=Label(delspc,text="""DELETE SPECIFIC RECORDS""",font=('Elephant',20),fg='red').grid(row=0,columnspan=2)
        label=Label(delspc,text="Which game's record do you wish to delete: ")
        label.grid(row=1,column=0)
        choices=["HANGMAN","VOCAB QUIZ","TIC TAC TOE","TYPE MASTER"]
        tkvar = StringVar(delspc)
        popupMenu = OptionMenu(delspc, tkvar, *choices)
        popupMenu.grid(row=1,column=1)

        def OK1(delspc):
                options=[]
                if(tkvar.get()=="HANGMAN"):
                        ini=1
                        try:
                                with open('HANGMAN_RECORDS.csv','r') as C1:
                                        r=csv.DictReader(C1)
                                        lmn=1
                                        for row in r:
                                                options.append(str(str(lmn)+' .   '+row['NAME']+'   :   '+row['SCORE']))
                                                lmn=lmn+1
                                        if(lmn==1):
                                                options.append("NO RECORDS FOUND !") 
                        except:
                                options.append("NO RECORDS FOUND !")
                        vkvar=StringVar(delspc)
                        popmenu=OptionMenu(delspc, vkvar,  *options)
                        popmenu.grid(row=3,column=1)
                        label=Label(delspc, text="Which record do you want to delete :").grid(row=3,column=0)

                        
                        def confirmn(delspc):
                                TEMP=[]
                                try:    
                                        with open('HANGMAN_RECORDS.csv','r') as C1:
                                                r=csv.DictReader(C1)
                                                for row in r:
                                                        TEMP.append(row)
                                        C1=open('HANGMAN_RECORDS.csv','w')
                                        colheadings=['NAME','SCORE']
                                        r=csv.DictWriter(C1,fieldnames=colheadings)
                                        r.writeheader()
                                        C1.close
                                        NOM = vkvar.get()
                                        for i in NOM:
                                                if(i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0'):
                                                        lmn=int(i)
                                                        break
                                        abc=1
                                        for i in TEMP:
                                                if(lmn != abc):
                                                        with open('HANGMAN_RECORDS.csv','a+'):
                                                                colheadings=['NAME','SCORE']
                                                                r=csv.DictWriter(C1,fieldnames=colheadings)
                                                                r.writerow(i)
                                                abc=abc+1
                                except:
                                        print()
                                delspc.destroy()
                        confirmnm=Button(delspc, text="CONFIRM",command=lambda: confirmn(delspc))
                        confirmnm.grid(row=4,columnspan=2)

                        
                elif(tkvar.get()=="VOCAB QUIZ"):
                        ini=1
                        try:
                                with open('VQUIZ_RECORDS.csv','r') as C1:
                                        r=csv.DictReader(C1)
                                        lmn=1
                                        for row in r:
                                                options.append(str(str(lmn)+' .   '+row['NAME']+'   :   '+str(row['Mains Level'])+'   :   '+str(row['Advance Level'])))
                                                lmn=lmn+1
                                        if(lmn==1):
                                                options.append("NO RECORDS FOUND !") 
                        except:
                                options.append("NO RECORDS FOUND !")
                        vkvar=StringVar(delspc)
                        popmenu=OptionMenu(delspc, vkvar,  *options)
                        popmenu.grid(row=3,column=1)
                        label=Label(delspc, text="Which record do you want to delete :").grid(row=3,column=0)

                        
                        def confirmn(delspc):
                                TEMP=[]
                                try:    
                                        with open('VQUIZ_RECORDS.csv','r') as C1:
                                                r=csv.DictReader(C1)
                                                for row in r:
                                                        TEMP.append(row)
                                        C1=open('VQUIZ_RECORDS.csv','w')
                                        colheadings=['NAME','Mains Level','Advance Level']
                                        r=csv.DictWriter(C1,fieldnames=colheadings)
                                        r.writeheader()
                                        C1.close
                                        NOM = vkvar.get()
                                        for i in NOM:
                                                if(i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0'):
                                                        lmn=int(i)
                                                        break
                                        abc=1
                                        for i in TEMP:
                                                if(lmn != abc):
                                                        with open('VQUIZ_RECORDS.csv','a+'):
                                                                colheadings=['NAME','Mains Level','Advance Level']
                                                                r=csv.DictWriter(C1,fieldnames=colheadings)
                                                                r.writerow(i)
                                                abc=abc+1
                                except:
                                        print()
                                delspc.destroy()
                        confirmnm=Button(delspc, text="CONFIRM",command=lambda: confirmn(delspc))
                        confirmnm.grid(row=4,columnspan=2)

                        
                elif(tkvar.get()=="TIC TAC TOE"):
                        ini=1
                        try:
                                with open('TICTACTOE_RECORDS.csv','r') as C1:
                                        r=csv.DictReader(C1)
                                        lmn=1
                                        for row in r:
                                                options.append(str(str(lmn)+' .   '+row['GAME CODE']+'   :   '+str(row['PLAYER 1'])+'   :   '+str(row['PLAYER 2'])+'   :   '+row['STATUS']))
                                                lmn=lmn+1
                                        if(lmn==1):
                                                options.append("NO RECORDS FOUND !") 
                        except:
                                options.append("NO RECORDS FOUND !")
                        vkvar=StringVar(delspc)
                        popmenu=OptionMenu(delspc, vkvar,  *options)
                        popmenu.grid(row=3,column=1)
                        label=Label(delspc, text="Which record do you want to delete :").grid(row=3,column=0)

                        
                        def confirmn(delspc):
                                TEMP=[]
                                try:    
                                        with open('TICTACTOE_RECORDS.csv','r') as C1:
                                                r=csv.DictReader(C1)
                                                for row in r:
                                                        TEMP.append(row)
                                        C1=open('TICTACTOE_RECORDS.csv','w')
                                        colheadings=['GAME CODE','PLAYER 1','PLAYER 2','STATUS']
                                        r=csv.DictWriter(C1,fieldnames=colheadings)
                                        r.writeheader()
                                        C1.close
                                        NOM = vkvar.get()
                                        for i in NOM:
                                                if(i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0'):
                                                        lmn=int(i)
                                                        break
                                        abc=1
                                        for i in TEMP:
                                                if(lmn != abc):
                                                        with open('TICTACTOE_RECORDS.csv','a+'):
                                                                colheadings=['GAME CODE','PLAYER 1','PLAYER 2','STATUS']
                                                                r=csv.DictWriter(C1,fieldnames=colheadings)
                                                                r.writerow(i)
                                                abc=abc+1
                                except:
                                        print()
                                delspc.destroy()
                        confirmnm=Button(delspc, text="CONFIRM",command=lambda: confirmn(delspc))
                        confirmnm.grid(row=4,columnspan=2)

                        
                elif(tkvar.get()=="TYPE MASTER"):
                        ini=1
                        try:
                                with open("TYPEMASTER_RECORDS.csv",'r') as C1:
                                        r=csv.DictReader(C1)
                                        lmn=1
                                        for row in r:
                                                options.append(str(str(lmn)+' .   '+row['NAME']+'   :   '+str(row['LEVEL'])+'   :   '+str(row['AVERAGE TIME'])+'   :   '+str(row['ERRORS'])+'   :   '+str(row['POINTS'])))
                                                lmn=lmn+1
                                        if(lmn==1):
                                                options.append("NO RECORDS FOUND !") 
                        except:
                                options.append("NO RECORDS FOUND !")
                        vkvar=StringVar(delspc)
                        popmenu=OptionMenu(delspc, vkvar,  *options)
                        popmenu.grid(row=3,column=1)
                        label=Label(delspc, text="Which record do you want to delete :").grid(row=3,column=0)

                        
                        def confirmn(delspc):
                                TEMP=[]
                                try:    
                                        with open("TYPEMASTER_RECORDS.csv",'r') as C1:
                                                r=csv.DictReader(C1)
                                                for row in r:
                                                        TEMP.append(row)
                                        C1=open("TYPEMASTER_RECORDS.csv",'w')
                                        colheadings=['NAME','LEVEL','AVERAGE TIME','ERRORS','POINTS']
                                        r=csv.DictWriter(C1,fieldnames=colheadings)
                                        r.writeheader()
                                        C1.close
                                        NOM = vkvar.get()
                                        for i in NOM:
                                                if(i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0'):
                                                        lmn=int(i)
                                                        break
                                        abc=1
                                        for i in TEMP:
                                                if(lmn != abc):
                                                        with open("TYPEMASTER_RECORDS.csv",'a+'):
                                                                colheadings=['NAME','LEVEL','AVERAGE TIME','ERRORS','POINTS']
                                                                r=csv.DictWriter(C1,fieldnames=colheadings)
                                                                r.writerow(i)
                                                abc=abc+1
                                except:
                                        print()
                                delspc.destroy()
                        confirmnm=Button(delspc, text="CONFIRM",command=lambda: confirmn(delspc))
                        confirmnm.grid(row=4,columnspan=2)
                                                
        confirm=Button(delspc, text="SELECT",command=lambda :OK1(delspc))
        confirm.grid(row=2,columnspan=2)

        delspc.mainloop()


#=======================================================================================================================================
#=======================================================================================================================================
#ABOUT SCREEN
#=======================================================================================================================================
#=======================================================================================================================================
def ABOUT_SCREEN():
        ABOUT_SCREEN=Tk()
        ABOUT_SCREEN.geometry('440x489')
        ABOUT_SCREEN.minsize(440,489)
        ABOUT_SCREEN.maxsize(440,489)
        ABOUT_SCREEN.title('About...')
        ABOUT_SCREEN.iconbitmap(path+'\\IMAGES\\favicon.ico')

        label=Label(ABOUT_SCREEN, text="            ",pady=50)
        label.pack()#label for better placing 


        HEADING=Button(ABOUT_SCREEN,text=" |  A   B   O   U   T  | ",font=('Elephant',20),fg = 'white',bg='#91d18b', padx=93.5, pady=40)
        HEADING.place(relx = 0.5, anchor='n')

        info=Label(ABOUT_SCREEN,fg='white',bg='#00796b',padx=400,text='''CREATORS:

NAME      :      VANSH JAGGI


CLASS     :      XII-A

SESSION   :      2020-21''',pady=90)
        info.pack()

        EXIT=Button(ABOUT_SCREEN,text="BACK TO THE MAIN MENU",bg='light blue',command=lambda:SCREEN_EXIT(ABOUT_SCREEN), pady=20,padx=145)
        EXIT.pack()
        

        ABOUT_SCREEN.mainloop()
        



#MAIN SCREEN------

MAIN_SCREEN=Tk()
MAIN_SCREEN.geometry('457x530')
MAIN_SCREEN.minsize(457,530)
MAIN_SCREEN.maxsize(457,530)
MAIN_SCREEN.title('BRAIN JAM')
MAIN_SCREEN.iconbitmap(path+"\\IMAGES\\favicon.ico")


label=Label(MAIN_SCREEN, text="",pady=40)
label.grid(row=0,column=0)#label for better placing 

photo1 = PhotoImage(file = path+"\\IMAGES\\bj3.gif")#IMAGE LOADING !
gamemenuimage=Label(MAIN_SCREEN, image = photo1,padx=200) #CREATING LABEL WITH IMAGE
gamemenuimage.place(relx = 0.5, anchor='n')#Heading image use as label and packing !

label2=Label(MAIN_SCREEN,text="=============================================================",pady=10)
label2.grid(row=1,columnspan=5)

#BUTTONS
GAMEMENU=Button(MAIN_SCREEN,text="GAME MENU",font=("Product Sans",10),command=Call_GAMEMENU, padx=178, pady=20,bg='yellow')
GAMEMENU.grid(row=2,columnspan=2)
label=Label(MAIN_SCREEN, text="            ")
label.grid(row=3,column=0)#label for better placing 
LEADERBOARD=Button(MAIN_SCREEN,text="LEADERBOARD",font=("Product Sans",10),command=LEADERBOARD_SCREEN, padx=173,pady=20,bg='yellow')
LEADERBOARD.grid(row=4,columnspan=2)
label=Label(MAIN_SCREEN, text="            ")
label.grid(row=5,column=0)#label for better placing 
ABOUT=Button(MAIN_SCREEN,text="ABOUT...",command=ABOUT_SCREEN, padx=192 ,font=("Product Sans",10), pady=20, bg='yellow')
ABOUT.grid(row=6,columnspan=2)
label=Label(MAIN_SCREEN, text="            ", pady=30)
label.grid(row=7,column=0)#label for better placing
EXIT=Button(MAIN_SCREEN,text="EXIT",pady=20, command=lambda:SCREEN_EXIT(MAIN_SCREEN),bg='light blue',padx=90)
EXIT.grid(row=8,column=1)
LOGIN=Button(MAIN_SCREEN,text="LOGIN",command=LOGIN_SCREEN, bg='light blue',pady=20,padx=90)
LOGIN.grid(row=8,column=0)



MAIN_SCREEN.mainloop()

