# here's how you read an int as an input
# x = int(raw_input())

# here's how you read 2 int as an input
# (i, j) = map(int, raw_input().split())
import fileinput

# To add


def add(x, y):
        return x + y


# To subtract
def subtract(x, y):
    return x - y


# To multiply
def multiply(x, y):
    return x * y


# To divide
def divide(x, y):
    return x / y


# To modulo
def modulo(x, y):
    return x % y

# read number of tests
# tests = int(raw_input())
# this is where you put your solution
# solving the problem description

if __name__ == '__main__':

    for line in fileinput.input():
        operation = raw_input()
        space = raw_input()
        (i, j) = map(int, raw_input().split())

        if operation == '+':
            print(add(i, j))

        elif operation == '-':
            print(subtract(i, j))

        elif operation == '*':
            print(multiply(i, j))

        elif operation == '/':
            print(divide(i, j))

        elif operation == '%':
            print(modulo(i, j))

# here's how you output the result
# print (i)
