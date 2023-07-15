# TrafficDataAnalasis

This program is designed to analyze and visualize traffic patterns using data from two different years. It reads CSV files containing traffic data for each year and generates bar graphs with best-fit curves for comparison.
The program will generate a figure with three subplots showing the traffic patterns. The first subplot displays the traffic data for the year 2010, the second subplot displays the traffic data for the year 2022, and the third subplot shows a comparison of the best-fit curves.

The figure will be displayed on your screen. You can interact with it (zoom in/out, save, etc.) using the options provided by the matplotlib window.

## Customization
If you have CSV files with different filenames or want to analyze data from different years, you can modify the filename2010 and filename2022 variables in the code. Ensure that the CSV files have the necessary data format for the program to work correctly.

The program currently fits a polynomial curve of degree 13 to the data. If you want to change the degree of the polynomial, you can modify the coefficients = np.polyfit(x2010, y2010, 13) line in the code.

You can customize the appearance of the graphs by modifying the options in the axs[num] section of the code. For example, you can change the title, labels, colors, or width of the bars.
