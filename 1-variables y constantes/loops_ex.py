    
    
    

import ctypes
import schedule
import time
import subprocess
import pyautogui

Publish_1=None
Publish_2=None
Publish_3=None


i = 0

Publish_i = [Publish_1, Publish_2,Publish_3]


while i < 3 :
    count = 0
    limit = 5
    while Publish_i[i] == None :
        Publish_1=pyautogui.locateOnScreen("C:\\Users\\xtorramade\\Tenkai Technologies SL\\Data and Finance Team - Licenses Costs\\Images\\Publish_tableau.png")
        Publish_2=pyautogui.locateOnScreen("C:\\Users\\xtorramade\\Tenkai Technologies SL\\Data and Finance Team - Licenses Costs\\Images\\Publish_tableau_2.png")
        Publish_3=pyautogui.locateOnScreen("C:\\Users\\xtorramade\\Tenkai Technologies SL\\Data and Finance Team - Licenses Costs\\Images\\Publish_tableau_Y.png")
        Publish_i = [Publish_1, Publish_2,Publish_3]
        count = count + 1
        print(f"Image {i+1} not found (Try number {count}/{limit})")
        if count == limit:
            ctypes.windll.user32.MessageBoxW(0, f"Then number of tries ({limit} to find Image {i+1} was exceeded. Please, manually update Tableau",1)
            print("Someting went wrong, Please manually update Tableau")
            exit()
    print(Publish_i[i])
    pyautogui.leftClick(Publish_i[i])
    i = i + 1    
    print(i)


'''
    Publish_1=pyautogui.locateOnScreen("C:\\Users\\xtorramade\\Tenkai Technologies SL\\Data and Finance Team - Licenses Costs\\Images\\Publish_tableau.png")

    while Publish_1 == None :
    
        Publish_1=pyautogui.locateOnScreen("C:\\Users\\xtorramade\\Tenkai Technologies SL\\Data and Finance Team - Licenses Costs\\Images\\Publish_tableau.png")
        print("Image 1 not found")
        time.sleep(2)
    pyautogui.leftClick(Publish_1)
    print("Image 1 FOUND")

    #time.sleep(8)

    Publish_2=pyautogui.locateOnScreen("C:\\Users\\xtorramade\\Tenkai Technologies SL\\Data and Finance Team - Licenses Costs\\Images\\Publish_tableau_2.png")
    
    while Publish_2 == None :
        Publish_2=pyautogui.locateOnScreen("C:\\Users\\xtorramade\\Tenkai Technologies SL\\Data and Finance Team - Licenses Costs\\Images\\Publish_tableau_2.png")
        print("Image 2 not found")
        time.sleep(2)
    pyautogui.leftClick(Publish_2)
    print("Image 2 FOUND")

    #time.sleep(2)

    Publish_3=pyautogui.locateOnScreen("C:\\Users\\xtorramade\\Tenkai Technologies SL\\Data and Finance Team - Licenses Costs\\Images\\Publish_tableau_Y.png")
    
    while Publish_3 == None :
        Publish_3=pyautogui.locateOnScreen("C:\\Users\\xtorramade\\Tenkai Technologies SL\\Data and Finance Team - Licenses Costs\\Images\\Publish_tableau_Y.png")
        print("Image 3 not found")
        time.sleep(2)
    pyautogui.leftClick(Publish_3)
    print("Image 3 FOUND and Tableau Online Updated")

    #subprocess.Popen.terminate("C:\\Users\\SergiSerra\\Skyline Medimed SL\\Data and Finance Team - Documents\\General\\Datasets_Finance\\Finance Budget_v4.twb")
    
    '''