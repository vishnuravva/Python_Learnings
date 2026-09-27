# students = {
#     "Vishnu":98,
#     "Yash":97,
#     "Harish":96
# }
# marksList = list(students.values())
# print(type(marksList))    
# champion = marksList[0]
# for i in range(1,len(marksList) + 1):
#     if(marksList[i] > marksList[i-1]):
#         champion = marksList[i]
#         print("Highest Marks: " + champion)  


# Mini application

# Build a simple student marks manager:

# 1. Add student
# 2. View students
# 3. Find highest marks
# 4. Calculate average
# 5. Exit
    
students = dict()
print("1. Add Student\n2. View Students\n3. Find highest marks\n4. Calculate average\n5. Exit")
while(True):
    print("Enter a valid input to operate")
    operation = int(input())
    match operation:
        case 1:
            print("Enter Student Name")
            student = input()
            print("Enter Marks")
            marks = int(input())
            students[student] = marks
        case 2:
            if students:
                for key, value in students.items():
                    print(f"Student: {key}, Marks: {value}")
            else:
                print("Kindly add students to view.")        
                
        case 3:
            # print(max(students.values()))  
            if students:
                marksList = list(students.values()) 
                champion = marksList[0]
                for i in range(1,len(marksList)):
                    if(marksList[i] > champion):
                        champion = marksList[i]
                print(f"Highest Marks: {champion}")
            else:
                print("No Student found. Kindly add students to view Highest marks.")        
        case 4:
            if students:
                avg = 0
                totalMarks = 0
                for marks in students.values():
                    totalMarks += marks
                print(f"Average Marks: {totalMarks / len(students)}")
            else:
                print("No Students found. Kindly add students to view Avg score.")        

        case _:
            print("Invalid Operation. Please choose between 1-5")
            break