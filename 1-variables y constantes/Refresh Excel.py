#import win32com.client

'''
xlapp = win32com.client.DispatchEx("Excel.Application")
wb = xlapp.Workbooks.Open(C:\Users\xtorramade\Tenkai Technologies SL\Data and Finance Team - Licenses Costs\Real_vs_BudgetTEST.xlsx)
wb.RefreshAll()
xlapp.CalculateUntilAsyncQueriesDone()
wb.Save()
xlapp.Quit()
'''


# Importing the pywin32 module
import win32com.client

# Opening Excel software using the win32com
File = win32com.client.Dispatch("Excel.Application")

# Optional line to show the Excel software
File.Visible = 1

# Opening your workbook
Workbook = File.Workbooks.open("Real_vs_BudgetTEST.xlsx")

# Refeshing all the shests
Workbook.RefreshAll()

# Saving the Workbook
Workbook.Save()

# Closing the Excel File
File.Quit()










































