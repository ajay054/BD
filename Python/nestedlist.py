if __name__ == '__main__':
    n = int(input())  # Number of students
    students = []  # List to store student names and grades

    # Accept input for each student
    for _ in range(n):
        name = input()  # Student name
        grade = float(input())  # Student grade
        students.append([name, grade])  # Append student name and grade to the list

    # Sort the list based on grades in ascending order
    sorted_students = sorted(students, key=lambda x: x[1])

    # Find the second lowest grade
    second_lowest_grade = sorted_students[1][1]

    # Find names of students with the second lowest grade
    second_lowest_students = [student[0] for student in sorted_students if student[1] == second_lowest_grade]

    # Print the names alphabetically
    for student_name in sorted(second_lowest_students):
        print(student_name)
