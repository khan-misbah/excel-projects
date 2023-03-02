from openpyxl import Workbook

workbook = Workbook()
# print(workbook.active.title)
# print(workbook.sheetnames)

workbook['Sheet'].title = 'Student result'
Sheet1 = workbook.active


Sheet1['A1'].value = 'student Name'
Sheet1['B1'].value = 'Marks'
Sheet1['C1'].value = 'Result'
Sheet1['A2'].value = 'khan Affan'
Sheet1['B2'].value = '78'
Sheet1['C2'].value = 'pass'
Sheet1['A3'].value = 'khan hassan'
Sheet1['B3'].value = '68'
Sheet1['C3'].value = 'pass'
Sheet1['A4'].value = 'shaikh Afsha'
Sheet1['B4'].value = '70'
Sheet1['C4'].value = 'pass'
Sheet1['A5'].value = 'khan faizan'
Sheet1['B5'].value = '30'
Sheet1['C5'].value = 'fail'


workbook.save("Result.xlsx")