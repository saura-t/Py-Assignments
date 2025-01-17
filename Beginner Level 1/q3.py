def gradeCalulator(s):
    marks = s.split(',')
    if len(marks) > 5:
        print("marks entered for too many subjects")
        return
    marks = list(map(int, marks))
    percent = (sum(marks)/(len(marks)*100))*100
    if percent >= 90:
        print("Grade A")
    elif percent >= 80:
        print("Grade B")
    elif percent >= 70:
        print("Grade C")
    elif percent >= 60:
        print("Grade D")
    elif percent >= 40:
        print("Grade E")
    elif percent <= 40:
        print("Grade F")


if __name__ == "__main__":
    try:
        s = input(
            "Enter subject marks for Physics, Chemistry, Biology, Mathematics, and Computer (seperate using ','): ")
        gradeCalulator(s)
    except ValueError as err:
        print("Only integers are allowed")
