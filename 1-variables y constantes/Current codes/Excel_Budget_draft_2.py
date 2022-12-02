

import schedule
import time
import subprocess
import pyautogui
import ctypes


    
def report_daily_Finance() : 

    # Importing the pywin32 module
    import win32com.client

    # Opening Excel software using the win32com
    File = win32com.client.Dispatch("Excel.Application")

    # Optional line to show the Excel software
    # File.Visible = True

    # Opening your workbook
    Workbook = File.Workbooks.open("C:\\Users\\xtorramade\\Tenkai Technologies SL\\Team - General\\Budgets\\Budget_Draft_2022.xlsm")

    # Executing Macro
    File.Application.Run("Budget_Draft_2022.xlsm!Expenses.Update_Expenses_NEW")
    print("Executing Macro Budget_Draft_2")

    # Refeshing all the shests
    Workbook.RefreshAll()

    print("Refreshing All Budget_Draft_2")

    #Invent de Sergi
    File.CalculateUntilAsyncQueriesDone()

    print("Budget_Draft_2 Refresh Completed")

    # Saving the Workbook
    Workbook.Save()
    print("Saving Budget_Draft_2")

    time.sleep(5)

    print("Wb Closed")

    Workbook.Close()

    # Opening Cost Licenses Workbook
    Workbook_2 = File.Workbooks.open("C:\\Users\\xtorramade\\Tenkai Technologies SL\\Data and Finance Team - Licenses Costs\\Licenses\\Cost_Licenses_teams.xlsx")
    print("Opening Cost_Licenses_teams")

    Workbook_2.RefreshAll()
    print("Refreshing All Cost_Licenses_teams")

    File.CalculateUntilAsyncQueriesDone()
    print("Cost_Licenses_teams Refresh Completed")

    Workbook_2.Save()
    print("Saving Cost_Licenses_teams")

    time.sleep(5)

    Workbook_2.Close()

    # Opening Cost Real vs Budget
    Workbook_3 = File.Workbooks.open("C:\\Users\\xtorramade\\Tenkai Technologies SL\\Data and Finance Team - Licenses Costs\\Real_vs_Budget.xlsx")
    print("Opening Real_vs_Budget")

    time.sleep(3)

    Workbook_3.RefreshAll()
    print("Refreshing All Real_vs_Budget")

    File.CalculateUntilAsyncQueriesDone()
    print("Real_vs_Budget Refresh Completed")

    Workbook_3.Save()
    print("Saving Real_vs_Budget")

    # Closing Excel
    Workbook_3.Close()
    print("Excel closed")
    
    File.Quit()
    #print("Excel App Closed")
    
#schedule.every().day.at("15:50").do(report_daily_Finance)

#def Publish_Tableau_Finance() :

    TF = subprocess.Popen(["C:\\Users\\xtorramade\\Tenkai Technologies SL\\Data and Finance Team - Licenses Costs\\Finance Budget_2022.twb"],shell=True)
    print("Opening Real vs Budget - Tableau")
    time.sleep(5)

    Publish_1=None
    Publish_2=None
    Publish_3=None

    i = 0
    
    Publish_i = [Publish_1, Publish_2,Publish_3]
    
    Number_of_images = len(Publish_i)
    print(f"Number of images to click = {Number_of_images}")

    while i < Number_of_images :
        count = 0
        limit = 8
        while Publish_i[i] == None :
            time.sleep(1)
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
        print(f"Click on image {i}")
        
    time.sleep(10)
    
    TF2 = subprocess.Popen(["C:\\Users\\xtorramade\\Tenkai Technologies SL\\Data and Finance Team - Licenses Costs\\Licenses\\Area_Expenses.twb"],shell=True)
    print("Opening Area Expenses - Tableau")
    time.sleep(5)

    Publish_1=None
    Publish_2=None
    Publish_3=None

    i = 0
    
    Publish_i = [Publish_1, Publish_2,Publish_3]
    
    Number_of_images = len(Publish_i)
    print(f"Number of images to click = {Number_of_images}")

    while i < Number_of_images :
        count = 0
        limit = 8
        while Publish_i[i] == None :
            time.sleep(1)
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
        print(f"Click on image {i}")

#schedule.every().day.at("15:49").do(Publish_Tableau_Finance)
schedule.every().day.at("15:01").do(report_daily_Finance)

while True :
    schedule.run_pending()
    time.sleep(1)
    
    
    
    
    
    
    