# Write code below 💖
import csv

csv_file_path = 'old.csv'

best_selling_book = None
max_sales = 0
try:
  with open(csv_file_path, 'r', encoding='utf8') as file:
    csv_reader = csv.reader(file)
    file.readline()  # Skip header row
    
    for row in csv_reader:
      current_sales = float(row[4])
      
      if current_sales > max_sales:
        max_sales = current_sales
        best_selling_book = row
        
  with open(csv_file_path, 'r', encoding='utf8') as file:
    csv_reader = csv.reader(file)
    file.readline() # Skip header row
    
    for row in csv_reader:
      current_sales = float(row[4])
      
      if current_sales > max_sales:
        max_sales = current_sales
        best_selling_book = row

  output_file_path = 'new.csv'
  with open(output_file_path, 'w', newline='') as file:
    csv_writer = csv.writer(file)
    
    csv_writer.writerow(['Book', 'Author', 'Sales in Millions'])
    csv_writer.writerow([best_selling_book[0], best_selling_book[1], best_selling_book[4]])

  print('Bestselling info written to', output_file_path)
except FileNotFoundError:
  print("CSV file not found. Please check the file path.")
