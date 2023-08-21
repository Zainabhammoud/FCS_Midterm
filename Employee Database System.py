f = open('C:/Users/HP/Desktop/SE Factory/FCS_Midterm/file.txt','r') #https://www.w3schools.com/python/python_file_open.asp


# O(1) = n^0
count=0
correct_user="admin"
correct_pass="admin123123"

input_user=99
input_pass=99

#The dictionary 
employees={}



#Display the employees' statistics
def display_statistics(employees):
  male = 0
  female = 0
  for key, value in data.value(): #O(n)
    if value[2] == "male":
      male+=1
    elif value[2] == "female":
      female+=1
  print("Male: "+ str(male))
  print("Female: "+ str(female))
    
#Add new employee 
def add_new_employee(employee_id, username, timestamp, gender, salary):#O(1)
    employee_id = f"emp{len(employees) + 1:03d}"
    username = input("Enter username: ")
    gender = input("Enter gender (male/female): ")
    salary = int(input("Enter salary: "))
    timestamp = input("Enter joining date (YYYYMMDD): ")
    
    employees[employee_id] = {
        'username': username,
        'timestamp': timestamp,
        'gender': gender,
        'salary': salary
    }
    print(f"Employee {employee_id} added successfully!")

#Display employees
def displayEmployee(employees):#O(1)
  for employee_id in employees:
        print(f"Employee ID: {emp_id}")
        print(f"Username: {emp_data['username']}")
        print(f"Join Date: {emp_data['join_date']}")
        print(f"Gender: {emp_data['gender']}")
        print(f"Salary: {emp_data['salary']}")
        print("")

#Check the salary
def Check_salary(employees):
  print()
    
#Change the salary
def change_salary(employees):#O(n)
    employee_id = input("Enter  ID: ")
    if employee_id in employees:
        new_salary = input("Enter new salary: ")
        employees[employee_id]['salary'] = new_salary
        print(f"Salary updated successfully!")
    else:
        print("Operation cannot be completed.")

#Remove the employees
def remove_employee(employees):
    username=input("Enter the username of the employee to be removed ")
    if username in employees:
      employees.pop(username)
    else:
      print("Username not found")


#Raise the employees salary
def raise_salary(employees):
    employee_id = input("Enter  ID: ")
    if employee_id in employees:
        raise_percent = float(input("Enter raise percentage: "))
        employees[emp_id]['salary'] *= raise_percent
        print(f"The new salary is !" + salary)

#Display the menu for normal users 
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
        
#Check for login
def login():#O(n)

    read_employee_data('employee_data.txt')
    
    print("Welcome to the Employee Database System!")
    while count<5 and (correct_pass != input_pass or correct_user!= username):
      username = input("Enter username: ")
      password = input("Enter password: ")
    if correct_pass != input_pass or correct_user!= input_user:
      count+=1 # the user input incorrect credentials    
      print("Incorrect Username and/or Password!")    
    else: username == "admin" and password == "admin123123"
    print("Welcome, Admin!")
        
#Display the menu-options 
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