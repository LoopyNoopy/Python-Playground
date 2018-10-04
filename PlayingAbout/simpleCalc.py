import sys, termios, tty, os, time
 
userNumber1 = input('Type first number: ')
userNumber2 = input('Type second number: ')

userNumber1 = int(userNumber1)
userNumber2 = int(userNumber2)


print("What do you want to do with the numbers?")

#Function which looks for which character is inputted
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 
button_delay = 0.2
 

while True:
    char = getch()
 
    if (char == "s"):
        print("Stop!")
        exit(0)
 
    if (char == "+"):
        answer = userNumber2 + userNumber1
        answer = str(answer)
        print("You have added the numbers, which gives you: " + answer)
        time.sleep(button_delay)
 
    elif (char == "-"):
        answer = userNumber1 - userNumber2
        answer = str(answer)
        print("You have subtracted the numbers, which gives you: " + answer)
        time.sleep(button_delay)
 
    elif (char == "*"):
        answer = userNumber1 * userNumber2
        answer = str(answer)
        print("You have multiplied the numbers, which gives you: " + answer)
        time.sleep(button_delay)
 
    elif (char == "/"):
        answer = userNumber1 / userNumber2
        answer = str(answer)
        print("You have divided the numbers, which gives you: " + answer)
        time.sleep(button_delay)