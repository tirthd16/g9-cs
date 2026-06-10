
# declare variable
sportsDict = {
    "cricket":0,
    "football":0,
    "basketball":0,
    "archery":0
}

# check remaining slots
def remainingSlots():
    for key in sportsDict:
        if sportsDict[key] < 10:
            return True
    return False

# Input the sport
def main():
    sportInput = input(
            """
                Which sport are you interested in?
                football, cricket, basketball or archery
            """
            )

    if sportsDict[sportInput] < 10:
        sportsDict[sportInput] += 1
        print("Successfully added, congrats!")
    else:
        if remainingSlots():
            print(sportsDict)
            main()
        else:
            pass


main()
