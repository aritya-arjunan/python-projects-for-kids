def addition():
    first = int(input('What is your first number? '))
    second = int(input('What is your second number? '))
    print(first + second)

def subtraction():
    first = int(input('What is your first number? '))
    second = int(input('What is your second number? '))
    print(first - second)



def multiplication():
    first = int(input('What is your first number? '))
    second = int(input('What is your second number? '))
    print(first * second)



def division():
    first = int(input('What is your first number? '))
    second = int(input('What is your second number? '))
    print(first / second)




def modulo():
    first = int(input('What is your first number? '))
    second = int(input('What is your second number? '))
    print(first % second)


def calc_run():
    op = input('add, subtract, multiply, divide, or modulo? ')
    if op == 'add':
        addition()
    elif op == 'subtract':
        subtraction()
    elif op == 'multiply':
        multiplication()
    elif op == 'divide':
        division()
    elif op == 'modulo':
        modulo()
    else:
        print('Thank you. Goodbye')






calc_run()
