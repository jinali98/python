help = '''
start - to start the car
stop - to stop the car
quit - to exit
'''
is_playing = True
started = False
stopped = False

while is_playing == True:
    user_first_input = input('>').lower()

    if user_first_input == 'help':
        print(help)
    elif user_first_input == 'start' and not started:
        started = True
        print('Car Started')
    elif user_first_input == 'stop' and not stopped:
        stopped = True
        print('Car Stopped')
    elif user_first_input == 'start' and started:
        print('Car is already Started')
    elif user_first_input == 'stop' and stopped:
        print('Car is already Stopped')
    elif user_first_input == 'quit':
        is_playing = False
    else:
        print("I don't understand that...")
