secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    user_input = int(input('Guess : '))
    guess_count += 1
    if user_input == secret_number:
        print('you won')
        break
else:
    print('you lost')
    

