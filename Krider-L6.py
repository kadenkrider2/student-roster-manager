

name = input("Please enter a name: ")

v_num = input("Please enter a V number: ")

grade = input("Please enter what grade they are in: ")

info = (name, v_num, grade)

with open("roster.txt", 'w') as file:
    file.write(" ".join(info) + "\n")

enter = input("Enter another student? (y/n) ")

while enter != 'n':
    name = input("Please enter a name: ")
    v_num = input("Please enter a V number: ")
    grade = input("Please enter what grade they are in: ")
    
    info = (name, v_num, grade)
    
with open("roster.txt", 'a') as file:
        file.write(" ".join(info) + '\n')  
 enter = input("Enter another student? (y/n) ")

if enter == 'n':
    print("Thanks for the info!")




