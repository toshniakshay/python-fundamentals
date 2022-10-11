def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


try:
    divide(20, 0)
except ZeroDivisionError:
    print("Invalid operation")
finally:
    print('This gets executed no matter what is the return value of function')
