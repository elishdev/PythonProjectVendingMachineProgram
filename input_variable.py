import os
import datetime

'''Intermediate Variable file name which can be edited as needed '''

# Assign current date to a variable
today_date = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')

file_name = 'vm_data.csv'
temp_file = 'temp.csv'
product_price = 0.50

# selection button image filename
coke = 'coke.png'
sprite = 'sprite.png'
fanta = 'fanta.png'
water = 'water.png'

# Function to return path of filename
# update below path based on the image file and csv file location
def database_file(filename):
    return os.path.join('C:', os.sep, 'Users', 'Dev', 'Documents', 'icon', filename)

def remove_file():
    os.remove(database_file(temp_file))