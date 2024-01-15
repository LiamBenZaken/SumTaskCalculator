from algorithm import calculator


def main():
    while True:
        try:
            string = input("enter what do u want to calculate:")
            print(calculator(string))
        except (ValueError, OverflowError, ArithmeticError) as err:
            print(err)
            print(" --------------------------------------- ")
        except (EOFError, KeyboardInterrupt) as err:
            print(err)
            print(" --------------------------------------- ")
            break


if __name__ == '__main__':
    main()
