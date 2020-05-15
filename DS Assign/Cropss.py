
import pandas as pd
import csv
import xlrd
df = pd.read_excel (r'‪C:\Users\Dell\Desktop\crops\CropsDataFile.xlsx')
# Program to extract a particular row value 
import xlrd 
loc = (r'‪C:\Users\Dell\Desktop\crops\CropsDataFile.xlsx') 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
sheet.cell_value(0, 0) 
a=int(input())
if a==2000:
    for i in range(3,13):
        print(sheet.row_values(i))
    for i in range(82,93):
        print(sheet.row_values(i))
    for i in range(291,302):
        print(sheet.row_values(i))  

elif a==2001:
    for i in range(93,100):
        print(sheet.row_values(i))
    for i in range(13,20):
        print(sheet.row_values(i))
      
elif a==2006:
    for i in range(56,67):
        print(sheet.row_values(i))
    for i in range(101,114):
        print(sheet.row_values(i))
    for i in range(175,188):
        print(sheet.row_values(i)) 

elif a==2002:
    for i in range(21,30):
        print(sheet.row_values(i))
    for i in range(132,142):
        print(sheet.row_values(i))
     
elif a==2003:
    for i in range(30,39):
        print(sheet.row_values(i))
    for i in range(142,152):
        print(sheet.row_values(i))
                      
elif a==2004:
    for i in range(39,48):
        print(sheet.row_values(i))
    for i in range(152,162):
        print(sheet.row_values(i))  

elif a==2005:
    for i in range(48,55):
        print(sheet.row_values(i))
    for i in range(162,175):
        print(sheet.row_values(i))

elif a==1997:
    for i in range(206,234):
        print(sheet.row_values(i))

elif a==1998:
    for i in range(234,261):
         print(sheet.row_values(i))

elif a==1999:
    for i in range(261,291):
        print(sheet.row_values(i)) 



#graph :

import csv
import xlrd
import pandas as pd        

loc = (r'‪C:\Users\Dell\Desktop\crops\CropsDataFile.xlsx') 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0) 
_ask = input('Admin or User\n')
if(_ask == 'Admin'):
     _see = input('Do you want to view data\n')
     if(_see == 'Yes'): 
         for i in range(sheet.nrows):
            print(sheet.row_values(i,0))
_graph = input('Do you want to view graph, tell Yes or No\n')
if _graph=='Yes':
     x=list()
     y=list()
     import matplotlib.pyplot as plt 
     a = input('Enter name of crop\n')
     for i in range(2,sheet.nrows) :
         if sheet.cell_value(i,4)==a:
             x.append(sheet.cell_value(i,2))
             y.append(sheet.cell_value(i,6))
     plt.plot(x, y) 
     plt.xlabel('Year') 
     plt.ylabel('Production') 
     plt.title('Crop Production')  
     plt.show() 
    
year=input('Do you want to see the details in a particular year, tell Yes or No\n')
if(year == 'Yes'):
     b=int(input('Enter year\n'))
     for i in range(2,sheet.nrows): 
         if sheet.cell_value(i,2)==b:
             data={sheet.cell_value(1,0):sheet.cell_value(i, 0),
                 sheet.cell_value(1,1):sheet.cell_value(i, 1),
                 sheet.cell_value(1,2):sheet.cell_value(i, 2),
                 sheet.cell_value(1,3):sheet.cell_value(i, 3),
                 sheet.cell_value(1,4):sheet.cell_value(i, 4)}
             dboard=pd.DataFrame(data,index=list(range(1)))
             print(dboard)