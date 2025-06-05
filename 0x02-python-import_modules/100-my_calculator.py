#!/usr/bin/python3

from calculator_1 import add, sub, div, mul
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
        
    input_a = sys.argv[1]
    input_b = sys.argv[3]
    operator = sys.argv[2]
        
    a = int(input_a)
    b = int(input_b)

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '/':
        result = div(a, b)
    elif operator == '*':
        result = mul(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, operator, b, result))

if __name__ == "__main__":
    main()

