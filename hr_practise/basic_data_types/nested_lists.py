'''Nested lists problem.

Given the names and grades for each student in a class of  students, store them
in a nested list and print the name(s) of any student(s) having the second
lowest grade.

Note: If there are multiple students with the second lowest grade, order their
names alphabetically and print each name on a new line.

Example:
records = [[""chi",20.0], ["beta",50.0], ["alpha",50.0]]
The ordered list of scores is [20.0,50.0], so the second lowest score is 50.0.
There are two students with that score: ["beta","alpha"]. Ordered
alphabetically, the names are printed as:
alpha
beta
'''

def second_lowest_grade(records):
    """Print the second lowest grade student name."""
    names = []
    scores = []
    student_names = []
    for record in records:
        names.append(record[0])
        scores.append(record[1])
    second_lowest_grade = sorted(set(scores))[1]
    for i in range(len(records)):
        if second_lowest_grade is records[i][1]:
            student_names.append(records[i][0])
    if len(student_names) > 1:
        for name in sorted(student_names):
            print(name)
        return sorted(student_names)
    return student_names

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    second_lowest_grade(records)