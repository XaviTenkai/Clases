    # Importing the pywin32 module
import win32com.client

    # Opening Excel software using the win32com
File = win32com.client.Dispatch("Excel.Application")

    # Optional line to show the Excel software
#File.Visible = 0

    # Opening your workbook
Workbook = File.Workbooks.open("C:\\Users\\xtorramade\\Tenkai Technologies\\Tenkai Data Team - General\\Reports\\Daily Leads FTDs\\Daily Leads and FTDs - Costs - TEST.xlsx")

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