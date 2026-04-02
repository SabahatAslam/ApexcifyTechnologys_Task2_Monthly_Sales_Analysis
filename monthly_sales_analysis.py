# Import libraries and load dataset
import matplotlib.pyplot as plt
import pandas as pd
monthly_sales = pd.read_csv("Monthly_sales_dataset.csv") #paste the file path or write csv file name here and place it in the same project folder
print(monthly_sales)

# Plot a line chart for yearly analysis
plt.figure(1)
plt.plot(monthly_sales["Month"], monthly_sales["Sales($)"])
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.xticks(rotation=30) #Rotate x-axis labels by 30 degrees



# plot a bar chart to analyze month by month sales
plt.figure(2)
plt.bar(monthly_sales["Month"], monthly_sales["Sales($)"], color='lightgreen')
plt.title("Monthly Sales Analysis")
plt.ylabel("Sales($)")
plt.xticks(rotation=30)

plt.tight_layout()
plt.show() # show both plot here

