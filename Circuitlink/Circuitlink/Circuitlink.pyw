from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import filedialog #this import the library needed to bring up the typical choose your file to open
import os #neccessary to open external programs, os stands for operating system so it lets you do operating system stuff
# import win32gui, win32con #imports neccessary libraries to hide console window
import pyautogui #(pip install pyautogui)
import subprocess # open external programs
from subprocess import Popen, PIPE
import time #allows make to make python program wait a set number of seconds
import shutil
import ctypes
import pygetwindow as gw






#subprocess.call(['C:/Program Files/AutoHotkey/AutoHotkey.exe', 'C:/Circuitlink/Script1.ahk']) #Call an autohotkey script
#hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(hide , win32con.SW_HIDE)

#out = os.popen('python --version').read()
#print(out)


#file as string from file dialog, then seperate .txt portion of string into its own variable then make custom string combining both and own words in its own variable, then replacing exisiting line in config file with new line.

configini = ("/%")
ftfile = "/%" #Set variable ftfile /% placeholder text
ftfilename = "/%"

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
Mbox('Important Message', 'Ensure C:/Circuitlink exists, ensure flashpro is in the folder and flashpro is using correct config.ini!', 1)


#def SetupWindow():
#    SetupWin = Tk()
#    #SetupWin = Toplevel(Main)
#    SetupWin.geometry("500x300")
    
#######################################################################################################    
def flashproconfig(): #replaces line with another line in text document
    progfile = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")]) # Retrict to a specific filetype square brackets are for readablility
    print(progfile)

    progname = progfile.split("/")
    print(progname)

    progname1 = progname[-1]
    progfile2 ="CodeFileName		txt   " + progname1 + "   " + progfile + "\n"
    print(progfile2)
    
    config1 = open("C:/Circuitlink/config.ini", 'r')
    configfile = config1.readlines()
    configfile[6] = progfile2 #specify line number and what to replace it with
    
    
    config1 = open("C:/Circuitlink/config.ini", 'w')
    config1.writelines(configfile)
    config1.close()
    label = Label(Main, text= progfile)
    label.place(x=0, y=435)
#######################################################################################################


#######################################################################################################
def ftprogconfig():
    global ftfile #uses the global ftfile variable, allowing me to use that variable again outside of this definition
    global ftfilename
    ftfile = filedialog.askopenfilename(filetypes=[("XML Files", "*.xml")])
    ftfilename2 = ftfile.split("/")
    ftfilename = ftfilename2[-1]
    label = Label(Main, text = ftfile)
    label.place(x=0, y=480)
#######################################################################################################
    

#progfile = openprogramfile
#def replaceconfig():
#    filein = open('C:/Users/matth/Documents/Circuitlink/7130013/test.txt', 'w')
#    for line in filein:
#        filein.write(line.replace(7 - 1, openprogramfile))

#    filein.close()



#class cmd():

#    def opencmd():
#    #c = subprocess.Popen('C:/Windows/System32/cmd.exe')
#    #os.system("start cmd")
#    os.popen('plink -serial com9')
    
#    out = os.popen('net use').read()
#    output = Text(Main, height=10, width = 10)
#    output.insert('end', out)
#    output.config(state='disabled')
#    output.place(x=100, y=250)
#    print(out)
#    os.popen('tb1')
#    time.sleep(1)

#    time.sleep(0.5)
#    #pyautogui.write('tb1')
#    #pyautogui.press('enter')
#    time.sleep(0.5)
#    #pyautogui.write('td')
#    #pyautogui.press('enter')
#    time.sleep(1)

#######################################################################################################
def opencmd():
    #c = subprocess.Popen('C:/Windows/System32/cmd.exe')
    #os.system("start cmd")
    #out = " "
    
    #Main.update_idletasks() # Refreshes screen to update any changes

    os.popen('plink -serial com9')
    out = os.popen('net user').readlines()[4] #specify which line to read
    output = Label(Main, text = out)
    output.place(x=100, y=250)
    print(out)
    os.popen('tb1')
    time.sleep(1)
    os.popen('td')
    time.sleep(0.5)
    #pyautogui.write('tb1')
    #pyautogui.press('enter')
    #time.sleep(0.5)
    #pyautogui.write('td')
    #pyautogui.press('enter')
    #time.sleep(1)
    #os.system("TASKKILL /F /IM cmd.exe")

#######################################################################################################
    #c.terminate()


#######################################################################################################
def programft():
    #print(ftfile)
    folder = 'C:/Circuitlink'
    isExist = os.path.exists(folder)
    if not isExist:
        os.makedirs(folder)
    folderxml = os.listdir(folder)
    xmlfiles = [file for file in folderxml if file.endswith(".xml")]
    for file in xmlfiles:
        filepath = os.path.join(folder, file)
        os.remove(filepath)
    target = r'C:/Circuitlink'
    shutil.copy2(ftfile, target)
    #f = subprocess.Popen('C:/Program Files (x86)/FTDI/FT_Prog/FT_Prog-CmdLine.exe')
    os.system("start cmd")
    #os.popen('cd C:/Program Files (x86)/FTDI/FT_Prog/')
    #os.popen('FT_Prog-CmdLine.exe')
    #Popen(["C:/Program Files (x86)/FTDI/FT_Prog/FT_Prog-CmdLine.exe"])
    #FT.stdin.write("prog 8".encode('utf-8'))
    #FT.stdin.close()
    time.sleep(1)
    pyautogui.write('cd C:/Program Files (x86)/FTDI/FT_Prog/')
    pyautogui.press('enter')
    time.sleep(.2)
    pyautogui.write('FT_Prog-CmdLine.exe')
    pyautogui.press('enter')
    time.sleep(.5)
    #ftprog = gw.getWindowsWithTitle('FT_Prog-CmdLine.exe')[0]
    #ftprog.activate()
    #os.popen('FT_Prog-CmdLine.exe')
    #time.sleep(0.2)
    #os.popen('prog * C/Circuitlink/' + ftfilename)
    time.sleep(0.2)
    pyautogui.write('prog * */Circuitlink/' + ftfilename)
    #os.popen('cycl *')
    pyautogui.press('enter')
    pyautogui.write('cycl *')
    pyautogui.press('enter')
    time.sleep(1)
    os.system("TASKKILL /F /IM FT_Prog-CmdLine.exe")
    os.system("TASKKILL /F /IM cmd.exe")
    #print(ftfile)
#######################################################################################################
    




#######################################################################################################
def programflashpro():
    p = subprocess.Popen('C:/Circuitlink/flashpro430.exe')
    time.sleep(3)
    subprocess.call(['C:/Program Files/AutoHotkey/AutoHotkey.exe', 'C:/Circuitlink/Script1.ahk'])
    time.sleep(5)
    # pyautogui.press('space')
    # time.sleep(2)
    # pyautogui.press('space')
    # time.sleep(3) # makes program wait 5 seconds before continueing (change 5 to howver many second you want)
    # pyautogui.press('F8') #sends key input F8
    # time.sleep(3)
    p.terminate()
#######################################################################################################





#######################################################################################################
def checkbox(): # checkbox if statements to determin what happens when checked and when not checked
    if (var1.get() == 1):
        partnumber.config(state='disabled')
    else:
        partnumber.config(state='normal')
#######################################################################################################






#######################################################################################################
Main = Tk()
Main.title("Circuitlink")
Main.resizable(width=False, height=False)
Main.geometry("1000x500")


#######################################################################################################



#Setup = Button(Main, text="Setup", command = SetupWindow) #Setup button
#Setup.place(x=10, y=10)

#Close = Button(Main, text="Close", command = exit) #exit button
#Close.place(x=915, y=470)



#######################################################################################################
ProgramFlashpro = Button(Main,
                        text="Program Flashpro",
                       command = programflashpro,)
ProgramFlashpro.place(x=400, y=50)

ProgramFt = Button(Main,
                  text="Program Ft_Prog",
                 command = programft) #Programm button
ProgramFt.place(x=400, y=80)

config = Button(Main,
               text="Flashpro File",
              command = flashproconfig) #Flashrpo Setup button
config.place(x=0, y=410)

configftdi = Button(Main,
                   text="FT_Prog File",
                  command = ftprogconfig) #FT_Prog Setup Button
configftdi.place(x=0, y=455)

cmd = Button(Main,
            text="Open CMD",
           command = opencmd)
cmd.place(x=400, y=120)

label = Label(Main,
             text="")
label.pack(pady=10)




var1 = tk.IntVar() # Creates variable that is "variable"

c1 = tk.Checkbutton(Main, text="Part Number Reference set.", variable=var1, onvalue=1, offvalue=0, command = checkbox) #tkinter code to create a check box, assigning the variable to use, what on and off = and the command to call
c1.place(x=0, y=380)

partnumber = Text(Main, height=1, width=7)
partnumber.place(x=500, y=220)
#######################################################################################################















mainloop()
#######################################################################################################