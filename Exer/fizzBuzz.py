
if __name__ == "__main__":
    pass
user_input = input("Enter a number:")


def fizzBuzz(user_input):
    for i in range(user_input):
        if(i == 0):
            print(i)
        elif(i%15 == 0):
            print("FizzBuzz")
        elif(i%3 == 0):
            print("Fizz")
        elif(i%5 == 0):
            print("Buzz")
        else:
            print(i)

fizzBuzz(user_input)