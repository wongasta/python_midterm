def FindFizzBuzz(number):

    count = 0
    for count in range(1, 30):
        if count % 3 == 0 and count % 5 == 0:
            print("FizzBuzz")
        elif count % 3 == 0:
            print("Fizz")
        elif count % 5 == 0:
            print("Buzz")
        else:
            print(count)
        count += 1
        


FindFizzBuzz(100)

