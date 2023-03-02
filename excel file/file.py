
import xlsxwriter
from openpyxl import Workbook
wb =  Workbook()
ws = wb.active

Data =[
        {
        "name":"khan misbah",
        "phone": "784926209" ,  
        "email": "khanmisbah@gmail", 
        "address":"kurla, mumbai 400070"
        },
        {
        "name":"shaikh Nida",
        "phone": "98726207" ,  
        "email": "shaikhnida@gmail", 
        "address":"Thane, mumbai 400072"
        },
      {
        "name":"khan zikra", 
        "phone": "7849438997",  
        "email": "khanZikra@gmail", 
        "address":"SakiNaka, mumbai 400072"
      }, 
        {
        "name":"shaikh Sahifa",
        "phone": "7849473452" ,  
        "email": "shaikhsahifa@gmail", 
        "address":"Ghatkopar, mumbai 400071"
        },
        {
    "name":"Shaikh Minhaj",
     "phone": "7849284609" ,  
     "email": "shaikhminhaj@gmail",  
     "address":"SakiNaka, mumbai 400070"
        }, 

        {
    "name":"khan anjum",
     "phone": "7849658392" ,  
     "email": "khananjum@gmail",  
     "address":"Jarimari, mumbai 400070"
        }   

]


workbook = xlsxwriter.Workbook("All_About_Python_Excel.xlsx")

worksheet= workbook.add_worksheet("firstSheet")

worksheet.write(0,1,"#")
worksheet.write(0,2, "Name")
worksheet.write(0,3,"Phone")
worksheet.write(0,4, "Email")
worksheet.write(0,5, "Address")
 
for index, entry in enumerate(Data):
    worksheet.write(index+1,0,str(index))
    worksheet.write(index+1,1,entry["name"])
    worksheet.write(index+1,2,entry["phone"])
    worksheet.write(index+1,3,entry["email"])
    worksheet.write(index+1,4,entry["address"])
workbook.close()




