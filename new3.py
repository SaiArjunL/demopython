a = 1
b = 2

try:
    print("Good Morning!!!!")
    print(a/b)
    value = int(input("Enter any value: "))
    print(value)
except ZeroDivisionError:
    print("You can't divide a number by Zero -", l)
except ValueError:
    print("Invalid Input")
except Exception:
    print("Something went wrong")
finally:
    print("Bye!!!!")
