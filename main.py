import csv 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
filename2010 = "i25_2010University.csv"

filename2022 = "i25_2022University.csv"
fig, axs = plt.subplots(1, 3)
fig.suptitle('Traffic Patterns')
def draw_bar(filename,num):
    with open(filename, 'r') as csvfile:
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
    axs[num].bar(rows_2010, fields_2010, color ='maroon',
            width = .8)
    final_finalname = filename.split(".")
    axs[num].set_title(final_finalname[0])
    axs[num].set(xlabel='Hours', ylabel='Numbers of Passengers')
    axs[num].plot(x_fit, y_fit, label='Best-fit Curve')
    axs[-1].plot(x_fit,y_fit,label=final_finalname[0])
    axs[-1].legend(loc="upper left")
draw_bar(filename2010,0)
draw_bar(filename2022,1)

plt.show()
