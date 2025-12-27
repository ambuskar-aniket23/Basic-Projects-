import pandas as pd
import module1 as m
import matplotlib.pyplot as plt
# for reading the csv (comma seperated value) file. 
data=pd.read_csv('sales_data_large.csv')

data['Date']=pd.to_datetime(data['Date'])
data['Revenue']=data['Quantity'] * data['Price']

# now code is given below is of KPI value.

t_revenue = data['Revenue'].sum()
b_product = data.groupby("Product")["Quantity"].sum().idxmax()
print("Sales dashboard of a Electronic products are as follows.")

# for creating some pattern 
m.printline("*")

print("Total Revenue is :- ",t_revenue,"₹")
print("And the best product is :- ",b_product) 

p_revenue=data.groupby('Product')['Revenue'].sum() 

# use Matplotlib for plotin the Graph.

plt.figure()
p_revenue.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()

# This is for Monthly revenue
data["Month"] = data["Date"].dt.month
monthly_sales = data.groupby("Month")["Revenue"].sum()

plt.figure()
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()



# ANIKET SANDIP AMBUSKAR
# aniket23july@gmail.com, ambuskaraniket100@gmail.com
# 8010519461