#Christopher Monarrez M3P2

#variables
last_name = str(input("Enter Your Last Name: "))
midterm_score = float(input("Enter Your Midterm Score: "))
finalexam_score = float(input("Enter Your Final Exam Score: "))

#calculation
total_exam_points = (midterm_score * 0.4) + (finalexam_score * 0.6)

print(last_name)
print(total_exam_points)