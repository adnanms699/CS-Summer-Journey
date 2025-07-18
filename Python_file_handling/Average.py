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
# create a dictionary to hold scores by name
grades_data = {}
top_score = {}

with open('grades.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row  
    # Get the name and score from each row
    for row in csv_reader:
        name = row[0]
        score = int(row[2])
        # Group scores by name
        if name in grades_data:
            grades_data[name].append(score)
        else:
            grades_data[name] = [score]
        
for name, scores in grades_data.items():
    Average = sum(scores) / len(scores)
    print(f"Average score of {name} is {Average:.2f}")
    
with open('grades.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row  
    # Get the name and score from each row
    for row in csv_reader:
        name = row[0]
        subject = row[1]
        score = int(row[2])
        # Group scores by name
        if subject not in top_score:
            top_score[subject] = {'top_scorer': name, 'top_scores': score}
        elif score > top_score[subject]['top_scores']:
            top_score[subject] = {'top_scorer': name, 'top_scores': score}
        
for subject, inf in top_score.items():
    print(f"Top scorer in {subject}:{inf['top_scorer']} with {inf['top_scores']}")