
# O(1) = n^0
count=0
correct_user="admin"
correct_pass="admin123123"

input_user=99
input_pass=99

while count<5 and (correct_pass != input_pass or correct_user!= input_user):
  input_user=input("enter your username ")
  input_pass=input("enter your password")

  if correct_pass != input_pass or correct_user!= input_user:
    count+=1 # the user input incorrect credentials