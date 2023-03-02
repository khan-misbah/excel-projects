
import pandas as pd
from openpyxl import load_workbook




df = pd.DataFrame({'NAME':['khan misbah', 'shiakh Afsha', 'khan zikra','khan anjum'],
                  'AGE':[ 20, 21,23, 22],'NUMBERS':[635271891,7546348328,732612384,63284721],
                  'EMAIL':['khanmisbah@gmail', 'shaikhafsha@gmail', 'khanzikra@gmail', 'khanajum@gmail']})

print(df)

writer = pd.ExcelWriter('demo.xlsx', engine='openpyxl')

writer.book = load_workbook('demo.xlsx')


writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)

df = pd.read_excel(r'demo.xlsx')
print(df)

df.to_excel(writer,sheet_name='Sheet1', index=False)



writer.close()
