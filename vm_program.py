# FILENAME: vending_machine.py

import tkinter as tk
import csv
import os
import input_variable as inp
import report as rpt
import data_load as dl

''' This is a Vending Machine Program with four items selection and generate visualization reports of sales data'''

# Popup window for Report Selection
def popup():
    popup_window = tk.Tk()
    popup_window.title("Reports")
    popup_window.geometry("200x100")
    label = tk.Label(popup_window, text="Reports Selection")
    label.pack()
    daily_sales_button = tk.Button(popup_window, text="Daily Sales Report", command=lambda: rpt.daily_sales() if os.path.exists(inp.database_file(inp.file_name)) else msg()).pack()
    product_sales_button = tk.Button(popup_window, text="Product Sales Report", command=lambda: rpt.product_sales() if os.path.exists(inp.database_file(inp.file_name)) else msg()).pack()
    popup_window.mainloop()

# Error handling message when no data file is missing or not created
def msg():
    msg_window = tk.Tk()
    msg_window.title("Error Message")
    msg_window.geometry("200x100")
    label = tk.Label(msg_window, text="Error: No purchased made Till date")
    label.pack()
    msg_window.mainloop()

# Selection button response message and store selection item in temp file
def payment(value):
    payment_label = tk.Label(message_frame, text="\t\tPayment Due : $ {} \t\t".format(inp.product_price)).grid(row=0, column=0)
    with open(inp.database_file(inp.temp_file), 'w') as tp:
        csv_writer = csv.writer(tp)
        csv_writer.writerow([value])

# Cancel button to reset the message contain
def clear_payment():
    if os.path.exists(inp.database_file(inp.temp_file)):
        payment_label = tk.Label(message_frame, text="\tSelect your product\t\t").grid(row=0, column=0)
        inp.remove_file()
    else:
        payment_label = tk.Label(message_frame, text="\tSelect your product\t\t").grid(row=0, column=0)

# Payment button function with response message and dataload to the csv file
def payment_complete():
    if os.path.exists(inp.database_file(inp.temp_file)):
        payment_label = tk.Label(message_frame, text="\tThank you for your Payment\t\t").grid(row=0, column=0)
        with open(inp.database_file(inp.temp_file), 'r') as sel:
            pass_val = sel.readline().rstrip()
            dl.data_entry(pass_val)
        inp.remove_file()
    else:
        payment_label = tk.Label(message_frame, text="\tSelect your product\t\t").grid(row=0, column=0)

# Popup main window
main_window = tk.Tk()
main_window.title("Vending Machine")
main_window.geometry("400x400")

welcome_lbl = tk.Label(main_window,
                       text="Welcome to \n Vending Machine \n Program \n Today's Date : {}".format(inp.today_date),
                       font="Verdana 14 bold")
welcome_lbl.pack()

# Selection Image location
coke = tk.PhotoImage(file=inp.database_file(inp.coke)).subsample(2, 2)
sprite = tk.PhotoImage(file=inp.database_file(inp.sprite)).subsample(2, 2)
fanta = tk.PhotoImage(file=inp.database_file(inp.fanta)).subsample(2, 2)
water = tk.PhotoImage(file=inp.database_file(inp.water)).subsample(2, 2)

# selection frame
selection_frame = tk.Frame(main_window)
selection_frame.pack(side=tk.TOP)

# message frame
message_frame = tk.Frame(main_window)
message_frame.pack(side=tk.LEFT)

# payment button frame
payment_frame = tk.Frame(main_window)
payment_frame.pack(side=tk.BOTTOM)

# report button frame
report_frame = tk.Frame(main_window)
report_frame.pack(side=tk.RIGHT)

# selection button
s1_button = tk.Button(selection_frame, text="Coke", image=coke, command=lambda: payment(1)).grid(row=0, column=0)
s2_button = tk.Button(selection_frame, text="Sprite", image=sprite, command=lambda: payment(2)).grid(row=0, column=1)
s3_button = tk.Button(selection_frame, text="Fanta", image=fanta, command=lambda: payment(3)).grid(row=1, column=0)
s4_button = tk.Button(selection_frame, text="Water", image=water, command=lambda: payment(4)).grid(row=1, column=1)

# payment button
p1_button = tk.Button(payment_frame, text="Payment", command=payment_complete).grid(row=0, column=0)
p2_button = tk.Button(payment_frame, text="Cancel", command=clear_payment).grid(row=0, column=1)

# report button
r1_button = tk.Button(report_frame, text="Reports", command=popup).grid(row=0, column=0)

main_window.mainloop()