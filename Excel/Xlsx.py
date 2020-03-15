import pandas as pd

def writer ():
    # dataframe Name and Age columns
    df = pd.DataFrame({'Name': ['A', 'B', 'C', 'D'],
                       'Age': [10, 0, 30, 50]})

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('demo.xlsx')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1', index=False)

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
    writer.close()



import pandas as pd


sheet = pd.ExcelFile(r'demo.xlsx')

nomesSheet = sheet.sheet_names

for i in nomesSheet:

    reader = pd.read_excel(r'demo.xlsx', sheet_name=i)
    print(reader)


