import pandas as pd
import matplotlib.pyplot as plt
import input_variable as inp

''' Generate  Sales or Product Bar Chart Reports'''

# Function to generate Daily Sales Bar Chart
def daily_sales():
    df = pd.read_csv(inp.database_file(inp.file_name))
    daily_sales = df.groupby(['Sales_Date']).Product_Price.sum().reset_index()
    daily_sales.plot(kind='bar', x='Sales_Date', y='Product_Price')
    plt.xlabel("Date", labelpad=11)
    plt.ylabel("Sales Amount", labelpad=11)
    plt.title("Daily Sales Amount Report", y=1.02)
    plt.gcf().subplots_adjust(bottom=0.2)
    plt.legend().set_visible(False)
    plt.show()

# Function to generate Product Sales Count Bar Chart
def product_sales():
    df = pd.read_csv(inp.database_file(inp.file_name))
    product_sales = df.groupby(['Product_Name']).Product_Price.count().reset_index()
    product_sales.plot(kind='bar', x='Product_Name', y='Product_Price')
    plt.xlabel("Product Name", labelpad=11)
    plt.ylabel("Product Count", labelpad=11)
    plt.title("Product Sales Count Report", y=1.02)
    plt.legend().set_visible(False)
    plt.show()

