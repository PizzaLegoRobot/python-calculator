operation = input('Operation (+, -, *, /): ')
match operation:
    case '+':
        num1 = float(input('First addend: '))
        num2 = float(input('Second addend: '))
        result = num1 + num2
    case '-':
        num1 = float(input('Minuend: '))
        num2 = float(input('Subtrahend: '))
        result = num1 - num2
    case '*':
        num1 = float(input('First factor: '))
        num2 = float(input('Second factor: '))
        result = num1 * num2
    case '/':
        num1 = float(input('Dividend: '))
        num2 = float(input('Divisor: '))
        result = num1 / num2

print(result)