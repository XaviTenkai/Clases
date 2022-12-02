
'''
import os.path 
assert os.path.isfile("<C:\\Users\\xtorramade\\Tenkai Technologies SL\\Data and Finance Team - Licenses Costs\\Real_vs_BudgetTEST.xlsx>")

'''


import schedule
import time
    
def report_dailyleadsandftds() : 

    # Importing the pywin32 module
    import win32com.client

    # Opening Excel software using the win32com
    File = win32com.client.Dispatch("Excel.Application")

    # Optional line to show the Excel software
    # File.Visible = 1

    # Opening your workbook
    Workbook = File.Workbooks.open("C:\\Users\\xtorramade\\Tenkai Technologies\\Tenkai Data Team - General\\Reports\\Daily Leads FTDs\\Daily Leads and FTDs - Costs.xlsx")

    # Refeshing all the shests
    Workbook.RefreshAll()

    print("Refreshing All")

    #Invent de Sergi
    File.CalculateUntilAsyncQueriesDone()

    print("Refresh Completed")

    # Saving the Workbook
    Workbook.Save()
    print("Saving")


    # Closing the Excel File
    File.Quit()

    print("Wb Closed")


schedule.every().day.at("18:04").do(report_dailyleadsandftds)

while True :
    schedule.run_pending()
    time.sleep(1)
    
      