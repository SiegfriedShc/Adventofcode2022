from collections import Counter

answer = 0
with open("D:\Repos\Adventofcode2022\day3\input.txt") as file:
    for bag in file:
        bag = bag.strip()

        # Divide the string in 2 equal-length substrings
        sizeHalfpack = len(bag) // 2
        halfpack1 = bag[:sizeHalfpack]
        halfpack2 = bag[sizeHalfpack:]

        # convert both strings into counter dictionary
        dict1 = Counter(halfpack1)
        dict2 = Counter(halfpack2)

        # take intersection of these dictionaries
        commonDict = dict1 & dict2

        # For each char that is common to both dictionnary :
            # meaning common item in both subparts of the bag
        # add the elf priority of the letter to the answer
        # note that ord() gives the ASCII value, to get elf priority, substract 96 when lowercase, substract 38 when uppercase
        for element in commonDict.elements():
            asciiValue = ord(element)
            if (asciiValue >= 65 and asciiValue <= 90): #uppercase
                elficValue = asciiValue - 38
            elif (asciiValue >= 97 and asciiValue <= 122): #lowercase
                elficValue =  asciiValue - 96
            else:
                print("char out of ascii values of letters\n")
                quit()
            answer += elficValue
            break #we just want the first
print(answer)