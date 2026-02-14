def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed! "

def power(a,b):
    return a**b

def calculator():
    print("Simple Calculator CLI based")
    print("Select Operation:")
    print("1.Add(+)")
    print("2.Subtract(-)")
    print("3.Multiply(*)")
    print("4.Divide(/)") 
    print("5.Power(a^b)")
    print("6.Exit")

    while True:
        try:
            choice = input("Enter your choice (1-6):")
            if choice == '6':
                print("Thanks for using simple calculator!!!")
                break

            if choice not in ['1', '2', '3', '4', '5', '6']:
                print("Invalid input Please input (1-6) ")
                continue

            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter first number:"))

            if choice == '1':
                print(f"result: {num1} + {num2} = {add(num1,num2)}")
            elif choice == '2':
                print(f"result: {num1} - {num2} + {subtract(num1,num2)}")
            elif choice == '3':
                print(f"result: {num1} * {num2} = {multiply(num1,num2)}")
            elif choice == '4':
                print(f"result: {num1} / {num2} = {divide(num1,num2)}")
            elif choice == '5':
                print(f"result: {num1} ^ {num2} = {power(num1,num2)}")

        except ValueError:
             print("Error: Invalid input")
        except Exception as e:
            print(f"An error occurred {e}")

if __name__ == "__main__":
    calculator()