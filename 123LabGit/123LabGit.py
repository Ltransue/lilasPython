def yearInSchool(grade):
    if grade == 9:
        return("Freshman")

    elif grade==10:
        return("Sophomore")

    elif grade==11:
        return("Junior")

    else:
        return("Senior")

def getGpa(grades, length):
    if length == 4:
        gpa = float((grades[0] + grades[1] + grades[2] + grades[3])/length)
    elif length == 5:
        gpa = float((grades[0] + grades[1] + grades[2] + grades[3] + grades[4])/length)
    else:
        gpa = float((grades[0] + grades[1] + grades[2] + grades[3] + grades[4] + grades[5])/length)

    return(str(gpa))

def getLetterGrade(myGpa):
    if float(myGpa) >= 90:
        return("A")
    elif float(myGpa)>= 80:
        return("B")
    elif float(myGpa)>= 70:
        return("C")
    elif float(myGpa)>= 60:
        return("D")
    else:
        return("F")




gradeInSchool = int(input("What grade are you in?"))

print("Congrats, you are a " + yearInSchool(gradeInSchool) + "!!")

gradeList = [59.2, 68.9, 77.5, 64.3, 44.0]

gradeListLength = len(gradeList)

print("Your current GPA is " + getGpa(gradeList, gradeListLength))

print("Your current Letter Grade is: " + getLetterGrade(getGpa(gradeList, gradeListLength)))

if ((getLetterGrade(getGpa(gradeList, gradeListLength))== "A") or (getLetterGrade(getGpa(gradeList, gradeListLength)) == "B")) or (getLetterGrade(getGpa(gradeList, gradeListLength)) == "C"):
     print("Congratulations, you are passing.")
else:
    print("You'd better get to work, you are failing")
