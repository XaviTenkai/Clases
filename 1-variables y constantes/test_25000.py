import schedule
import time
import subprocess
import pyautogui
    
    

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