from tkinter import *
import tkinter as tk
from tkinter import ttk

from tuitions import Payment
from student import Student
# functions



window = Tk()
window.title("Fees Payment")

def add_fees():
    tuition = int(tuition_entry.get())
    lib_fee = int(lib_fee_entry.get())
    func_fee = int(func_fee_entry.get())
    med_fee = int(med_fee_entry.get())

    Payment.set_total_fees(tuition, lib_fee, func_fee,med_fee)
    Total_fee_entry.delete(0)
    Total_fee_entry.insert(0,string=f"total_fees is: {Payment.get_total_fees()}")

stds = []
def student_details():
    global stds
    name = name_entry.get()
    age = age_entry.get()
    fees = int(fee_paid_entry.get())
    std1 = Student(name, age, fees)

    stds = std1.get_all_students()
def print_students():
    output_text.insert(tk.END, 'All the Students: ')
    i = 0
    for std in stds:
        output_text.insert(tk.END, f'\n\nStudent {i + 1}')
        output_text.insert(tk.END, f'\n{std}')
        i +=1

    output_text.insert(tk.END, '\nSTUDENTS WHO HAVE PAID: ')
    paid = Payment.get_paid_std()

    for pa in paid:
        output_text.insert(tk.END, f'\n{pa}')



# creating labels
setting_fees_label = ttk.Label(text = "Setting fees")
setting_fees_label.grid(row=0, column=1)

tuition_label = ttk.Label(text="Enter tuition: ")
tuition_label.grid(row=1, column=0)

med_fee_label = ttk.Label(text="Enter med_fee: ")
med_fee_label.grid(row=2, column=0)

lib_fee_label = ttk.Label(text="Enter lib_fee:")
lib_fee_label.grid(row=3, column=0)

func_fee_label = ttk.Label(text="Enter func_fee: ")
func_fee_label.grid(row=4, column=0)

Total_fee_label = ttk.Label(text="Total_fee: ")
Total_fee_label.grid(row=5, column=0)

fees_paid_label = ttk.Label(text="Fees_paid: ")
fees_paid_label.grid(row=7, column=0)

name_label = ttk.Label(text="Enter student name: ")
name_label.grid(row=9, column=0)

age_label = ttk.Label(text="Enter student age: ")
age_label.grid (row=10, column=0)

#fee_label = ttk.Label(text="Enter fees paid: ")
#fee_label.grid(row=11, column=0)




# setting entry
tuition_entry = Entry(width=30)
tuition_entry.grid(row=1, column=1)
tuition_entry.focus()

med_fee_entry = Entry(width=30)
med_fee_entry.grid(row=2, column=1)


lib_fee_entry = Entry(width=30)
lib_fee_entry.grid(row=3, column=1)


func_fee_entry = Entry(width=30)
func_fee_entry.grid(row=4, column=1)

Total_fee_entry = Entry(width=25)
Total_fee_entry.grid(row=5, column=1)

fee_paid_entry = Entry(width=20)
fee_paid_entry.grid(row=7, column=1)

name_entry = Entry(width=30)
name_entry.grid(row=9, column=1)

age_entry = Entry(width=15)
age_entry.grid(row=10, column=1)

#fee_paid_entry = Entry(width=20)
#fee_paid_entry.grid(row=11, column=1)



# creating button
total_fee_button = Button(text="add_fees", command=add_fees)
total_fee_button.grid(row=6, column=1)



record_student_label = ttk.Label(text="\nDO YOU WANT TO ADD MORE STUDENTS:")
record_student_label.grid(row=12, column=1)
record_student_button = ttk.Button( text='YES', command=student_details)
record_student_button.grid(row=12, column=2)

no_more_student_label = ttk.Label(text="\nDO YOU WANT TO RECORD THIS STUDENT:")
no_more_student_label.grid(row=13, column=1)
no_more_student_button = ttk.Button(text='NO', command=print_students)
no_more_student_button.grid(row=13, column=2)

print_button = ttk.Button(text='\nPrint Students', command=print_students)
print_button.grid(row=14, column=2)

output_text = Text()
output_text.grid(row=15, column=2)




window.mainloop()