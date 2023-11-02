from tuitions import Payment
from student import Student
print('setting fees:')
tuition = input("enter tuiton")
lib_fee = input("enter lib fee")
func_fee = input("enter func fee")
med_fee = ("enter medical fee")
#set_total_fees(cls, tuition, lib_fee, func_fee, med_fee):
#Payment.set_total_fees(500, 50, 100, 150)
Payment.set_total_fees(tuition, lib_fee, func_fee, med_fee)
print(f'Total total fees is {Payment.get_total_fees()}')
i=0

num_std = int(input("enter number of students"))
for i in range(num_std):
    print(f"enter student {i+1} details")

#std1 = Student('Musa', 23, 500)
#std2 = Student('Joe', 30, 650)
#std3 = Student('Eve', 30, 1500)
#std4 = Student('Isa', 30, 1500)

    name = input("enter student name: ")
    age = int(input("enter student age: "))
    fees = int(input("enter fees paid by the studente: "))

    std1 = Student(name,age,fees)

stds = std1.get_all_students()

#print(f'Total fees is {Payment.get_total_fees()}')

print('These are all the Students')
i=0
for std in stds:
    print(f'Student {i+1}\n')
    print(std,'\n')
    i+=1

print('These are students that have paid')
paid = Payment.get_paid_std()

for pa in paid:
    print(pa)