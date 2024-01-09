from algorithm import calculator


def main():
    while True:
        try:
            string = input("enter what do u want to calculate:")
            print(calculator(string))
            break
        except ValueError as err:
            print(err)
            print(" --------------------------------------- ")
        except EOFError:
            print("EOFError: no input received")
            print(" --------------------------------------- ")
            break


if __name__ == '__main__':
    main()
