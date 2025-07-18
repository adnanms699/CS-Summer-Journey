import csv

grades = [
    ['Name', 'Subject', 'Score'],
    ['Ali', 'Math', 85],
    ['Zara', 'Science', 78],
    ['Adnan', 'Math', 92],
    ['Zara', 'Math', 88],
    ['Ali', 'Science', 79],
    ['Adnan', 'Science', 95]
]
score = 0
with open('grades.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(grades)

grades_data = {}

with open('grades.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row  
    for row in csv_reader:
        subject = row[1]
        score = int(row[2])
        if subject in grades_data:
            grades_data[subject].append(score)
        else:
            grades_data[subject] = [score]
        
for subject, score in grades_data.items():
    Average = sum(score) / len(score)
    print(f"Average score of {subject} is {Average:.2f}")


        