def getGrade(mark):
      #your code here
        grade = ""
        if mark >= 90:
            grade = "A"
        elif 80 <= mark < 90:
            grade = "B"
        elif 70 <= mark < 80:
            grade = "C"
        elif 60 <= mark < 70:
            grade = "D"
        else:
            grade = "F"
        return grade

print(getGrade(-10))





