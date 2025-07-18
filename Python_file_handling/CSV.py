# Reading a csv file in Python
import csv

with open('new.csv','r', encoding='utf8') as file:
  csv_reader = csv.reader(file)

  for row in csv_reader:
    print(row)

# Writing to a csv file in Python
import csv

data_to_write = [
  ['Name', 'Age', 'Grade'],
  ['Alice', 25, 'A'],
  ['Bob', 22, 'B'],
  ['Charlie', 28, 'A+']
]

with open('new.csv','r', encoding='utf8') as file:
  csv_writer = csv.writer(file)

  csv_writer.writes(data_to_write)