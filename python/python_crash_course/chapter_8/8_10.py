list_of_messages = ['Hi','Hello','Good Morning!','Good Night!','Good Afternoon']

def show_messages(list_of_messages):
    send_messages = []
    while len(list_of_messages) != 0:
        for message in list_of_messages:
            print(message,'\n')
            send_messages.append(message)
            list_of_messages.remove(message)
    print(f"Messages to send: {list_of_messages}")
    print(f"Send Messages: {send_messages}")

show_messages(list_of_messages)
