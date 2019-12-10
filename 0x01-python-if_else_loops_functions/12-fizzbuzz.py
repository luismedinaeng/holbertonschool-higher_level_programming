def fizzbuzz():
    for i in range(1, 101):
        s = " "
        if i % 3 is 0 and i % 5 is 0:
            print("FizzBuzz", end=s)
        elif i % 3 is 0:
            print("Fizz", end=s)
        elif i % 5 is 0:
            print("Buzz", end=s)
        else:
            print(i, end=s)
