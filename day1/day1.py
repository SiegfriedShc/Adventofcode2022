max1, max2, max3, current = 0, 0, 0, 0
with open("input1.txt") as file:
    for line in file:
        line = line.strip()
        if line:
            current += int(line)
        else:
            if current > max1:
                max3 = max2
                max2 = max1
                max1 = current
            elif current > max2:
                max3 = max2
                max2 = current
            elif current > max3:
                max3 = current
            current = 0
print(max1+max2+max3)