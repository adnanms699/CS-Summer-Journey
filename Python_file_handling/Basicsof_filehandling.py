with open('diaries.txt', 'w') as file:
   file.write('Hello I am Adnan\n')

with open('diaries.txt', 'r') as file:
  content = file.read()
  print(content)