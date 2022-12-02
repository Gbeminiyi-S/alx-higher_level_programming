#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    import calculator_1
    if len(sys.argv) != 4:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == '+':
        print("{} + {} = {}".format(a, b, a + b))
    elif sys.argv[2] == '-':
        print("{} - {} = {}".format(a, b, a - b))
    elif sys.argv[2] == '*':
        print("{} * {} = {}".format(a, b, a * b))
    elif sys.argv[2] == '/':
        print("{} / {} = {}".format(a, b, a / b))
    else:
        print(f"Unknown operator. Available operators: +, -, * and /")
        exit(1)
    exit(0)
