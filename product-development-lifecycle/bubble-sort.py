arr = input("Enter the array: ")

# Split the input string into a list
# "5,2,8,1,3" becomes ["5", "2", "8", "1", "3"]
arr = arr.split(",")

# convert each item of array from string to integer
# ["5", "2", "8", "1", "3"] becomes [5, 2, 8, 1, 3]
arr = [int(item) for item in arr] 

def moveBiggestToLast(arr,stop):
    """
    This function takes in 2 arguments:
        arr : The array that we want to operate on
        stop: Until what index to compare values

    It compares two succesive values ( compare 1st value with 2nd value, 2nd value with 3rd)
    And swap if first_value is greater than second_value
    """

    n=0 
    # Start with comparing index(0) with index(1)

    while n<stop-1:
        # This while statement increases n by one until
        # we reach last second term of array.

        # Declare variable for nth term & (n+1)th term of array
        first = (arr[n]) 
        second = (arr[n+1])

        if first>second:
            # Swap the values
            newFirst = second
            newSecond = first
            arr[n] = newFirst
            arr[n+1] = newSecond
        else:
            pass

        # Increment n by one
        n=n+1

    # exit & print the sorted array
    print("move",arr)
    return(arr)

def repeatMovingBiggestToLast(arr):
    n = 0

    # run loop until only first two values of array are left
    while n<len(arr)-1:

        # until what index we need to sort?
        # For first run we need to consider till last index
        # For second run we only need to consider till last second index
        # And so on
        stop = len(arr)-n

        # Move the biggest term in this array to end
        arr = moveBiggestToLast(arr,stop)

        print(arr)

        # Increment n by one
        n=n+1


repeatMovingBiggestToLast(arr)
