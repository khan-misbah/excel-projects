import  pandas  as pd
import os 

#data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
def append_data_to_excel(excel_name,sheet_name, data):

    with pd.ExcelWriter('test.xlsx') as writer:
        columns = []
        for k, v in data.items():
            columns.append(k)

        df = pd.DataFrame(data, index= None)
        df_source = None
        # if os.path.exists(excel_name):
        # if os.path.exists(excel_name):
        if not os.path.exists(excel_name):
            df_source(excel_name, 'w').close()
            df_source = pd.DataFrame(pd.read_excel("test.xlsx", sheet_name=sheet_name,engine="xlrd"))
        if df_source is not None:
            df_dest = df_source.append(df)
        else:
            df_dest = df

        df_dest.to_excel(writer, sheet_name=sheet_name, index = False, columns=columns)

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky','saname', 'mac', 'suhan', 'jerry'],
'Age':[28,34,29,42,21,20,17,19], 'city':['mumbai', 'pune','kokan', 'jalgao','UP','MP','kashmir','Panjab']}
append_data_to_excel('test.xlsx', 'person',data)
# data = {'Name':['saname', 'mac', 'suhan', 'jerry'],'Age':[21,20,17,19]}
# append_data_to_excel('test.xlsx', 'person',data)
# append_data_to_excel('test.xlsx', 'person',data)

# writer.close()