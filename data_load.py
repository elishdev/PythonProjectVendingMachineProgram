import csv
import os
import input_variable as inp

''' Data load to backend file '''

# Function to evaluate the selection and perform data entry to backend file
def data_entry(item_number):
    if item_number == '1':
        product_name = "Coke"
    elif item_number == '2':
        product_name = "Sprite"
    elif item_number == '3':
        product_name = "Fanta"
    else:
        product_name = "Water"
    if os.path.exists(inp.database_file(inp.file_name)):
        with open(inp.database_file(inp.file_name), 'a') as csv_file:
            csv_writer = csv.writer(csv_file, lineterminator='\n')
            csv_writer.writerow([item_number, product_name, inp.product_price, inp.today_date])
    else:
        with open(inp.database_file(inp.file_name), 'w') as csv_file:
            csv_writer = csv.writer(csv_file, lineterminator='\n')
            csv_writer.writerow(['Product_ID', 'Product_Name', 'Product_Price', 'Sales_Date'])
            csv_writer.writerow([item_number, product_name, inp.product_price, inp.today_date])