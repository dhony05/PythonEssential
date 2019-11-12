
user_input = input("Enter a number:")

for i in range(user_input):
    if(i == 0):
        print(i)
    elif(i%15 == 0):
        print("FizzBuzz")
    elif(i%3 == 0):
        print("Fizz")
    elif(i%5):
        print("Buzz")
    else:
        print(i)


