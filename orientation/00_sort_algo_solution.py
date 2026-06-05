def sort(arr):
    # This list will store the numbers in sorted order
    sortedArr = []

    # Keep running until all items have been removed from arr
    while len(arr) != 0:

        # Assume the first item is the smallest
        smallest = int(arr[0])

        # Store the position of the smallest item
        smallestIndex = 0

        # Check every item in the list
        for index, item in enumerate(arr):

            # If we find a smaller item,
            # update smallest and its position
            if int(item) < smallest:
                smallest = int(item)
                smallestIndex = index

        # Remove the smallest item from the original list
        arr.pop(smallestIndex)

        # Add the smallest item to the sorted list
        sortedArr.append(smallest)

        # Show the current state after each pass
        print("Remaining:", arr, "Sorted:", sortedArr)


# Ask the user to enter numbers separated by commas
# Example: 5,2,8,1,3
arr = input("Enter the array: ")

# Split the input string into a list
# "5,2,8,1,3" becomes ["5", "2", "8", "1", "3"]
arr = arr.split(",")

# Sort the list
sort(arr)
