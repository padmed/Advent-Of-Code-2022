class RockPaperScissors():
    def __init__(self):
        self.moves = self.readMoves();
    
    def readMoves(self):
        allMoves = []
        with open('input.txt', 'r') as moves:
            for move in moves:
                allMoves.append(move.strip())
        
        return allMoves

    def UserVsOpponent(self, user, opponent):
        user_score = 0
        opponent_score = 0
        if user == 'X':
            if opponent == 'A':
                user_score += 3
                opponent_score += 3

            elif opponent == 'B':
                opponent_score += 6
            
            elif opponent == 'C':
                user_score += 6
        
        elif user == 'Y':
            if opponent == 'B':
                user_score += 3
                opponent_score += 3

            elif opponent == 'A':
                user_score += 6
            
            elif opponent == 'C':
                opponent_score += 6
        
        elif user == 'Z':
            if opponent == 'C':
                user_score += 3
                opponent_score += 3

            elif opponent == 'B':
                user_score += 6
            
            elif opponent == 'A':
                opponent_score += 6

        return user_score, opponent_score


    def analyzeMoves(self, move):
        if move in ['A', 'X']:
            return 1
        elif move in ['B', 'Y']:
            return 2
        elif move in ['C', 'Z']:
            return 3


    def winner(self):
        playerTotal = 0
        for move in self.moves:
            playerMove = move[2]
            opponentMove = move[0]

            player_score, opponent_score = self.UserVsOpponent(playerMove, opponentMove)

            player_score += self.analyzeMoves(playerMove)
            opponent_score += self.analyzeMoves(opponentMove)
        
            playerTotal += player_score


        return playerTotal



result = RockPaperScissors()
print(result.winner())

# A, X = Rock
# B, Y = Paper
# C, Z = Scissor