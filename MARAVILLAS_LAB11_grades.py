Student_Grades = []
Pass_Grades = []
COUNTER_PASS = 0
COUNTER_FAILED = 0
num = 0

while True:
    num += 1
    USER_INPUT = input(f"Student Grade {num}: ")
    
    if USER_INPUT.lower() == "done":
       break
    
    elif USER_INPUT == "":
       continue
       
    elif not USER_INPUT.isdigit():
       print("Please Enter a Number")
       continue
         
    else:
       USER_INPUT = int(USER_INPUT)
       
    # CHECK IF INPUT NUMBER IS VALID (40-100)
    if USER_INPUT < 40 or USER_INPUT > 100:
         print("Invalid number")
         continue
    
    Student_Grades.append(USER_INPUT)

    # ADD COUNTER FOR PASSED GRADES
    if USER_INPUT >= 75:
         COUNTER_PASS += 1
         Pass_Grades.append(USER_INPUT)
    else:
         COUNTER_FAILED += 1

# AVERAGE, PASS PERCENTAGE CALCULATION
if Student_Grades and Pass_Grades:  # CHECK IF STUDENT GRADES AND PASS GRADES LIST ARE TRUE
    Sum = sum(Student_Grades) 
    Length = len(Student_Grades)
    Average = round(Sum / Length, 2) #AVERAGE FORMULA
    Pass_Percent = len(Pass_Grades) / len(Student_Grades) * 100 #PERCENT PASSING FORMULA
else:
    Average = 0
    Pass_Percent = 0

# DISPLAY 
print(f"Average Grade: {Average}")
print(f"Passed the Subject: {COUNTER_PASS}") 
print(f"Failed the Subject: {COUNTER_FAILED}")
print(f"PASSING %: {Pass_Percent:.2f} %")
print(f"Grades: {Student_Grades}")
    
     