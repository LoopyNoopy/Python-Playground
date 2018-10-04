userNumber1 = input('Type first number: ')
userNumber2 = input('Type second number: ')

userNumber1 = int(userNumber1)
userNumber2 = int(userNumber2)

def fnMultiply(no1, no2):
    return no1*no2;
    
multiplyAnswer = fnMultiply(userNumber1, userNumber2)

answer = userNumber1 + userNumber2;

answer = str(answer)
multiplyAnswer = str(multiplyAnswer)


print ("The answer is: " + answer)
print ("Multiplying these numbers together gives you: " + multiplyAnswer)

