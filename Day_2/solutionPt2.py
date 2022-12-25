class RockPaperScissors():
    def __init__(self):
        self.moves = self.readMoves();
    
    def readMoves(self):
        allMoves = []
        with open('input.txt', 'r') as moves:
            for move in moves:
                allMoves.append(move.strip())
        
        return allMoves


    def getMoves(self, opponentMove, userAction):
        if userAction == 'X':
            if opponentMove == 'A':
                return 'Scissor', 'Rock'
            
            elif opponentMove == 'B':
                return 'Rock', 'Paper'

            elif opponentMove == 'C':
                return 'Paper', 'Scissor'
        
        elif userAction == 'Y':
            if opponentMove == 'A':
                return 'Rock', 'Rock'
            
            elif opponentMove == 'B':
                return 'Paper', 'Paper'

            elif opponentMove == 'C':
                return 'Scissor', 'Scissor'
        
        elif userAction == 'Z':
            if opponentMove == 'A':
                return 'Paper', 'Rock'
            
            elif opponentMove == 'B':
                return 'Scissor', 'Paper'

            elif opponentMove == 'C':
                return 'Rock', 'Scissor'

    def UserVsOpponent(self, user, opponent):
        user_score = 0
        opponent_score = 0
        if user == 'Rock':
            if opponent == 'Rock':
                user_score += 3
                opponent_score += 3

            elif opponent == 'Paper':
                opponent_score += 6
            
            elif opponent == 'Scissor':
                user_score += 6
        
        elif user == 'Paper':
            if opponent == 'Paper':
                user_score += 3
                opponent_score += 3

            elif opponent == 'Rock':
                user_score += 6
            
            elif opponent == 'Scissor':
                opponent_score += 6
        
        elif user == 'Scissor':
            if opponent == 'Scissor':
                user_score += 3
                opponent_score += 3

            elif opponent == 'Paper':
                user_score += 6
            
            elif opponent == 'Rock':
                opponent_score += 6

        return user_score, opponent_score



    def analyzeMoves(self, move):
        if move == 'Rock':
            return 1
        elif move == 'Paper':
            return 2
        elif move == 'Scissor':
            return 3


    def playerScore(self):
        playerTotal = 0
        for move in self.moves:
            playerMove, opponentMove = self.getMoves(move[0], move[2])
            player_score, opponent_score = self.UserVsOpponent(playerMove, opponentMove)
            player_score += self.analyzeMoves(playerMove)

            playerTotal += player_score
        return playerTotal 



result = RockPaperScissors()
print(result.winner())

# A = Rock
# B = Paper
# C = Scissor

# X = lose
# Y = draw
# Z = Win