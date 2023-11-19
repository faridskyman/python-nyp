def main():
    try:
        num1 = int(input('Enter a number: '))
        num2 = int(input('Enter another number: '))
        result = num1 / num2
        print('{} divided by {} is {}'.format(num1, num2, result))
    except ValueError:
        print("pls enter in an inter")
    except ZeroDivisionError:
        print("2nd number cant be zero")


main()