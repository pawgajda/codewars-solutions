# https://www.codewars.com/kata/59f70440bee845599c000085
def sum_scores(grades):
    courses = len(grades)
    sum = 0
    good_grades = 0

    for grade in grades:
        if grade == "A":
            sum += 30
            good_grades += 1
        elif grade == "B":
            sum += 20
            good_grades += 1
        elif grade == "C":
            sum += 10
        elif grade == "D":
            sum += 5
    
    # calculate bonus score
    if courses >= 5 and courses == good_grades:
        sum += 20

    # return sum of all grades with bonus score
    return sum
        

def find_hack(arr):
    crackers = []

    for student in arr:
        # unpack student array entry
        student_name = student[0]
        student_score = student[1]
        student_grades = student[2]

        # calculate sum of all student's grades
        score_sum = sum_scores(student_grades)
        
        if student_score > 200:
            crackers.append(student_name)
        elif student_score > score_sum:
            crackers.append(student_name)

    return crackers
