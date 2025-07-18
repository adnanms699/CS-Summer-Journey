sent_message = 'Hey there! this is a secret message'
with open('sent_message.txt', 'w') as file:
    file.write(sent_message)

with open('sent_message.txt', 'r+') as file:
    file.seek(0)

    unsent_message = 'This message is getting deleted'

    file.write(unsent_message)
    file.truncate(len(unsent_message))

with open('sent_message.txt', 'r') as file:
    content = file.read()
    print(content)

# print(sent_message)
# print(unsent_message)
