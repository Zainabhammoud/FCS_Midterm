f = open('C:/Users/HP/Desktop/SE Factory/FCS_Midterm/file.txt','r') #https://www.w3schools.com/python/python_file_open.asp


# O(1) = n^0
count=0
correct_user="admin"
correct_pass="admin123123"

input_user=99
input_pass=99

employees={"employee_id", "username", 'timestamp', 'gender', 'salary'}

while count<5 and (correct_pass != input_pass or correct_user!= input_user):
  input_user=input("Enter your username ")
  input_pass=input("Enter your password ")

  if correct_pass != input_pass or correct_user!= input_user:
    count+=1 # the user input incorrect credentials    
    print("Incorrect Username and/or Password!")
  else:
    admin_menu();
    
  if correct_user == input_user and correct_pass == input_pass:
    print("Admin menu")
    



def display_statistics(employees):
  male = 0
  female = 0
  for key, value in data.value():
    if value[2] == "male":
      male+=1
    elif value[2] == "female":
      female+=1
  print("Male: "+ str(male))
  print("Female: "+ str(female))

def add_new_employee(employee_id, username, timestamp, gender, salary):
  employee_id=
  username =input("Enter the name of the employee: ")
  timestamp =(input("Enter the date of joining: "))
  gender =input("Enter his/her gender: ")
  salary=float(input("Enter the salary: "))
  if username in employees:
    print("Username already exists")
    return
  if salary<0:
    print("Invalid salary ")
    return
  employees[data]=[employee_id,username,timestamp,gender,salary]
  print()


def displayEmployee(employees):
  print()

                       
def Check_salary(employees):
  print()

def change_salary(employees):
  print()

def remove_employee(employees):
    username=input("Enter the username of the employee to be removed ")
    if username in employees:
      employees.pop(username)
    else:
      print("Username not found")


def raise_salary(employees):
  print()



  





def admin_menu():
  # give the user their option
  choice=None # dummy value
  while choice!=7:
    print("Enter:")
    print("1. Display Statistics")
    print("2. Add an Employee")
    print("3. Display all Employees")
    print("4. Change Employee’s Salary")
    print("5. Remove Employee")
    print("6. Raise Employee’s Salary")
    print("7. Exit")
    
    choice=int(input())  # take their input/choice
    if choice==1:
      display_statistics(employees)
    elif choice==2:
      add_new_employee(employee_id, username, timestamp, gender, salary)
    elif choice==3:
      displayEmployee(employees)
    elif choice==4:
      change_salary(employees)
    elif choice==5:
      remove_employee(employees)
    elif choice==6:
      raise_salary(employees)
    elif choice==7:
      print("Good bye")
    else:
      print("Wront input")
    
    
admin_menu()

def user_menu():
  choice=None # dummy value
  while choice!=2:
    print("Enter:")
    print("1. Check my Salary")
    print("2. Exit")
    choice=int(input())  # take their input/choice
    if choice==1:
      Check_salary(employees)
    elif choice==2:
      print("Good bye")
    else:
      print("Wront input")
user_menu()