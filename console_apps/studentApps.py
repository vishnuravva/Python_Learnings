# Mini application
# Build a simple student marks manager:
# 1. Add student
# 2. View students
# 3. Find highest marks
# 4. Calculate average
# 5. Search Student
# 6. Update Marks
# 7. Delete Student
# 8. Exit
students = dict()
print("1. Add Student\n2. View Students\n3. Find highest marks\n4. Calculate average\n5. Search Student\n6.Update marks\n7. Delete Student\n8. Exit")
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
        case 5:
            print("Enter a student name to search")
            searchStudent = input()
            
            if students:
                if searchStudent in students:
                    print("Student: ", searchStudent)
                    print("Marks: ", students[searchStudent])
                else:
                    print("No results found.")
            else:
                print("No Students found. Kindly add students to view Avg score.")     
        case 6:
            print("Enter a student name to update marks")
            searchStudent = input()
            
            if students:
                if searchStudent in students:
                    print("Enter marks to be updated for the student")
                    updatedMarks = int(input())
                    students[searchStudent] = updatedMarks
                    print(f"Updated marks for {searchStudent} successfully.")
                else:
                    print("No student found.")
            else:
                print("No Students found. Kindly add students to view Avg score.")     
        case 7:
            print("Enter a student name to delete from master")
            searchStudent = input()
            if students:
                if searchStudent in students:
                    print("Kindly confirm before deletion Yes / No")
                    confirm = input()
                    if confirm == "Yes":
                        del students[searchStudent]
                        print(f"Deleted Student {searchStudent} successfully.")
                else:
                    print("No results found.")
            else:
                print("No students found to delete.")         
        case 8:
            break
        case _:
            print("Invalid Operation. Please choose between 1-8")