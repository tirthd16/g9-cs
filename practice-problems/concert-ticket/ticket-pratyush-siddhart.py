def main():
    a = 20  # ticket price
    c = 25  # number of tickets allowed

    b = input("enter no. of tickets")

    # try to convert input to an integer
    try:
        b = int(b)

        if b > c:
            print("ERROR")
        else:
            if b < 10:
                total_cost = b * a
                print("Total cost is:", total_cost)

            else:
                if b < 20:
                    a = 18
                    total_cost = b * a
                    print("Total cost is:", total_cost)

                else:
                    a = 16
                    total_cost = b * a
                    print("Total cost is:", total_cost)

    # what to do if input cannot be converted to an integer
    except:
        print("input is not a number")

        # run the program again
        main()


main()
