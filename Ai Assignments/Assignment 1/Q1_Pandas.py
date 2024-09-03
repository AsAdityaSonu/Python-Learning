import pandas as pd


class Student:
    def __init__(self, name, maths, english, science, it):
        self.maths = maths
        self.english = english
        self.science = science
        self.it = it


def cal(students):
    data = {
        "Subjects": ["Maths", "English", "Science", "IT", "OverAll"]

    }


def main():
    students = [
        Student('Aditya', 78, 67, 93, 67),
        Student('Aditya2', 68, 98, 65, 94),
        Student('Aditya3', 98, 97, 85, 91)
    ]

    cal(students)


if __name__ == "__main__":
    main()
