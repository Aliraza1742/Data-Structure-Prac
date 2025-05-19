import numpy as np

ARRAY1 = np.array([[1, 23, 45, 67], [2, 36, 39, 42], [3, 50, 12, 34], [4, 45, 42, 31]])


def Student_scored_highest_marks(ARRAY1):
    Subject = 1
    marks = 0
    while Subject < 4:
        for i in ARRAY1:
            if i[Subject] > marks:
                marks = i[Subject]
                Roll_Number = i[0]

        print("The Roll number who got highest marks in Subject ", Subject, "is", Roll_Number, "Marks are", marks)
        Subject += 1
        marks = 0


hm = Student_scored_highest_marks(ARRAY1)


def Each_subject_highest(ARRAY1):
    for i in ARRAY1:
        marks = 0
        subject = 0
        for j in i[1:]:
            if j > marks:
                marks = j
                subject += 1
        print("THE Roll number :", i[0], "Got highest marks in Subject :", subject, "Such that ", marks)


esh = Each_subject_highest(ARRAY1)


def Student_scored_lowest_marks(ARRAY1):
    Subject = 1
    marks = 150
    while Subject < 4:
        for i in ARRAY1:
            if i[Subject] < marks:
                marks = i[Subject]
                Roll_Number = i[0]

        print("The Roll number who got lowest marks in Subject ", Subject, "is", Roll_Number, "Marks are ", marks)
        Subject += 1
        marks = 150


lm = Student_scored_lowest_marks(ARRAY1)


def Each_subject_lowest(ARRAY1):
    for i in ARRAY1:
        marks = 150
        subject = 0
        for j in i[1:]:
            if j < marks:
                marks = j
                subject += 1
        print("THE Roll number :", i[0], "Got lowest marks in Subject :", subject, "Such that ", marks)


esl = Each_subject_lowest(ARRAY1)


def Average_Marks_of_each_student(ARRAY1):
    for i in ARRAY1:
        sum = 0
        for j in i[1:]:
            sum = sum + j
            Average = sum // 3
        print("The average of the roll number ", i[0], "is : ", Average)


Average_marks = Average_Marks_of_each_student(ARRAY1)


def Highest_average_student(ARRAY1):
    High_Average = 0
    for i in ARRAY1:
        add = 0
        for j in i[1:]:
            add = add + j
        Average = add // 3
        if Average > High_Average:
            High_Average = Average
            Roll_number = i[0]
    print("The Roll number who got the highest Average is :", Roll_number, "such that it's Average is :", High_Average)


Highest_Average = Highest_average_student(ARRAY1)


def Lowest_average_student(ARRAY1):
    Low_Average = 100
    for i in ARRAY1:
        add = 0
        for j in i[1:]:
            add = add + j
        Average = add // 3
        if Average < Low_Average:
            Low_Average = Average
            Roll_number = i[0]
    print("The Roll number who got the lowest Average is :", Roll_number, "such that it's Average is :", Low_Average)


Lowest_Average = Lowest_average_student(ARRAY1)


def Total_Marks_of_each_student(ARRAY1):
    for i in ARRAY1:
        add = 0
        for j in i[1:]:
            add = add + j
        print("The Total Marks of Roll number :", i[0], " is :", add)


Total_marks = Total_Marks_of_each_student(ARRAY1)