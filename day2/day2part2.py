score = 0
# Here 1 is ROCK, 2 is PAPER, and 3 is SCISSORS, as per score values.
dictionnary = {"A":1, "B":2, "C":3}
winningTable = {1:2, 2:3, 3:1}
losingTable = {1:3, 2:1, 3:2}
with open("input.txt") as file:
    for line in file:
        match line[2]:
            case 'X' : #Lose
                score += losingTable[dictionnary[line[0]]] + 0
            case 'Y' : #Draw
                score += dictionnary[line[0]] + 3
            case 'Z' : #Win
                score += winningTable[dictionnary[line[0]]] + 6
print(f"score: {score}")