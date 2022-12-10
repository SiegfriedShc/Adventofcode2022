score = 0
# Here 1 is ROCK, 2 is PAPER, and 3 is SCISSORS, as per score values.
dictionnary = {"A":1, "B":2, "C":3, "X":1, "Y":2, "Z":3}
with open("input.txt") as file:
    for line in file:
        mymove = dictionnary[line[2]]
        score += mymove
        # As per winning table, for elf - you : Draw on 0 (obviously), Win on -1 or 2, Lose on 1 or -2
        match dictionnary[line[0]] - mymove :
            case 0 :
                score += 3
            case -1 : 
                score += 6
            case 2 :
                score += 6
print(f"score: {score}")