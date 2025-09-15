import matplotlib.pyplot as plt
import numpy as np

# Sample sales data
x = np.array([0, 1, 2, 3, 4, 5])

# Sales data for three products over six months
product_A_sales = np.array([1000, 1500, 2000, 2500, 3000, 3500])
product_B_sales = np.array([1200, 1600, 2200, 2700, 3200, 3700])
product_C_sales = np.array([1300, 1700, 2300, 2800, 3300, 3800])

# Plotting the sales data as a line chart
plt.plot(x, product_A_sales, marker='o', label='Product A', color='blue')
plt.plot(x, product_B_sales, marker='s', label='Product B', color='green')
plt.plot(x, product_C_sales, marker='^', label='Product C', color='red')    
plt.title('Sales Data Over Six Months')
plt.xlabel('Months')
plt.ylabel('Sales (in units)')
plt.xticks(x, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('sales_data_line_chart.png')
# Try to show the plot if possible
try:
	plt.show()
except Exception as e:
	print("Could not display the chart window. The image has been saved as 'sales_data_line_chart.png'.")
 