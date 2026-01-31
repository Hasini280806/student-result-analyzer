def calculate_result(marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = 'A'
    elif average >= 75:
        grade = 'B'
    elif average >= 60:
        grade = 'C'
    else:
        grade = 'D'

    return total, average, grade


if __name__ == "__main__":
    marks = list(map(int, input("Enter marks separated by space: ").split()))
    total, average, grade = calculate_result(marks)

    print("Total Marks:", total)
    print("Average:", average)
    print("Grade:", grade)
