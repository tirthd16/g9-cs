arr = input("Enter the array: ")

# Split the input string into a list
# "5,2,8,1,3" becomes ["5", "2", "8", "1", "3"]
arr = arr.split(",")
arr = [int(item) for item in arr] 

def main(arr,n):
    print(arr,n)
    first = (arr[n])
    second = (arr[n+1])
    if first>second:
        newFirst = second
        newSecond = first
        arr[n] = newFirst
        arr[n+1] = newSecond
    if n<(len(arr)-2):
        n=n+1
        main(arr,n)
    else:
        print(arr)

main(arr,0)
