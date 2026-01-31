def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"


def save_result(name, marks):
    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)

    with open("results.txt", "a") as file:
        file.write(f"{name},{total},{average:.2f},{grade}\n")


def show_results():
    print("\n--- Student Results ---")
    with open("results.txt", "r") as file:
        for line in file:
            name, total, avg, grade = line.strip().split(",")
            print(f"Name: {name}, Total: {total}, Avg: {avg}, Grade: {grade}")


name = input("Enter student name: ")

marks = []
for i in range(3):
    marks.append(int(input(f"Enter marks for subject {i+1}: ")))

save_result(name, marks)
show_results()
