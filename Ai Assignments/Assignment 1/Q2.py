def GS(salary):
    if salary <= 10000:
        hra = 0.2
        da = 0.8
    elif salary <= 20000:
        hra = 0.25
        da = 0.9
    else:
        hra = 0.3
        da = 0.95

    hra = salary * hra
    da = salary * da
    gross_salary = salary + hra + da
    return gross_salary


def main():
    salary = float(input("basic salary of the employee: "))
    gs = GS(salary)
    print("Gross salary:", gs)


if __name__ == "__main__":
    main()
