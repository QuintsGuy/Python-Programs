def fizz_buzz(number):
    if number%15==0:
        return "FizzBuzz"
    elif number%5==0:
        return "Buzz"
    elif number%3==0:
        return "Fizz"
    else:
        return number

number=int(input("Enter a number greater than 0: "))
solution=(fizz_buzz(number))
print(solution)