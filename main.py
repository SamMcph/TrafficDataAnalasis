import csv 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
filename2010 = "i25_2010University.csv"
fields_2010 = []
rows_2010=[]
filename2022 = "i25_2022University.csv"
fields_2022 = []
rows_2022 = []
with open(filename2010, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    total_data = []
    for i in csvreader:
        total_data.append(i)
    rows_2010 = total_data[0][1:25]
    fields_2010 = total_data[1][1:25]
    fields_2010 = [ float(x) for x in fields_2010 ]
    for i in range(len(rows_2010)):
        rows_2010[i] = int(rows_2010[i][4:])   
x2010 = np.array(rows_2010)
y2010 = np.array(fields_2010)
coefficients = np.polyfit(x2010, y2010, 13)
poly = np.poly1d(coefficients)
x_fit = np.linspace(x2010.min(), x2010.max(), 100)
y_fit = poly(x_fit) 
with open(filename2022,"r")as csvfile:
    csvreader = csv.reader(csvfile)
    total_data = []
    for i in csvreader:
        total_data.append(i)
    rows_2022 = total_data[0][1:25]
    fields_2022 = total_data[1][1:25]
    fields_2022 = [ float(x) for x in fields_2022]
    for i in range(len(rows_2022)):
        rows_2022[i] = int(rows_2022[i][4:])
x2022 = np.array(rows_2022)
y2022 = np.array(fields_2022)
coefficients2022 = np.polyfit(x2022,y2022,13)
poly = np.poly1d(coefficients2022)
x_fit2022 = np.linspace(x2022.min(),x2022.max(),100)
y_fit2022 = poly(x_fit2022)




fig, axs = plt.subplots(1, 2)
fig.suptitle('Traffic Patterns')
axs[0].bar(rows_2010, fields_2010, color ='maroon',
        width = .8)
axs[0].set_title("I-25 Traffic in 2010")
axs[0].set(xlabel='Hours', ylabel='Numbers of Passengers')
axs[0].plot(x_fit, y_fit, label='Best-fit Curve')
axs[1].set(xlabel='Hours', ylabel='Numbers of Passengers')
axs[1].set_title("I-25 Traffic in 2022")
axs[1].bar(rows_2022, fields_2022, color="blue",width = .8)
axs[1].plot(x_fit2022, y_fit2022, label='Best-fit Curve')
plt.show()
