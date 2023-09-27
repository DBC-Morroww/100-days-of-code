# simple averaging tool utilising lists and loops to replicate sum() and len() functions

student_heights = input("Input a list of student heights seperated by a space ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height

number_of_students = 0
for height in student_heights:
    number_of_students += 1
    
average_height = total_height/number_of_students

print(f"The average height for this group is {average_height}")