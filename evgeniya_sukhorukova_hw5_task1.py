while True:
    password = input("Hello, please enter your password.\n")
    password2 = input("Please enter your password one more time.\n")
    if password == password2:
        print('You are welcome!')
        break
    elif password != password2:
        print('Try again!\n')




