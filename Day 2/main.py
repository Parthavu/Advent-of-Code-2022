path = "/Users/parthaupadhya/Coding/Python/Advent of Code/Day 2/input.txt"

valX = 1
valY = 2
valZ = 3

inputFile = open(path)

def checkscoreFollowingGuideP1(strat: str) -> int:
    score = 0
    
    opponent = strat[0]
    me = strat[2]
    
    # I put Rock:
    if me == "X":
        score += valX
        
        # Opponent puts rock
        if opponent == "A":
            score += 3
        
        # Opponent puts paper
        if opponent == "B":
            score += 0
            
        # Opponent puts scissor
        if opponent == "C":
            score += 6
            
    # I put Paper:
    elif me == "Y":
        score += valY
        
        # Opponent puts rock
        if opponent == "A":
            score += 6
        
        # Opponent puts paper
        if opponent == "B":
            score += 3
            
        # Opponent puts scissor
        if opponent == "C":
            score += 0
        
    # I put Scissor:
    elif me == "Z":
        score += valZ
        
        # Opponent puts rock
        if opponent == "A":
            score += 0
        
        # Opponent puts paper
        if opponent == "B":
            score += 6
            
        # Opponent puts scissor
        if opponent == "C":
            score += 3
   
    return score

def checkscoreFollownigGuideP2(strat: str) -> int:
    score = 0
    
    opponent = strat[0]
    outcome = strat[2]
    
    # I need to lose:
    if outcome == "X":
        
        # Opponent puts rock
        if opponent == "A":
            score += valZ
        
        # Opponent puts paper
        if opponent == "B":
            score += valX
            
        # Opponent puts scissor
        if opponent == "C":
            score += valY
            
    # I need to tie:
    elif outcome == "Y":
        score += 3
        
        # Opponent puts rock
        if opponent == "A":
            score += valX
        
        # Opponent puts paper
        if opponent == "B":
            score += valY
            
        # Opponent puts scissor
        if opponent == "C":
            score += valZ
            
    # I need to win:
    elif outcome == "Z":
        score += 6
        
        # Opponent puts rock
        if opponent == "A":
            score += valY
        
        # Opponent puts paper
        if opponent == "B":
            score += valZ
            
        # Opponent puts scissor
        if opponent == "C":
            score += valX
    
    return score

lines = [line.rstrip() for line in inputFile]

score = 0

for line in lines:
    score += checkscoreFollowingGuideP1(line)
    
print(score)

score2 = 0

for line in lines:
    score2 += checkscoreFollownigGuideP2(line)
    
print(score2)