while True:
    last_name = input("Enter last name (ZZZ to quit): ")

    if last_name == "ZZZ":
        break

    first_name = input("Enter first name: ")
    gpa = float(input("Enter GPA: "))

    if gpa >= 3.5:
        print(first_name, last_name, "made the Dean's List")
    elif gpa >= 3.25:
        print(first_name, last_name, "made the Honor Roll")
    else:
        print(first_name, last_name, "did not qualify")
