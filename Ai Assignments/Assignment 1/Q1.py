class Student:
    def __init__(self, name, maths, english, science, it):
        self.maths = maths
        self.english = english
        self.science = science
        self.it = it


def cal(students):
    highest_math = 0
    lowest_math = 100
    total_math = 0

    highest_english = 0
    lowest_english = 100
    total_english = 0

    highest_science = 0
    lowest_science = 100
    total_science = 0

    highest_it = 0
    lowest_it = 100
    total_it = 0

    for student in students:
        # Math
        total_math += student.maths
        if student.maths > highest_math:
            highest_math = student.maths
        if student.maths < lowest_math:
            lowest_math = student.maths

        # English
        total_english += student.english
        if student.english > highest_english:
            highest_english = student.english
        if student.english < lowest_english:
            lowest_english = student.english

        # Science
        total_science += student.science
        if student.science > highest_science:
            highest_science = student.science
        if student.science < lowest_science:
            lowest_science = student.science

        # IT
        total_it += student.it
        if student.it > highest_it:
            highest_it = student.it
        if student.it < lowest_it:
            lowest_it = student.it

    # Calculate averages
    num_students = len(students)
    average_math = total_math / num_students
    average_english = total_english / num_students
    average_science = total_science / num_students
    average_it = total_it / num_students

    overall_highest = max(highest_math, highest_english, highest_science, highest_it)
    overall_lowest = min(lowest_math, lowest_english, lowest_science, lowest_it)
    overall_average = (average_math + average_english + average_science + average_it) / 4

    # Print the results
    print("Maths - Highest:", highest_math, " Lowest:", lowest_math, " Average:", average_math)
    print("English - Highest:", highest_english, " Lowest:", lowest_english, " Average:", average_english)
    print("Science - Highest:", highest_science, " Lowest:", lowest_science, " Average:", average_science)
    print("IT - Highest:", highest_it, " Lowest:", lowest_it, " Average:", average_it)
    print("Overall - Highest:", overall_highest, " Lowest:", overall_lowest, " Average:", overall_average)


def main():
    students = [
        Student('Aditya', 78, 67, 93, 67),
        Student('Aditya2', 68, 98, 65, 94),
        Student('Aditya3', 98, 97, 85, 91)
    ]

    cal(students)


if __name__ == "__main__":
    main()
