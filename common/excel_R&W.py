
import openpyxl
import data
wb = openpyxl.load_workbook("..\data\Testcase.xlsx")
sheet1 = wb["Sheet1"]
for row in sheet1.iter_rows():
    for cell in row:

        print(cell.coordinate,cell.value)