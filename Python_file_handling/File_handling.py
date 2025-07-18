sent_message = 'Hey there! this is a secret message'
with open('sent_message.txt', 'w') as file:
    file.write(sent_message)

with open('sent_message.txt', 'r+') as file:
    file.truncate(10)

with open('sent_message.txt', 'r') as file:
    content = file.read()
    print(content)