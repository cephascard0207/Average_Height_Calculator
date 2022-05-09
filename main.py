#Average_height
#Created by Cephas Cardozo
#Developed with Python

#welcome_print
print("Average Height")
print("Created By Cephas Cardozo")
print("Developed using Python\n")

#variable
student_heights = input("Input a list of student heights\nType here: ").split()

#for_loop
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

#variable
total_height = 0

#for_loops
for height in student_heights:
  total_height += height
number_of_students = 0

for student in student_heights:
  number_of_students +=1


#average_height -formula
average_height = round(total_height / number_of_students)

#average_height _print-statement
print(average_height)
