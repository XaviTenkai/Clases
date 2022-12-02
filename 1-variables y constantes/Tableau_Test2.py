import subprocess

import pyautogui

import time


def Publish_Tableau_Finance() :

    TF = subprocess.Popen(["C:\\Users\\xtorramade\\Tenkai Technologies SL\\Data and Finance Team - Licenses Costs\\Finance Budget_v4.twb"],shell=True)

    #print("tableau opened")

    time.sleep(15)

    Publish_1=pyautogui.locateOnScreen("C:\\Users\\xtorramade\\Tenkai Technologies SL\\Data and Finance Team - Licenses Costs\\Images\\Publish_tableau.png")

    pyautogui.leftClick(Publish_1)

    time.sleep(8)

    Publish_2=pyautogui.locateOnScreen("C:\\Users\\xtorramade\\Tenkai Technologies SL\\Data and Finance Team - Licenses Costs\\Images\\Publish_tableau_2.png")

    pyautogui.leftClick(Publish_2)

    time.sleep(2)

    Publish_3=pyautogui.locateOnScreen("C:\\Users\\xtorramade\\Tenkai Technologies SL\\Data and Finance Team - Licenses Costs\\Images\\Publish_tableau_Y.png")

    pyautogui.leftClick(Publish_3)

    #subprocess.Popen.terminate("C:\\Users\\SergiSerra\\Skyline Medimed SL\\Data and Finance Team - Documents\\General\\Datasets_Finance\\Finance Budget_v4.twb")
    
schedule.every().day.at("17:50").do(Update_Dashboard_FinanceBudgetv4)



while True:

    schedule.run_pending()

    time.sleep(1)
    
    
    
    
    
    
    