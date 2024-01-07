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

if __name__ == '__main__':
    main()
